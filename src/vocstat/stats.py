from __future__ import annotations

from collections import Counter, defaultdict, deque
from statistics import mean
from typing import Any

from rdflib import Graph, URIRef
from rdflib.namespace import RDF, SKOS


SKOS_LABEL_PROPERTIES = (
    SKOS.prefLabel,
    SKOS.altLabel,
    SKOS.hiddenLabel,
)

SKOS_NOTE_PROPERTIES = (
    SKOS.note,
    SKOS.changeNote,
    SKOS.definition,
    SKOS.editorialNote,
    SKOS.example,
    SKOS.historyNote,
    SKOS.scopeNote,
)

SKOS_MAPPING_PROPERTIES = (
    SKOS.broadMatch,
    SKOS.closeMatch,
    SKOS.exactMatch,
    SKOS.mappingRelation,
    SKOS.narrowMatch,
    SKOS.relatedMatch,
)


def skos_statistics(graph: Graph) -> dict[str, Any]:
    concepts = set(graph.subjects(RDF.type, SKOS.Concept))
    hierarchy = hierarchy_statistics(graph, concepts)
    return {
        "concepts": len(concepts),
        "concept_schemes": count_type(graph, SKOS.ConceptScheme),
        "collections": count_type(graph, SKOS.Collection),
        "ordered_collections": count_type(graph, SKOS.OrderedCollection),
        "labels": predicate_counts(graph, SKOS_LABEL_PROPERTIES),
        "notes": predicate_counts(graph, SKOS_NOTE_PROPERTIES),
        "semantic_relations": predicate_counts(
            graph, (SKOS.broader, SKOS.narrower, SKOS.related)
        ),
        "mappings": predicate_counts(graph, SKOS_MAPPING_PROPERTIES),
        "hierarchy": hierarchy,
    }


def count_type(graph: Graph, rdf_type: URIRef) -> int:
    return len(set(graph.subjects(RDF.type, rdf_type)))


def predicate_counts(graph: Graph, predicates: tuple[URIRef, ...]) -> dict[str, int]:
    return {prefixed_name(predicate): len(list(graph.triples((None, predicate, None)))) for predicate in predicates}


def hierarchy_statistics(graph: Graph, concepts: set[Any]) -> dict[str, Any]:
    narrower_by_parent: dict[Any, set[Any]] = defaultdict(set)
    broader_by_child: dict[Any, set[Any]] = defaultdict(set)

    for child, _, parent in graph.triples((None, SKOS.broader, None)):
        broader_by_child[child].add(parent)
        narrower_by_parent[parent].add(child)

    for parent, _, child in graph.triples((None, SKOS.narrower, None)):
        narrower_by_parent[parent].add(child)
        broader_by_child[child].add(parent)

    roots = sorted(
        (concept for concept in concepts if not broader_by_child.get(concept)),
        key=str,
    )
    depths = concept_depths(roots, narrower_by_parent)
    level_counts = Counter(depths.values())
    concepts_with_depth = set(depths)
    orphaned = concepts - concepts_with_depth

    branch_factors = [
        len(children)
        for parent, children in narrower_by_parent.items()
        if parent in concepts and children
    ]

    top_five_count = sum(
        count for level, count in level_counts.items() if 1 <= level <= 5
    )
    concept_total = len(concepts)
    top_five_percentage = (
        round((top_five_count / concept_total) * 100, 2) if concept_total else 0
    )

    return {
        "roots": len(roots),
        "max_depth": max(level_counts, default=0),
        "level_counts": dict(sorted(level_counts.items())),
        "top_five_levels": {
            "concepts": top_five_count,
            "percentage": top_five_percentage,
        },
        "orphaned_or_cyclic_concepts": len(orphaned),
        "branching": {
            "average_children": round(mean(branch_factors), 2)
            if branch_factors
            else 0,
            "max_children": max(branch_factors, default=0),
        },
        "geometry": classify_geometry(level_counts, branch_factors, roots, concept_total),
    }


def concept_depths(
    roots: list[Any], narrower_by_parent: dict[Any, set[Any]]
) -> dict[Any, int]:
    depths: dict[Any, int] = {}
    queue = deque((root, 1) for root in roots)

    while queue:
        concept, depth = queue.popleft()
        current_depth = depths.get(concept)
        if current_depth is not None and current_depth <= depth:
            continue
        depths[concept] = depth
        for child in narrower_by_parent.get(concept, set()):
            queue.append((child, depth + 1))

    return depths


def classify_geometry(
    level_counts: Counter[int],
    branch_factors: list[int],
    roots: list[Any],
    concept_total: int,
) -> list[str]:
    if not concept_total:
        return ["empty"]

    labels: list[str] = []
    max_depth = max(level_counts, default=0)
    top_two = sum(count for level, count in level_counts.items() if level <= 2)
    lower_levels = sum(count for level, count in level_counts.items() if level >= 4)

    if max_depth <= 2:
        labels.append("shallow")
    if max_depth >= 8:
        labels.append("deep")
    if top_two / concept_total >= 0.65:
        labels.append("top-heavy")
    if lower_levels / concept_total >= 0.65:
        labels.append("bottom-heavy")
    if len(roots) > max(3, concept_total * 0.2):
        labels.append("fragmented")
    if branch_factors and max(branch_factors) >= max(10, mean(branch_factors) * 4):
        labels.append("lop-sided")

    return labels or ["moderate"]


def prefixed_name(uri: URIRef) -> str:
    text = str(uri)
    if text.startswith(str(SKOS)):
        return f"skos:{text.removeprefix(str(SKOS))}"
    return text


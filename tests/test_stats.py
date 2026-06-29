from rdflib import Graph

from vocstat.stats import skos_statistics


def test_tiny_skos_statistics() -> None:
    graph = Graph()
    graph.parse("examples/tiny-skos.ttl")

    stats = skos_statistics(graph)

    assert stats["concepts"] == 3
    assert stats["concept_schemes"] == 1
    assert stats["labels"]["skos:prefLabel"] == 4
    assert stats["labels"]["skos:altLabel"] == 1
    assert stats["hierarchy"]["roots"] == 1
    assert stats["hierarchy"]["max_depth"] == 2
    assert stats["hierarchy"]["top_five_levels"]["percentage"] == 100.0
    assert "shallow" in stats["hierarchy"]["geometry"]

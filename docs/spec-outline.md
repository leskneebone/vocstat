# VocStat Specification Outline

## 1. Scope

VocStat is an informational profile for analysing SKOS and SKOS-adjacent
vocabularies. It uses SHACL reports to surface observations, not only
constraint violations.

## 2. Principles

- Inform before judging.
- Distinguish standards-derived expectations from local policy.
- Treat `sh:Info` as the default severity for descriptive observations.
- Preserve room for stricter validation profiles where a project wants them.
- Account for all SKOS classes and properties.

## 3. Evidence Classes

- Standards-derived: ISO 25964, ANSI/NISO Z39.19, W3C SKOS.
- Secondary literature: thesaurus construction textbooks and peer-reviewed
  publications.
- Local policy: project-specific vocabulary governance rules.
- Empirical: observed statistical distributions across real vocabularies.

## 4. Draft Report Families

- Inventory: counts of SKOS classes, properties, labels, notes, relations, and
  mappings.
- Coverage: percentages for labels, notes, definitions, mappings, language tags,
  scheme membership, and top concepts.
- Hierarchy geometry: roots, leaves, levels, depth, branching, top-five-level
  concentration, isolated components, and lop-sided branches.
- Lexical patterns: preferred-label uniqueness, alternative label density,
  hidden label use, language distribution, casing, punctuation, and qualifier
  conventions.
- Semantic relations: broader/narrower reciprocity, related relation density,
  cycles, polyhierarchy, associative-link concentration.
- Mapping behaviour: exact, close, broad, narrow, and related mapping counts and
  target distributions.
- Documentation richness: definitions, scope notes, examples, change notes,
  editorial notes, and history notes.

## 5. SKOS Coverage Checklist

- Classes: `skos:Concept`, `skos:ConceptScheme`, `skos:Collection`,
  `skos:OrderedCollection`.
- Labelling: `skos:prefLabel`, `skos:altLabel`, `skos:hiddenLabel`.
- Documentation: `skos:note`, `skos:changeNote`, `skos:definition`,
  `skos:editorialNote`, `skos:example`, `skos:historyNote`, `skos:scopeNote`.
- Semantic relations: `skos:semanticRelation`, `skos:broader`,
  `skos:narrower`, `skos:related`, `skos:broaderTransitive`,
  `skos:narrowerTransitive`.
- Mapping relations: `skos:mappingRelation`, `skos:broadMatch`,
  `skos:closeMatch`, `skos:exactMatch`, `skos:narrowMatch`,
  `skos:relatedMatch`.
- Schemes: `skos:inScheme`, `skos:hasTopConcept`, `skos:topConceptOf`.
- Collections: `skos:member`, `skos:memberList`.
- Notation: `skos:notation`.

## 6. Open Design Questions

- Should VocStat define a custom `vocstat:Information` severity, or remain
  strictly SHACL-native with `sh:Info`?
- Should warnings from conventional SHACL validators be normalised into an
  informational report layer?
- How should standard-derived observations be cited inside SHACL shapes?
- Which geometry thresholds should be fixed by the spec, and which should be
  configurable by vocabulary type?


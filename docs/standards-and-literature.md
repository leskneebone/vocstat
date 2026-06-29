# Standards and Literature Register

This register favours primary standards first, then secondary sources that can
help translate standards into practical VocStat observations.

## Primary Standards

| Source | Status | Access notes | Relevance |
| --- | --- | --- | --- |
| ANSI/NISO Z39.19-2005 (R2010), *Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies* | Primary standard | Free PDF from NISO: https://www.niso.org/publications/ansiniso-z3919-2005-r2010 | US standard for controlled vocabulary and thesaurus construction. Useful for term choice, relationships, display, and management guidance. |
| ISO 25964-1:2011, *Thesauri and interoperability with other vocabularies - Part 1: Thesauri for information retrieval* | Primary standard | Paid ISO page: https://www.iso.org/standard/53657.html. ISO currently lists it as confirmed in 2022 and expected to be replaced by ISO/FDIS 25964-1. | ISO successor to ISO 2788 and ISO 5964 for thesaurus construction. This is the closest ISO equivalent to Z39.19. |
| ISO 25964-2:2013, *Thesauri and interoperability with other vocabularies - Part 2: Interoperability with other vocabularies* | Primary standard | Paid ISO page: https://www.iso.org/standard/53658.html. ISO currently lists it as confirmed in 2023. | Guidance for mapping and interoperability with other vocabularies, highly relevant to SKOS mapping statistics. |
| W3C SKOS Reference, 18 August 2009 | Web standard | Free W3C Recommendation: https://www.w3.org/TR/skos-reference/ | Normative source for SKOS classes and properties. VocStat should account for all of it. |
| W3C SKOS Primer, 18 August 2009 | W3C Working Group Note | Free W3C note: https://www.w3.org/TR/skos-primer/ | Practical explanatory companion to the SKOS Reference. |

## Useful Free or Open Resources

| Source | Access notes | Relevance |
| --- | --- | --- |
| ISO 25964 official website | https://www.niso.org/schemas/iso25964 | NISO-hosted XML schemas, data model resources, documentation, test document, and SKOS correspondence notes related to ISO 25964. Useful for implementation alignment. |
| ISO 25964 SKOS correspondence/RDF schema | http://purl.org/iso25964/skos-thes | Machine-readable correspondence work for ISO 25964 and SKOS. Useful later for shape annotations and possible compatibility checks. |
| Dextre Clarke and Zeng, work on ISO 25964 and thesaurus standards | Search for author copies and conference versions before using publisher copies. | Good bridge between standards history, data modelling, and interoperability. |
| W3C SKOS test cases and examples | https://www.w3.org/2004/02/skos/ | Useful for SKOS behaviour and validation examples. |

## Secondary Literature Candidates

These are likely useful, but each needs acquisition checking and bibliographic
cleanup before formal citation in the spec.

| Source | Candidate use |
| --- | --- |
| Jean Aitchison, Alan Gilchrist, and David Bawden, *Thesaurus Construction and Use: A Practical Manual* | Practical thesaurus construction rules, relationship types, facet and hierarchy guidance. Likely paid/used-book access. |
| Vanda Broughton, *Essential Thesaurus Construction* | Modern practical guide to thesaurus construction. Useful for translating standards into checks and explanatory statistics. |
| Stella G. Dextre Clarke and Marcia Lei Zeng publications on ISO 25964 | Standards evolution, data modelling, interoperability, and SKOS alignment. |
| Krooks and Lancaster, work on the evolution of thesaurus construction guidelines | Historical comparison of thesaurus standards and construction guidance. |
| Soergel, *Indexing Languages and Thesauri* | Deep theoretical treatment of thesauri and indexing languages. Usually paid/library access. |

## Acquisition Notes

- Do not commit paid standards PDFs to this repository unless licensing permits
  redistribution.
- Keep paid standards as bibliographic references plus local, untracked notes.
- Prefer open publisher pages, author manuscripts, institutional repositories,
  and standards-hosted schemas/examples for committed materials.
- Add a `docs/source-notes/` directory later for short, original notes keyed to
  page/section references.

## Immediate Research Tasks

- Verify the current ISO 25964 revision status before freezing citations.
- Locate stable public pages for ISO 25964 schemas, examples, and data model.
- Find open-access Dextre Clarke/Zeng papers or author copies.
- Decide whether VocStat should formally cite ANSI/NISO Z39.19, ISO 25964, or
  both in individual SHACL shape annotations.

---
title: "Graph-Based Dependency Parsing"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Gr: 19.3 • GRAPH-BASED DEPENDENCY PARSING score of the operator used to produce it. ConfigScore(c0) = 0.0 ConfigScore(ci) = ConfigScore(ci−1)+Score(ti,ci−1) This score is used both in filtering the agenda and in selecting"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "453-458"
---

# Graph-Based Dependency Parsing

§II Annotating Linguistic Structure › Dependency Parsing › Graph-Based Dependency Parsing · pp. 453–458 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
19.3 • GRAPH-BASED DEPENDENCY PARSING score of the operator used to produce it. ConfigScore(c0) = 0.0 ConfigScore(ci) = ConfigScore(ci−1)+Score(ti,ci−1) This score is used both in filtering the agenda and in selecting the final answer. The new beam search version of transition-based parsing is given in Fig. 19.10. function DEPENDENCYBEAMPARSE(words, width) returns dependency tree state←{[root], [words], [], 0.0} ;initial configuration agenda←⟨state⟩ ;initial agenda while agenda contains non-final states newagenda←⟨⟩ for each state ∈agenda do for all {t | t ∈VALIDOPERATORS(state)} do child←APPLY(t, state) newagenda←ADDTOBEAM(child, newagenda, width) agenda←newagenda return BESTOF(agenda) function ADDTOBEAM(state, agenda, width) returns updated agenda if LENGTH(agenda) < width then agenda←INSERT(state, agenda) else if SCORE(state) > SCORE(WORSTOF(agenda)) agenda←REMOVE(WORSTOF(agenda)) agenda←INSERT(state, agenda) return agenda Figure 19.10 Beam search applied to transition-based dependency parsing. Graph-based methods are the second important family of dependency parsing algorithms. Graph-based parsers are more accurate than transition-based parsers, especially on long sentences; transition-based methods have trouble when the heads are very far from the dependents (McDonald and Nivre, 2011).

## Key terms
- **tree** — 44 mentions
- **edge** — 42 mentions
- **score** — 37 mentions
- **spanning** — 26 mentions
- **graph** — 23 mentions
- **cycle** — 20 mentions
- **agenda** — 18 mentions
- **algorithm** — 17 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=453|Speech and Language Processing.pdf p. 453]]

## Liens
- Up: [[research/slp/dependency-parsing]]
- ← Prev: [[research/slp/transition-based-dependency-parsing]]
- Next: [[research/slp/evaluation]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "Representing Selectional Restrictions"
summary: "§II Annotating Linguistic Structure › Semantic Role Labeling : 21.7 • SELECTIONAL RESTRICTIONS One way to capture the semantics of selectional restrictions is to use and extend the event representation of Appendix F."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "501-501"
---

# Representing Selectional Restrictions

§II Annotating Linguistic Structure › Semantic Role Labeling › Selectional Restrictions › Representing Selectional Restrictions · pp. 501–501 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
21.7 • SELECTIONAL RESTRICTIONS One way to capture the semantics of selectional restrictions is to use and extend the event representation of Appendix F. Recall that the neo-Davidsonian representation of an event consists of a single variable that stands for the event, a predicate denoting the kind of event, and variables and relations for the event roles. Ignoring the issue of the λ-structures and using thematic roles rather than deep event roles, the semantic contribution of a verb like eat might look like the following: ∃e,x,y Eating(e)∧Agent(e,x)∧Theme(e,y) With this representation, all we know about y, the filler of the THEME role, is that it is associated with an Eating event through the Theme relation. To stipulate the selectional restriction that y must be something edible, we simply add a new term to that effect: ∃e,x,y Eating(e)∧Agent(e,x)∧Theme(e,y)∧EdibleThing(y) When a phrase like ate a hamburger is encountered, a semantic analyzer can form the following kind of representation: ∃e,x,y Eating(e)∧Eater(e,x)∧Theme(e,y)∧EdibleThing(y)∧Hamburger(y) This representation is perfectly reasonable since the membership of y in the category Hamburger is consistent with its membership in the category EdibleThing, assuming a reasonable set of facts in the knowledge base.

## Key terms
- **restriction** — 10 mentions
- **selectional** — 9 mentions
- **theme** — 9 mentions
- **hamburger** — 9 mentions
- **role** — 8 mentions
- **event** — 7 mentions
- **representation** — 7 mentions
- **synset** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=501|Speech and Language Processing.pdf p. 501]]

## Liens
- Up: [[research/slp/selectional-restrictions]]
- Next: [[research/slp/selectional-preferences]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "Creating an Oracle"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Tr: 19.2 • TRANSITION-BASED DEPENDENCY PARSING Step Stack Word List Action Relation Added [root] [book, me, the, morning, flight] SHIFT [root, book] [me, the, morning, flight] SHIFT [root, book, me] [the, morning, flight]"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "447-448"
---

# Creating an Oracle

§II Annotating Linguistic Structure › Dependency Parsing › Transition-Based Dependency Parsing › Creating an Oracle · pp. 447–448 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
19.2 • TRANSITION-BASED DEPENDENCY PARSING Step Stack Word List Action Relation Added [root] [book, me, the, morning, flight] SHIFT [root, book] [me, the, morning, flight] SHIFT [root, book, me] [the, morning, flight] RIGHTARC (book →me) [root, book] [the, morning, flight] SHIFT [root, book, the] [morning, flight] SHIFT [root, book, the, morning] [flight] SHIFT [root, book, the, morning, flight] [] LEFTARC (morning ←flight) [root, book, the, flight] [] LEFTARC (the ←flight) [root, book, flight] [] RIGHTARC (book →flight) [root, book] [] RIGHTARC (root →book) [root] [] Done Figure 19.6 Trace of a transition-based parse. Finally, for simplicity, we have illustrated this example without the labels on the dependency relations. To produce labeled trees, we can parameterize the LEFTARC and RIGHTARC operators with dependency labels, as in LEFTARC(NSUBJ) or RIGHTARC(OBJ). This is equivalent to expanding the set of transition operators from our original set of three to a set that includes LEFTARC and RIGHTARC operators for each relation in the set of dependency relations being used, plus an additional one for the SHIFT operator. This, of course, makes the job of the oracle more difficult since it now has a much larger set of operators from which to choose.

## Key terms
- **root** — 27 mentions
- **book** — 27 mentions
- **flight** — 22 mentions
- **shift** — 15 mentions
- **rightarc** — 15 mentions
- **relation** — 14 mentions
- **configuration** — 14 mentions
- **leftarc** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=447|Speech and Language Processing.pdf p. 447]]

## Liens
- Up: [[research/slp/transition-based-dependency-parsing]]
- Next: [[research/slp/a-feature-based-classifier]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

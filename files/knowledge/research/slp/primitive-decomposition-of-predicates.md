---
title: "Primitive Decomposition of Predicates"
summary: "§II Annotating Linguistic Structure › Semantic Role Labeling : CHAPTER 21 • SEMANTIC ROLE LABELING An even simpler approach is to use the simple log co-occurrence frequency of the predicate with the argument logcount(v,n,r) instead of conditional probability; this seems to do bet"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "504-504"
---

# Primitive Decomposition of Predicates

§II Annotating Linguistic Structure › Semantic Role Labeling › Primitive Decomposition of Predicates · pp. 504–504 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 21 • SEMANTIC ROLE LABELING An even simpler approach is to use the simple log co-occurrence frequency of the predicate with the argument logcount(v,n,r) instead of conditional probability; this seems to do better for extracting preferences for syntactic subjects rather than objects (Brockmann and Lapata, 2003). Evaluating Selectional Preferences One way to evaluate models of selectional preferences is to use pseudowords (Gale pseudowords et al. 1992b, Sch¨utze 1992a). A pseudoword is an artificial word created by concatenating a test word in some context (say banana) with a confounder word (say door) to create banana-door). The task of the system is to identify which of the two words is the original word. To evaluate a selectional preference model (for example on the relationship between a verb and a direct object) we take a test corpus and select all verb tokens. For each verb token (say drive) we select the direct object (e.g., car), concatenated with a confounder word that is its nearest neighbor, the noun with the frequency closest to the original (say house), to make car/house). We then use the selectional preference model to choose which of car and house are more preferred objects of drive, and compute how often the model chooses the correct original object (e.g., car) (Chambers and Jurafsky, 2010).

## Key terms
- **preference** — 8 mentions
- **semantic** — 6 mentions
- **word** — 6 mentions
- **selectional** — 5 mentions
- **door** — 5 mentions
- **model** — 5 mentions
- **object** — 5 mentions
- **become** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=504|Speech and Language Processing.pdf p. 504]]

## Liens
- Up: [[research/slp/semantic-role-labeling]]
- ← Prev: [[research/slp/selectional-restrictions]]
- Next: [[research/slp/summary-20]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

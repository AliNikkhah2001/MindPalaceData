---
title: "Neural Graph-based linking"
summary: "§II Annotating Linguistic Structure › Coreference Resolution : CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING where in(x) is the set of Wikipedia pages pointing to x and W is the set of all Wikipedia pages in the collection."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "550-551"
---

# Neural Graph-based linking

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › Entity Linking › Neural Graph-based linking · pp. 550–551 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING where in(x) is the set of Wikipedia pages pointing to x and W is the set of all Wikipedia pages in the collection. The vote given by anchor b to the candidate annotation a →X is the average, over all the possible entities of b, of their relatedness to X, weighted by their prior probability: vote(b,X) = |E(b)| X Y∈E(b) rel(X,Y)p(Y|b) (23.60) The total relatedness score for a →X is the sum of the votes of all the other anchors detected in q: relatedness(a →X) = X b∈Xq\a vote(b,X) (23.61) To score a →X, we combine relatedness and prior by choosing the entity X that has the highest relatedness(a →X), finding other entities within a small ϵ of this value, and from this set, choosing the entity with the highest prior P(X|a). The result of this step is a single entity assigned to each span in q. The TAGME algorithm has one further step of pruning spurious anchor/entity pairs, assigning a score averaging link probability with the coherence. coherence(a →X) = |S|−1 X B∈S\X rel(B,X) score(a →X) = coherence(a →X)+linkprob(a) (23.62) Finally, pairs are pruned if score(a →X) < λ, where the threshold λ is set on a held-out set. More recent entity linking models are based on bi-encoders, encoding a candidate mention span, encoding an entity, and computing the dot product between the encodings.

## Key terms
- **entity** — 23 mentions
- **mention** — 13 mentions
- **span** — 10 mentions
- **wikipedia** — 9 mentions
- **entities** — 8 mentions
- **score** — 8 mentions
- **linking** — 7 mentions
- **algorithm** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=550|Speech and Language Processing.pdf p. 550]]

## Liens
- Up: [[research/slp/entity-linking]]
- ← Prev: [[research/slp/linking-based-on-anchor-dictionaries-and-web-graph]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

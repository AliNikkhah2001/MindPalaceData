---
title: "A feature-based algorithm for assigning scores"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Gr: CHAPTER 19 • DEPENDENCY PARSING function MAXSPANNINGTREE(G=(V,E), root,score) returns spanning tree F←[] T’←[] score’←[] for each v ∈V do bestInEdge←argmaxe=(u,v)∈E score[e] F←F ∪bestInEdge for each e=(u,v) ∈E do scor"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "456-456"
---

# A feature-based algorithm for assigning scores

§II Annotating Linguistic Structure › Dependency Parsing › Graph-Based Dependency Parsing › A feature-based algorithm for assigning scores · pp. 456–456 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 19 • DEPENDENCY PARSING function MAXSPANNINGTREE(G=(V,E), root,score) returns spanning tree F←[] T’←[] score’←[] for each v ∈V do bestInEdge←argmaxe=(u,v)∈E score[e] F←F ∪bestInEdge for each e=(u,v) ∈E do score’[e]←score[e] −score[bestInEdge] if T=(V,F) is a spanning tree then return it else C←a cycle in F G’←CONTRACT(G, C) T’←MAXSPANNINGTREE(G’, root, score’) T←EXPAND(T’,C) return T function CONTRACT(G,C) returns contracted graph function EXPAND(T, C) returns expanded graph Figure 19.12 The Chu-Liu Edmonds algorithm for finding a maximum spanning tree in a weighted directed graph. On arbitrary directed graphs, this version of the CLE algorithm runs in O(mn) time, where m is the number of edges and n is the number of nodes. Since this particular application of the algorithm begins by constructing a fully connected graph m = n2 yielding a running time of O(n3). Gabow et al. (1986) present a more efficient implementation with a running time of O(m+nlogn). Recall that given a sentence, S, and a candidate tree, T, edge-factored parsing models make the simplification that the score for the tree is the sum of the scores of the edges that comprise the tree: score(S,T) = X e∈T score(S,e) In a feature-based algorithm we compute the edge score as a weighted sum of features extracted from it: score(S,e) = N X i=1 wi fi(S,e) Or more succinctly.

## Key terms
- **score** — 14 mentions
- **tree** — 6 mentions
- **return** — 5 mentions
- **graph** — 5 mentions
- **algorithm** — 4 mentions
- **feature** — 4 mentions
- **function** — 3 mentions
- **spanning** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=456|Speech and Language Processing.pdf p. 456]]

## Liens
- Up: [[research/slp/graph-based-dependency-parsing]]
- ← Prev: [[research/slp/parsing-via-finding-the-maximum-spanning-tree]]
- Next: [[research/slp/a-neural-algorithm-for-assigning-scores]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

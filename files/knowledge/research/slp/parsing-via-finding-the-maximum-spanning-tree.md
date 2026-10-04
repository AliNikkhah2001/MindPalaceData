---
title: "Parsing via finding the maximum spanning tree"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Gr: CHAPTER 19 • DEPENDENCY PARSING We’ll make the simplifying assumption that this score can be edge-factored, edge-factored meaning that the overall score for a tree is the sum of the scores of each of the scores of the"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "454-455"
---

# Parsing via finding the maximum spanning tree

§II Annotating Linguistic Structure › Dependency Parsing › Graph-Based Dependency Parsing › Parsing via finding the maximum spanning tree · pp. 454–455 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 19 • DEPENDENCY PARSING We’ll make the simplifying assumption that this score can be edge-factored, edge-factored meaning that the overall score for a tree is the sum of the scores of each of the scores of the edges that comprise the tree. Score(t,S) = X e∈t Score(e) Graph-based algorithms have to solve two problems: (1) assigning a score to each edge, and (2) finding the best parse tree given the scores of all potential edges. In the next few sections we’ll introduce solutions to these two problems, beginning with the second problem of finding trees, and then giving a feature-based and a neural algorithm for solving the first problem of assigning scores. In graph-based parsing, given a sentence S we start by creating a graph G which is a fully-connected, weighted, directed graph where the vertices are the input words and the directed edges represent all possible head-dependent assignments. We’ll include an additional ROOT node with outgoing edges directed at all of the other vertices. The weights of each edge in G reflect the score for each possible head-dependent relation assigned by some scoring algorithm. It turns out that finding the best dependency parse for S is equivalent to finding the maximum spanning tree over G.

## Key terms
- **edge** — 39 mentions
- **tree** — 30 mentions
- **spanning** — 23 mentions
- **cycle** — 19 mentions
- **graph** — 16 mentions
- **score** — 15 mentions
- **maximum** — 14 mentions
- **algorithm** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=454|Speech and Language Processing.pdf p. 454]]

## Liens
- Up: [[research/slp/graph-based-dependency-parsing]]
- Next: [[research/slp/a-feature-based-algorithm-for-assigning-scores]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

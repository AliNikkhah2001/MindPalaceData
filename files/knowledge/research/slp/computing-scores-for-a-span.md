---
title: "Computing Scores for a Span"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: 18.7 • SPAN-BASED NEURAL CONSTITUENCY PARSING just this manner. While the CKY parsing algorithm we’ve seen so far does great at enumerating all the possible parse trees for a sentence, it has a large problem: it doesn"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "431-431"
---

# Computing Scores for a Span

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › Span-Based Neural Constituency Parsing › Computing Scores for a Span · pp. 431–431 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
18.7 • SPAN-BASED NEURAL CONSTITUENCY PARSING just this manner. While the CKY parsing algorithm we’ve seen so far does great at enumerating all the possible parse trees for a sentence, it has a large problem: it doesn’t tell us which parse is the correct one! That is, it doesn’t disambiguate among the possible parses. To solve the disambiguation problem we’ll use a simple neural extension of the CKY algorithm. The intuition of such parsing algorithms (often called span-based constituency parsing, or neural CKY), is to train a neural classifier to assign a score to each constituent, and then use a modified version of CKY to combine these constituent scores to find the best-scoring parse tree. Here we’ll describe a version of the algorithm from Kitaev et al. (2019). This parser learns to map a span of words to a constituent, and, like CKY, hierarchically combines larger and larger spans to build the parse-tree bottom-up. But unlike classic CKY, this parser doesn’t use the hand-written grammar to constrain what constituents can be combined, instead just relying on the learned neural representations of spans to encode likely combinations. Let’s begin by considering just the constituent (we’ll call it a span) that lies between span fencepost positions i and j with non-terminal symbol label l.

## Key terms
- **span** — 10 mentions
- **constituent** — 6 mentions
- **neural** — 5 mentions
- **parse** — 5 mentions
- **score** — 5 mentions
- **parsing** — 4 mentions
- **algorithm** — 4 mentions
- **doesn** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=431|Speech and Language Processing.pdf p. 431]]

## Liens
- Up: [[research/slp/span-based-neural-constituency-parsing]]
- Next: [[research/slp/integrating-span-scores-into-a-parse]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

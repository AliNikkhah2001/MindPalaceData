---
title: "CTC"
summary: "§I Large Language Models › Automatic Speech Recognition › CTC: 15.5 • CTC codebook that has one codeword for each of the k clusters. codebook Then repeat iteratively until convergence: 1."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "363-366"
---

# CTC

§I Large Language Models › Automatic Speech Recognition › CTC · pp. 363–366 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
15.5 • CTC codebook that has one codeword for each of the k clusters. codebook Then repeat iteratively until convergence: 1. Assignment: For each vector v(i) in the dataset assign it to one of the k clusters by choosing the one with the nearest codeword µ. Most simply we can define ‘nearest’ as the cluster whose codeword has the smallest squared Euclidean distance to v(i). cluster(i) = argmin 1<j<k ||v(i) −µj||2 (15.14) where ||v|| is the L2 norm of the vector Pd j=1 v2 j 2. Re-estimation: Re-estimate the codeword for each cluster by recomputing the mean (centroid) of all the vectors in the cluster. If Si is the set of vectors in cluster i, then ∀i : µi = |Si| X v∈Si v (15.15) We pointed out in the previous section that speech recognition has two particular properties that make it very appropriate for the encoder-decoder architecture, where the encoder produces an encoding of the input that the decoder uses attention to explore. First, in speech we have a very long acoustic input sequence X mapping to a much shorter sequence of letters Y, and second, it’s hard to know exactly which part of X maps to which part of Y. In this section we briefly introduce an alternative to encoder-decoder: an algorithm and loss function called CTC, short for Connectionist Temporal ClassificaCTC tion (Graves et al., 2006), that deals with these problems in a very different way.

## Key terms
- **alignment** — 34 mentions
- **output** — 25 mentions
- **input** — 18 mentions
- **letter** — 15 mentions
- **function** — 14 mentions
- **sequence** — 10 mentions
- **collapsing** — 9 mentions
- **algorithm** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=363|Speech and Language Processing.pdf p. 363]]

## Liens
- Up: [[research/slp/automatic-speech-recognition]]
- ← Prev: [[research/slp/self-supervised-models-hubert]]
- Next: [[research/slp/asr-evaluation-word-error-rate]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

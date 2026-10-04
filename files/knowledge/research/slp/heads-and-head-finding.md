---
title: "Heads and Head-Finding"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING S(dumped) VP(dumped) PP(into) NP(bin) NN(bin) bin DT(a) a P into NP(sacks) NNS(sacks) sacks VBD(dumped) dumped NP(workers) NNS(workers) workers Figure 18.16 "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "434-434"
---

# Heads and Head-Finding

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › Heads and Head-Finding · pp. 434–434 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING S(dumped) VP(dumped) PP(into) NP(bin) NN(bin) bin DT(a) a P into NP(sacks) NNS(sacks) sacks VBD(dumped) dumped NP(workers) NNS(workers) workers Figure 18.16 A lexicalized tree from Collins (1999). As usual, we often report a combination of the two, F1: F1 = 2PR P+R (18.12) We additionally use a new metric, crossing brackets, for each sentence s: cross-brackets: the number of constituents for which the reference parse has a bracketing such as ((A B) C) but the hypothesis parse has a bracketing such as (A (B C)). For comparing parsers that use different grammars, the PARSEVAL metric includes a canonicalization algorithm for removing information likely to be grammarspecific (auxiliaries, pre-infinitival “to”, etc.) and for computing a simplified score (Black et al., 1991). The canonical implementation of the PARSEVAL metrics is called evalb (Sekine and Collins, 1997). evalb Syntactic constituents can be associated with a lexical head; N is the head of an NP, V is the head of a VP. This idea of a head for each constituent dates back to Bloomfield 1914, and is central to the dependency grammars and dependency parsing we’ll introduce in Chapter 19.

## Key terms
- **head** — 16 mentions
- **tree** — 5 mentions
- **parse** — 5 mentions
- **grammar** — 5 mentions
- **dumped** — 4 mentions
- **collins** — 4 mentions
- **constituent** — 4 mentions
- **parsing** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=434|Speech and Language Processing.pdf p. 434]]

## Liens
- Up: [[research/slp/context-free-grammars-and-constituency-parsing]]
- ← Prev: [[research/slp/evaluating-parsers]]
- Next: [[research/slp/summary-17]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "Integrating Span Scores into a Parse"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING passing them through a pretrained language model like BERT. Because BERT operates on the level of subword (wordpiece) tokens rather than words, we’ll first n"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "432-432"
---

# Integrating Span Scores into a Parse

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › Span-Based Neural Constituency Parsing › Integrating Span Scores into a Parse · pp. 432–432 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING passing them through a pretrained language model like BERT. Because BERT operates on the level of subword (wordpiece) tokens rather than words, we’ll first need to convert the BERT outputs to word representations. One standard way of doing this is to simply use the first subword unit as the representation for the entire word; using the last subword unit, or the sum of all the subword units are also common. The embeddings can then be passed through some postprocessing layers; Kitaev et al. (2019), for example, use 8 Transformer layers. The resulting word encoder outputs yt are then used to compute a span score. First, we must map the word encodings (indexed by word positions) to span encodings (indexed by fenceposts). We do this by representing each fencepost with two separate values; the intuition is that a span endpoint to the right of a word represents different information than a span endpoint to the left of a word. We convert each word output yt into a (leftward-pointing) value for spans ending at this fencepost, ←−y t, and a (rightward-pointing) value −→y t for spans beginning at this fencepost, by splitting yt into two halves.

## Key terms
- **span** — 19 mentions
- **word** — 9 mentions
- **score** — 7 mentions
- **fencepost** — 6 mentions
- **output** — 5 mentions
- **through** — 4 mentions
- **subword** — 4 mentions
- **embedding** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=432|Speech and Language Processing.pdf p. 432]]

## Liens
- Up: [[research/slp/span-based-neural-constituency-parsing]]
- ← Prev: [[research/slp/computing-scores-for-a-span]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "Decoding in MT: Beam Search"
summary: "§I Large Language Models › Machine Translation › Decoding in : 12.4 • DECODING IN MT: BEAM SEARCH As in that case, we use teacher forcing in the decoder. Recall that in teacher forcteacher forcing ing, at each time step in decoding we force the system to use the gold target token"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "277-280"
---

# Decoding in MT: Beam Search

§I Large Language Models › Machine Translation › Decoding in MT: Beam Search · pp. 277–280 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
12.4 • DECODING IN MT: BEAM SEARCH As in that case, we use teacher forcing in the decoder. Recall that in teacher forcteacher forcing ing, at each time step in decoding we force the system to use the gold target token from training as the next input xt+1, rather than allowing it to rely on the (possibly erroneous) decoder output ˆyt. Recall the greedy decoding algorithm from Chapter 8: at each time step t in generation, the output yt is chosen by computing the probability for each word in the vocabulary and then choosing the highest probability word (the argmax): ˆwt = argmaxw∈V P(w|w<t) (12.14) A problem with greedy decoding is that what looks high probability at word t might turn out to have been the wrong choice once we get to word t +1. The beam search algorithm maintains multiple choices until later when we can see which one is best. In beam search we model decoding as searching the space of possible generations, represented as a search tree whose branches represent actions (generating a search tree token), and nodes represent states (having generated a particular prefix). We search for the best action sequence, i.e., the string with the highest probability. An illustration of the problem Fig.

## Key terms
- **frontier** — 28 mentions
- **beam** — 27 mentions
- **search** — 26 mentions
- **probability** — 20 mentions
- **state** — 19 mentions
- **arrived** — 17 mentions
- **witch** — 17 mentions
- **decoding** — 14 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=277|Speech and Language Processing.pdf p. 277]]

## Liens
- Up: [[research/slp/machine-translation]]
- ← Prev: [[research/slp/details-of-the-encoder-decoder-model]]
- Next: [[research/slp/translating-in-low-resource-situations]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "HMM tagging as decoding"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES The A transition probabilities, and B observation likelihoods of the HMM are illustrated in Fig."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "400-400"
---

# HMM tagging as decoding

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › HMM Part-of-Speech Tagging › HMM tagging as decoding · pp. 400–400 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES The A transition probabilities, and B observation likelihoods of the HMM are illustrated in Fig. 17.9 for three states in an HMM part-of-speech tagger; the full tagger would have one state for each tag. For any model, such as an HMM, that contains hidden variables, the task of determining the hidden variables sequence corresponding to the sequence of observations is called decoding. More formally, decoding Decoding: Given as input an HMM λ = (A,B) and a sequence of observations O = o1,o2,...,oT, find the most probable sequence of states Q = q1q2q3 ...qT. For part-of-speech tagging, the goal of HMM decoding is to choose the tag sequence t1 ...tn that is most probable given the observation sequence of n words w1 ...wn: ˆt1:n = argmax t1... tn P(t1 ...tn|w1 ...wn) (17.12) The way we’ll do this in the HMM is to use Bayes’ rule to instead compute: ˆt1:n = argmax t1... tn P(w1 ...wn|t1 ...tn)P(t1 ...tn) P(w1 ...wn) (17.13) Furthermore, we simplify Eq. 17.13 by dropping the denominator P(wn 1): ˆt1:n = argmax t1... tn P(w1 ...wn|t1 ...tn)P(t1 ...tn) (17.14) HMM taggers make two further simplifying assumptions. The first (output independence, from Eq.

## Key terms
- **sequence** — 9 mentions
- **argmax** — 5 mentions
- **observation** — 4 mentions
- **tagger** — 4 mentions
- **decoding** — 4 mentions
- **probability** — 4 mentions
- **assumption** — 4 mentions
- **transition** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=400|Speech and Language Processing.pdf p. 400]]

## Liens
- Up: [[research/slp/hmm-part-of-speech-tagging]]
- ← Prev: [[research/slp/the-components-of-an-hmm-tagger]]
- Next: [[research/slp/the-viterbi-algorithm]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "CTC Training"
summary: "§I Large Language Models › Automatic Speech Recognition › CTC: CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION and sums those as an approximation of (Eq. See Hannun (2017) for a clear explanation of this extension of beam search for CTC."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "366-366"
---

# CTC Training

§I Large Language Models › Automatic Speech Recognition › CTC › CTC Training · pp. 366–366 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION and sums those as an approximation of (Eq. 15.18). See Hannun (2017) for a clear explanation of this extension of beam search for CTC. Because of the strong conditional independence assumption mentioned earlier (that the output at time t is independent of the output at time t −1, given the input), CTC does not implicitly learn a language model over the data (unlike the attentionbased encoder-decoder architectures). It is therefore essential when using CTC to interpolate a language model (and some sort of length factor L(Y)) using interpolation weights that are trained on a devset: scoreCTC(Y|X) = logPCTC(Y|X)+λ1 logPLM(Y)λ2L(Y) (15.19) To train a CTC-based ASR system, we use negative log-likelihood loss with a special CTC loss function. Thus the loss for an entire dataset D is the sum of the negative log-likelihoods of the correct output Y for each input X: LCTC = X (X,Y)∈D −logPCTC(Y|X) (15.20) To compute CTC loss function for a single input pair (X,Y), we need the probability of the outputY given the input X. As we saw in Eq. 15.18, to compute the probability of a given output Y we need to sum over all the possible alignments that would collapse to Y.

## Key terms
- **loss** — 7 mentions
- **output** — 4 mentions
- **input** — 4 mentions
- **logpctc** — 4 mentions
- **alignments** — 4 mentions
- **language** — 3 mentions
- **model** — 3 mentions
- **function** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=366|Speech and Language Processing.pdf p. 366]]

## Liens
- Up: [[research/slp/ctc]]
- ← Prev: [[research/slp/ctc-inference]]
- Next: [[research/slp/combining-ctc-and-encoder-decoder]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

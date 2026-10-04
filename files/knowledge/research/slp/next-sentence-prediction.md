---
title: "Next Sentence Prediction"
summary: "§I Large Language Models › Masked Language Models › Training : CHAPTER 9 • MASKED LANGUAGE MODELS probabilities y over the vocabulary: ui = hL i ET (9.3) yi = softmax(ui) (9.4) With a predicted probability distribution for each masked item, we can use crossentropy to compute the "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "212-212"
---

# Next Sentence Prediction

§I Large Language Models › Masked Language Models › Training Bidirectional Encoders › Next Sentence Prediction · pp. 212–212 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 9 • MASKED LANGUAGE MODELS probabilities y over the vocabulary: ui = hL i ET (9.3) yi = softmax(ui) (9.4) With a predicted probability distribution for each masked item, we can use crossentropy to compute the loss for each masked item-the negative log probability assigned to the actual masked word, as shown in Fig. 9.3. More formally, for a given vector of input tokens in a sentence or batch x, let the set of tokens that are masked be M, the version of that sentence with some tokens replaced by masks be xmask, and the sequence of output vectors be h. For a given input token xi, such as the word long in Fig. 9.3, the loss is the probability of the correct word long, given xmask (as summarized in the single output vector hL i ): LMLM(xi) = −logP(xi|hL i ) The gradients that form the basis for the weight updates are based on the average loss over the sampled learning items from a single training sequence (or batch of sequences). LMLM = −1 |M| X i∈M logP(xi|hL i ) Note that only the tokens in M play a role in learning; the other words play no role in the loss function, so in that sense BERT and its descendents are inefficient; only 15% of the input samples in the training data are actually used for training weights.1 The focus of mask-based learning is on predicting words from surrounding contexts with the goal of producing effective word-level representations.

## Key terms
- **sentence** — 15 mentions
- **token** — 15 mentions
- **pair** — 11 mentions
- **input** — 8 mentions
- **training** — 7 mentions
- **word** — 6 mentions
- **masked** — 5 mentions
- **loss** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=212|Speech and Language Processing.pdf p. 212]]

## Liens
- Up: [[research/slp/training-bidirectional-encoders]]
- ← Prev: [[research/slp/masking-words]]
- Next: [[research/slp/training-regimes]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

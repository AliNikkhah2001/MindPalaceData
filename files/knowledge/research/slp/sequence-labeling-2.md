---
title: "Sequence Labeling"
summary: "§I Large Language Models › RNNs and LSTMs › RNNs for other NL: 13.3 • RNNS FOR OTHER NLP TASKS second set of learned word embeddings. Instead of having two sets of embedding matrices, language models use a single embedding matrix, which appears at both the input and softmax layer"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "299-299"
---

# Sequence Labeling

§I Large Language Models › RNNs and LSTMs › RNNs for other NLP tasks › Sequence Labeling · pp. 299–299 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
13.3 • RNNS FOR OTHER NLP TASKS second set of learned word embeddings. Instead of having two sets of embedding matrices, language models use a single embedding matrix, which appears at both the input and softmax layers. That is, we dispense with V and use E at the start of the computation and E⊺(because the shape of V is the transpose of E at the end. Using the same matrix (transposed) in two places is called weight tying.1 The weight-tied equations for an RNN language weight tying model then become: et = Ext (13.12) ht = g(Uht−1 +Wet) (13.13) ˆyt = softmax(E⊺ht) (13.14) In addition to providing improved model perplexity, this approach significantly reduces the number of parameters required for the model. Now that we’ve seen the basic RNN architecture, let’s consider how to apply it to three types of NLP tasks: sequence classification tasks like sentiment analysis and topic classification, sequence labeling tasks like part-of-speech tagging, and text generation tasks, including with a new architecture called the encoder-decoder. In sequence labeling, the network’s task is to assign a label chosen from a small fixed set of labels to each element of a sequence. One classic sequence labeling tasks is part-of-speech (POS) tagging (assigning grammatical tags like NOUN and VERB to each word in a sentence).

## Key terms
- **sequence** — 9 mentions
- **task** — 9 mentions
- **input** — 7 mentions
- **layer** — 7 mentions
- **softmax** — 6 mentions
- **embedding** — 5 mentions
- **step** — 5 mentions
- **word** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=299|Speech and Language Processing.pdf p. 299]]

## Liens
- Up: [[research/slp/rnns-for-other-nlp-tasks]]
- Next: [[research/slp/rnns-for-sequence-classification]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

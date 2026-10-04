---
title: "Weight Tying"
summary: "§I Large Language Models › RNNs and LSTMs › RNNs as Language : CHAPTER 13 • RNNS AND LSTMS Input Embeddings Softmax over Vocabulary So long and thanks for long and thanks for Next word all … Loss … … RNN h y Vh −log ˆylong −log ˆyand −log ˆythanks −log ˆyfor −log ˆyall e Figure 1"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "298-298"
---

# Weight Tying

§I Large Language Models › RNNs and LSTMs › RNNs as Language Models › Weight Tying · pp. 298–298 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 13 • RNNS AND LSTMS Input Embeddings Softmax over Vocabulary So long and thanks for long and thanks for Next word all … Loss … … RNN h y Vh −log ˆylong −log ˆyand −log ˆythanks −log ˆyfor −log ˆyall e Figure 13.6 Training RNNs as language models. In the case of language modeling, the correct distribution yt comes from knowing the next word. This is represented as a one-hot vector corresponding to the vocabulary where the entry for the actual next word is 1, and all the other entries are 0. Thus, the cross-entropy loss for language modeling is determined by the probability the model assigns to the correct next word. So at time t the CE loss is the negative log probability the model assigns to the next word in the training sequence. LCE( ˆyt,yt) = −log ˆyt[wt+1] (13.11) Thus at each word position t of the input, the model takes as input the correct word wt together with ht−1, encoding information from the preceding w1:t−1, and uses them to compute a probability distribution over possible next words so as to compute the model’s loss for the next token wt+1. Then we move to the next word, we ignore what the model predicted for the next word and instead use the correct word wt+1 along with the prior history encoded to estimate the probability of token wt+2.

## Key terms
- **word** — 16 mentions
- **next** — 10 mentions
- **model** — 9 mentions
- **embedding** — 6 mentions
- **loss** — 5 mentions
- **training** — 5 mentions
- **correct** — 5 mentions
- **input** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=298|Speech and Language Processing.pdf p. 298]]

## Liens
- Up: [[research/slp/rnns-as-language-models]]
- ← Prev: [[research/slp/training-an-rnn-language-model]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

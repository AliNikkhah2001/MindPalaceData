---
title: "Pretraining corpora for large language models"
summary: "§I Large Language Models › Large Language Models › Training L: 7.5 • TRAINING LARGE LANGUAGE MODELS possible next tokens so as to compute the model’s loss for the next token wt+1. Then we move to the next word, we ignore what the model predicted for the next word and instead use "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "169-170"
---

# Pretraining corpora for large language models

§I Large Language Models › Large Language Models › Training Large Language Models › Pretraining corpora for large language models · pp. 169–170 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
7.5 • TRAINING LARGE LANGUAGE MODELS possible next tokens so as to compute the model’s loss for the next token wt+1. Then we move to the next word, we ignore what the model predicted for the next word and instead use the correct sequence of tokens w1:t+1 to get the model to estimate the probability of token wt+2. This idea that we always give the model the correct history sequence to predict the next word (rather than feeding the model its best guess from the previous time step) is called teacher forcing. teacher forcing Fig. 7.13 illustrates the general training approach. At each step, given all the preceding tokens, the language model produces an output distribution over the entire vocabulary. During training, the probability assigned to the correct word is used to calculate the cross-entropy loss for each item in the sequence. The loss for each batch is the average cross-entropy loss over the entire sequence of negative log probabilities, or more formally: LCE(batch of length T) = T T X t=1 −log ˆyt[wt+1] (7.7) The weights in the network are then adjusted to minimize this average cross-entropy loss over the batch via gradient descent (Fig. 4.5), using error backpropagation on the computation graph to compute the gradient.

## Key terms
- **model** — 17 mentions
- **token** — 13 mentions
- **next** — 9 mentions
- **training** — 8 mentions
- **language** — 8 mentions
- **word** — 8 mentions
- **text** — 8 mentions
- **large** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=169|Speech and Language Processing.pdf p. 169]]

## Liens
- Up: [[research/slp/training-large-language-models]]
- ← Prev: [[research/slp/self-supervised-training-algorithm-for-pretraining]]
- Next: [[research/slp/finetuning]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

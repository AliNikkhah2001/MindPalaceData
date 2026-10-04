---
title: "Forward Inference in an RNN language model"
summary: "§I Large Language Models › RNNs and LSTMs › RNNs as Language : CHAPTER 13 • RNNS AND LSTMS Let’s see how to apply RNNs to the language modeling task. Recall from Chapter 3 that language models predict the next word in a sequence given some preceding context."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "296-296"
---

# Forward Inference in an RNN language model

§I Large Language Models › RNNs and LSTMs › RNNs as Language Models › Forward Inference in an RNN language model · pp. 296–296 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 13 • RNNS AND LSTMS Let’s see how to apply RNNs to the language modeling task. Recall from Chapter 3 that language models predict the next word in a sequence given some preceding context. For example, if the preceding context is “Thanks for all the” and we want to know how likely the next word is “fish” we would compute: P(fish|Thanks for all the) Language models give us the ability to assign such a conditional probability to every possible next word, giving us a distribution over the entire vocabulary. We can also assign probabilities to entire sequences by combining these conditional probabilities with the chain rule: P(w1:n) = n Y i=1 P(wi|w<i) The n-gram language models of Chapter 3 compute the probability of a word given counts of its occurrence with the n−1 prior words. The context is thus of size n−1. For the feedforward language models of Chapter 6, the context is the window size. RNN language models (Mikolov et al., 2010) process the input sequence one word at a time, attempting to predict the next word from the current word and the previous hidden state. RNNs thus don’t have the limited context problem that n-gram models have, or the fixed context that feedforward language models have, since the hidden state can in principle represent information about all of the preceding words all the way back to the beginning of the sequence.

## Key terms
- **language** — 13 mentions
- **model** — 13 mentions
- **context** — 10 mentions
- **word** — 9 mentions
- **sequence** — 5 mentions
- **next** — 4 mentions
- **hidden** — 4 mentions
- **state** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=296|Speech and Language Processing.pdf p. 296]]

## Liens
- Up: [[research/slp/rnns-as-language-models]]
- Next: [[research/slp/training-an-rnn-language-model]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

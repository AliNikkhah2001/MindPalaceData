---
title: "Generation with RNN-Based Language Models"
summary: "§I Large Language Models › RNNs and LSTMs › RNNs for other NL: 13.3 • RNNS FOR OTHER NLP TASKS drives the training. The error signal from the classification is backpropagated all the way through the weights in the feedforward classifier through, to its input, and then through to "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "301-301"
---

# Generation with RNN-Based Language Models

§I Large Language Models › RNNs and LSTMs › RNNs for other NLP tasks › Generation with RNN-Based Language Models · pp. 301–301 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
13.3 • RNNS FOR OTHER NLP TASKS drives the training. The error signal from the classification is backpropagated all the way through the weights in the feedforward classifier through, to its input, and then through to the three sets of weights in the RNN as described earlier in Section 13.1.2. The training regimen that uses the loss from a downstream application to adjust the weights all the way through the network is referred to as end-to-end training. end-to-end Another option, instead of using just the hidden state of the last token hn to represent the whole sequence, is to use some sort of pooling function of all the pooling hidden states hi for each word i in the sequence. For example, we can create a representation that pools all the n hidden states by taking their element-wise mean: hmean = 1 n n X i=1 hi (13.15) Or we can take the element-wise max; the element-wise max of a set of n vectors is a new vector whose kth element is the max of the kth elements of all the n vectors. The long contexts of RNNs makes it quite difficult to successfully backpropagate error all the way through the entire input; we’ll talk about this problem, and some standard solutions, in Section 13.5. RNN-based language models can also be used to generate text, Text generation, along with image generation and code generation, constitute a new area of AI that is often called generative AI.

## Key terms
- **word** — 11 mentions
- **generation** — 8 mentions
- **model** — 6 mentions
- **through** — 5 mentions
- **hidden** — 5 mentions
- **sequence** — 5 mentions
- **time** — 5 mentions
- **input** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=301|Speech and Language Processing.pdf p. 301]]

## Liens
- Up: [[research/slp/rnns-for-other-nlp-tasks]]
- ← Prev: [[research/slp/rnns-for-sequence-classification]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

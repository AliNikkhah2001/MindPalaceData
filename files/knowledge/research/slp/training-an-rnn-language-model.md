---
title: "Training an RNN language model"
summary: "§I Large Language Models › RNNs and LSTMs › RNNs as Language : 13.2 • RNNS AS LANGUAGE MODELS words each represented as a one-hot vector of size |V| × 1, and the output prediction, ˆy, is a vector representing a probability distribution over the vocabulary."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "297-297"
---

# Training an RNN language model

§I Large Language Models › RNNs and LSTMs › RNNs as Language Models › Training an RNN language model · pp. 297–297 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
13.2 • RNNS AS LANGUAGE MODELS words each represented as a one-hot vector of size |V| × 1, and the output prediction, ˆy, is a vector representing a probability distribution over the vocabulary. At each step, the model uses the word embedding matrix E to retrieve the embedding for the current word, multiples it by the weight matrix W, and then adds it to the hidden layer from the previous step (weighted by weight matrix U) to compute a new hidden layer. This hidden layer is then used to generate an output layer which is passed through a softmax layer to generate a probability distribution over the entire vocabulary. That is, at time t: et = Ext (13.4) ht = g(Uht−1 +Wet) (13.5) ˆyt = softmax(Vht) (13.6) When we do language modeling with RNNs (and we’ll see this again in Chapter 8 with transformers), it’s convenient to make the assumption that the embedding dimension de and the hidden dimension dh are the same. So we’ll just call both of these the model dimension d. So the embedding matrix E is of shape [d ×|V|], and xt is a one-hot vector of shape [|V|×1]. The product et is thus of shape [d ×1]. W and U are of shape [d × d], so ht is also of shape [d × 1]. V is of shape [|V| × d], so the result of Vh is a vector of shape [|V| × 1].

## Key terms
- **word** — 9 mentions
- **probability** — 7 mentions
- **model** — 7 mentions
- **shape** — 7 mentions
- **vector** — 5 mentions
- **distribution** — 5 mentions
- **layer** — 5 mentions
- **vocabulary** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=297|Speech and Language Processing.pdf p. 297]]

## Liens
- Up: [[research/slp/rnns-as-language-models]]
- ← Prev: [[research/slp/forward-inference-in-an-rnn-language-model]]
- Next: [[research/slp/weight-tying]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

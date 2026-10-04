---
title: "Training"
summary: "§I Large Language Models › RNNs and LSTMs › Recurrent Neural : CHAPTER 13 • RNNS AND LSTMS the hidden layer from the previous time step ht−1 with the weight matrix U. We add these values together and pass them through a suitable activation function, g, to arrive at the activation"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "294-294"
---

# Training

§I Large Language Models › RNNs and LSTMs › Recurrent Neural Networks › Training · pp. 294–294 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 13 • RNNS AND LSTMS the hidden layer from the previous time step ht−1 with the weight matrix U. We add these values together and pass them through a suitable activation function, g, to arrive at the activation value for the current hidden layer, ht. Once we have the values for the hidden layer, we proceed with the usual computation to generate the output vector. ht = g(Uht−1 +Wxt) (13.1) yt = f(Vht) (13.2) Let’s refer to the input, hidden and output layer dimensions as din, dh, and dout respectively. Given this, our three parameter matrices are: W ∈Rdh×din, U ∈Rdh×dh, and V ∈Rdout×dh. We compute yt via a softmax computation that gives a probability distribution over the possible output classes. yt = softmax(Vht) (13.3) The fact that the computation at time t requires the value of the hidden layer from time t −1 mandates an incremental inference algorithm that proceeds from the start of the sequence to the end as illustrated in Fig. 13.3. The sequential nature of simple recurrent networks can also be seen by unrolling the network in time as is shown in Fig. 13.4. In this figure, the various layers of units are copied for each time step to illustrate that they will have differing values over time.

## Key terms
- **layer** — 15 mentions
- **time** — 14 mentions
- **hidden** — 12 mentions
- **output** — 9 mentions
- **weight** — 7 mentions
- **network** — 7 mentions
- **value** — 6 mentions
- **function** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=294|Speech and Language Processing.pdf p. 294]]

## Liens
- Up: [[research/slp/recurrent-neural-networks]]
- ← Prev: [[research/slp/inference-in-rnns]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

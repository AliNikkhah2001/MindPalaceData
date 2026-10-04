---
title: "Greedy decoding"
summary: "§I Large Language Models › Large Language Models › Generation: 7.4 • GENERATION AND SAMPLING The generation depends on the probability of each token, so let’s remind ourselves where this probability distribution comes from."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "163-163"
---

# Greedy decoding

§I Large Language Models › Large Language Models › Generation and Sampling › Greedy decoding · pp. 163–163 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
7.4 • GENERATION AND SAMPLING The generation depends on the probability of each token, so let’s remind ourselves where this probability distribution comes from. The internal networks for language models (whether transformers or alternatives like LSTMs or state space models) generate scores called logits (real valued numbers) for each token in the vocabulary. This score vector u is then normalized by softmax to be a legal probability distribution, just as we saw for logistic regression in Chapter 4. So if we have a logit vector u of shape [1 × |V|] that gives a score for each possible next token, we can pass it through a softmax to get a vector y, also of shape [1 × |V|], which assigns a probability to each token in the vocabulary, as shown in the following equation: y = softmax(u) (7.1) Fig. 7.7 shows an example in which the softmax is computed for pedagogical purposes on a simplified vocabulary of only 4 words. 1.2 0.9 all the your that -0.5 logits .44 .33 all the your that .15 .08 probabilities softmax Transformer (or other decoder) long and thanks for So ? 0.1 u y Figure 7.7 Taking the logit vector u and using the softmax to create a probability vector y. Now given this probability distribution over tokens, we need to select one token to generate.

## Key terms
- **token** — 16 mentions
- **probability** — 8 mentions
- **model** — 8 mentions
- **generation** — 6 mentions
- **generate** — 6 mentions
- **softmax** — 6 mentions
- **decoding** — 6 mentions
- **language** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=163|Speech and Language Processing.pdf p. 163]]

## Liens
- Up: [[research/slp/generation-and-sampling]]
- Next: [[research/slp/random-sampling]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "Self-supervised training algorithm for pretraining"
summary: "§I Large Language Models › Large Language Models › Training L: 7.5 • TRAINING LARGE LANGUAGE MODELS 1.2 0.9 0.1 -0.5 logits .44 .33 .15 .08 𝜏=1 all the your that normal softmax .59 .32 .07 .02 𝜏=0.5 .95 .05 𝜏=0.1 .27 .26 .24 .23 𝜏=10 .25 .25 .25 .25 𝜏=100 close to greedy softmax "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "167-168"
---

# Self-supervised training algorithm for pretraining

§I Large Language Models › Large Language Models › Training Large Language Models › Self-supervised training algorithm for pretraining · pp. 167–168 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
7.5 • TRAINING LARGE LANGUAGE MODELS 1.2 0.9 0.1 -0.5 logits .44 .33 .15 .08 𝜏=1 all the your that normal softmax .59 .32 .07 .02 𝜏=0.5 .95 .05 𝜏=0.1 .27 .26 .24 .23 𝜏=10 .25 .25 .25 .25 𝜏=100 close to greedy softmax output with temperature 𝜏 close to uniform low temperature sampling (towards greedy) high temperature sampling (towards uniform) Figure 7.11 Seeing how different values of τ change the resulting probabilities from the initial logits in temperature sampling. In this simplified example, there are only 4 tokens in the vocabulary. 1. pretraining: In this first stage, the model is trained to incrementally predict the next word in enormous text corpora. The model uses the cross-entropy loss, sometimes called the language modeling loss, and that loss is backpropagated all the way through the network. The training data is usually based on cleaning up parts of the web. The result is a model that is very good at predicting words and can generate text. 2. instruction tuning, also called supervised finetuning or SFT: In the second stage, the model is trained, again by cross-entropy loss to follow instructions, for example to answer questions, give summaries, write code, translate sentences, and so on.

## Key terms
- **model** — 19 mentions
- **word** — 12 mentions
- **loss** — 12 mentions
- **language** — 11 mentions
- **next** — 11 mentions
- **instruction** — 9 mentions
- **training** — 7 mentions
- **correct** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=167|Speech and Language Processing.pdf p. 167]]

## Liens
- Up: [[research/slp/training-large-language-models]]
- Next: [[research/slp/pretraining-corpora-for-large-language-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

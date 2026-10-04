---
title: "Historical Notes"
summary: "§I Large Language Models › Neural Networks › Historical Notes: CHAPTER 6 • NEURAL NETWORKS For logistic regression we can initialize gradient descent with all the weights and biases having the value 0."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "152-153"
---

# Historical Notes

§I Large Language Models › Neural Networks › Historical Notes · pp. 152–153 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 6 • NEURAL NETWORKS For logistic regression we can initialize gradient descent with all the weights and biases having the value 0. In neural networks, by contrast, we need to initialize the weights with small random numbers. It’s also helpful to normalize the input values to have 0 mean and unit variance. Various forms of regularization are used to prevent overfitting. One of the most important is dropout: randomly dropping some units and their connections from dropout the network during training (Hinton et al. 2012, Srivastava et al. 2014). At each iteration of training (whenever we update parameters, i.e. each mini-batch if we are using mini-batch gradient descent), we repeatedly choose a probability p and for each unit we replace its output with zero with probability p (and renormalize the rest of the outputs from that layer). Tuning of hyperparameters is also important. The parameters of a neural nethyperparameter work are the weights W and biases b; those are learned by gradient descent. The hyperparameters are things that are chosen by the algorithm designer; optimal values are tuned on a devset rather than by gradient descent learning on the training set. Hyperparameters include the learning rate η, the mini-batch size, the model architecture (the number of layers, the number of hidden nodes per layer, the choice of activation functions), how to regularize, and so on.

## Key terms
- **network** — 22 mentions
- **neural** — 20 mentions
- **unit** — 10 mentions
- **gradient** — 8 mentions
- **layer** — 7 mentions
- **descent** — 6 mentions
- **model** — 6 mentions
- **number** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=152|Speech and Language Processing.pdf p. 152]]

## Liens
- Up: [[research/slp/neural-networks]]
- ← Prev: [[research/slp/summary-5]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

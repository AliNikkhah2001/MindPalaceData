---
title: "Embeddings as the input to neural net classifiers"
summary: "§I Large Language Models › Neural Networks › Embeddings as th: 6.19 shows how to classify a single example x, in practice we want to efficiently classify an entire test set of m examples."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "140-144"
---

# Embeddings as the input to neural net classifiers

§I Large Language Models › Neural Networks › Embeddings as the input to neural net classifiers · pp. 140–144 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 6 • NEURAL NETWORKS While Eq. 6.19 shows how to classify a single example x, in practice we want to efficiently classify an entire test set of m examples. We do this by vectorizing the process, just as we saw with logistic regression; instead of using for-loops to go through each example, we’ll use matrix multiplication to do the entire computation of an entire test set at once. First, we pack all the input feature vectors for each input x into a single input matrix X, with each row i a row vector consisting of the features for input example x(i) (i.e., the vector x(i)). If the dimensionality of our input feature vector is d, X will be a matrix of shape [m×d]. Because we are now modeling each input as a row vector rather than a column vector, we also need to slightly modify Eq. 6.19. X is of shape [m×d] and W is of shape [dh ×d], so we’ll reorder how we multiply X and W and transpose W so they correctly multiply to yield a matrix H of shape [m×dh]. 1 The bias vector b from Eq. 6.19 of shape [1×dh] will now have to be replicated into a matrix of shape [m × dh]. We’ll need to similarly reorder the next step and transpose U. Finally, our output matrix ˆY will be of shape [m × 3] (or more generally [m × do], where do is the number of output classes), with each row i of our output matrix ˆY consisting of the output vector ˆy(i).

## Key terms
- **embedding** — 53 mentions
- **input** — 37 mentions
- **vector** — 31 mentions
- **word** — 29 mentions
- **matrix** — 20 mentions
- **token** — 20 mentions
- **neural** — 17 mentions
- **language** — 17 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=140|Speech and Language Processing.pdf p. 140]]

## Liens
- Up: [[research/slp/neural-networks]]
- ← Prev: [[research/slp/feedforward-networks-for-nlp-classification]]
- Next: [[research/slp/training-neural-nets]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

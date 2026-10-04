---
title: "The solution: neural networks"
summary: "§I Large Language Models › Neural Networks › The XOR problem : CHAPTER 6 • NEURAL NETWORKS It’s very easy to build a perceptron that can compute the logical AND and OR functions of its binary inputs; Fig."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "132-132"
---

# The solution: neural networks

§I Large Language Models › Neural Networks › The XOR problem › The solution: neural networks · pp. 132–132 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 6 • NEURAL NETWORKS It’s very easy to build a perceptron that can compute the logical AND and OR functions of its binary inputs; Fig. 6.4 shows the necessary weights. x1 x2 +1 -1 x1 x2 +1 (a) (b) Figure 6.4 The weights w and bias b for perceptrons for computing logical functions. The inputs are shown as x1 and x2 and the bias as a special node with value +1 which is multiplied with the bias weight b. (a) logical AND, with weights w1 = 1 and w2 = 1 and bias weight b = −1. (b) logical OR, with weights w1 = 1 and w2 = 1 and bias weight b = 0. These weights/biases are just one from an infinite number of possible sets of weights and biases that would implement the functions. It turns out, however, that it’s not possible to build a perceptron to compute logical XOR! (It’s worth spending a moment to give it a try!) The intuition behind this important result relies on understanding that a perceptron is a linear classifier. For a two-dimensional input x1 and x2, the perceptron equation, w1x1 +w2x2 +b = 0 is the equation of a line. (We can see this by putting it in the standard linear format: x2 = (−w1/w2)x1 + (−b/w2).) This line acts as a decision boundary in two-dimensional space in which the output 0 is assigned to all decision boundary inputs lying on one side of the line, and the output 1 to all input points lying on the other side of the line.

## Key terms
- **weight** — 12 mentions
- **input** — 12 mentions
- **perceptron** — 8 mentions
- **line** — 8 mentions
- **bias** — 7 mentions
- **function** — 7 mentions
- **logical** — 6 mentions
- **possible** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=132|Speech and Language Processing.pdf p. 132]]

## Liens
- Up: [[research/slp/the-xor-problem]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

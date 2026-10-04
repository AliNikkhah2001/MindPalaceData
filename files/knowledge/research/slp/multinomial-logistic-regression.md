---
title: "Multinomial logistic regression"
summary: "§I Large Language Models › Logistic Regression › Multinomial : CHAPTER 4 • LOGISTIC REGRESSION respectively. We make the assumption that the training examples are independent: log p(training labels) = log m Y i=1 p(y(i)|x(i)) = m X i=1 log p(y(i)|x(i)) = − m X i=1 LCE(ˆy(i),y(i))"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "86-88"
---

# Multinomial logistic regression

§I Large Language Models › Logistic Regression › Multinomial logistic regression · pp. 86–88 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION respectively. We make the assumption that the training examples are independent: log p(training labels) = log m Y i=1 p(y(i)|x(i)) = m X i=1 log p(y(i)|x(i)) = − m X i=1 LCE(ˆy(i),y(i)) (4.29) Now the cost function for the mini-batch of m examples is the average loss for each example: Cost(ˆy,y) = m m X i=1 LCE(ˆy(i),y(i)) = −1 m m X i=1 y(i) logσ(w ·x(i) +b)+(1−y(i))log  1−σ(w ·x(i) +b)  (4.30) The mini-batch gradient is the average of the individual gradients from Eq. 4.26: ∂Cost(ˆy,y) ∂w j = m m X i=1 h σ(w ·x(i) +b)−y(i)i x(i) j (4.31) Instead of using the sum notation, we can more efficiently compute the gradient in its matrix form, following the vectorization we saw on page 70, where we have a matrix X of size [m × f] representing the m inputs in the batch, and a vector y of size [m×1] representing the correct outputs: ∂Cost(ˆy,y) ∂w = m (ˆy −y)⊺X = m (σ(Xw +b)−y)⊺X (4.32) Sometimes we need more than two classes. Perhaps we might want to do 3-way sentiment classification (positive, negative, or neutral). Or we could be assigning some of the labels we will introduce in Chapter 17, like the part of speech of a word (choosing from 10, 30, or even 50 different parts of speech), or the named entity type of a phrase (choosing from tags like person, location, organization).

## Key terms
- **vector** — 25 mentions
- **weight** — 18 mentions
- **softmax** — 14 mentions
- **class** — 14 mentions
- **logistic** — 13 mentions
- **regression** — 12 mentions
- **classes** — 12 mentions
- **feature** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=86|Speech and Language Processing.pdf p. 86]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/gradient-descent]]
- Next: [[research/slp/learning-in-multinomial-logistic-regression]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

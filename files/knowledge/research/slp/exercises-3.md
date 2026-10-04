---
title: "Exercises"
summary: "§I Large Language Models › Logistic Regression › Exercises: CHAPTER 4 • LOGISTIC REGRESSION ∂LCE ∂w j = ∂ ∂w j −[ylogσ(w ·x+b)+(1−y)log(1−σ(w ·x+b))] = −  ∂ ∂wj ylogσ(w ·x+b)+ ∂ ∂w j (1−y)log[1−σ(w ·x+b)]  (4.60) Next, using the chain rule, and relying on the derivative of log:"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "102-103"
---

# Exercises

§I Large Language Models › Logistic Regression › Exercises · pp. 102–103 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION ∂LCE ∂w j = ∂ ∂w j −[ylogσ(w ·x+b)+(1−y)log(1−σ(w ·x+b))] = −  ∂ ∂wj ylogσ(w ·x+b)+ ∂ ∂w j (1−y)log[1−σ(w ·x+b)]  (4.60) Next, using the chain rule, and relying on the derivative of log: ∂LCE ∂wj = − y σ(w ·x+b) ∂ ∂w j σ(w ·x+b)− 1−y 1−σ(w ·x+b) ∂ ∂w j [1−σ(w ·x+b)] (4.61) Rearranging terms: ∂LCE ∂w j = −  y σ(w ·x+b) − 1−y 1−σ(w ·x+b)  ∂ ∂wj σ(w ·x+b) And now plugging in the derivative of the sigmoid, and using the chain rule one more time, we end up with Eq. 4.62: ∂LCE ∂wj = −  y−σ(w ·x+b) σ(w ·x+b)[1−σ(w ·x+b)]  σ(w ·x+b)[1−σ(w ·x+b)]∂(w ·x+b) ∂w j = −  y−σ(w ·x+b) σ(w ·x+b)[1−σ(w ·x+b)]  σ(w ·x+b)[1−σ(w ·x+b)]xj = −[y−σ(w ·x+b)]xj = [σ(w ·x+b)−y]x j (4.62) This chapter introduced the logistic regression model of classification. • Logistic regression is a supervised machine learning classifier that extracts real-valued features from the input, multiplies each by a weight, sums them, and passes the sum through a sigmoid function to generate a probability. A threshold is used to make a decision. • Logistic regression can be used with two classes (e.g., positive and negative sentiment) or with multiple classes (multinomial logistic regression, for example for n-ary text classification, part-of-speech labeling, etc.).

## Key terms
- **regression** — 12 mentions
- **logistic** — 11 mentions
- **classification** — 8 mentions
- **feature** — 7 mentions
- **text** — 5 mentions
- **information** — 5 mentions
- **function** — 4 mentions
- **weight** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=102|Speech and Language Processing.pdf p. 102]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/historical-notes-3]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

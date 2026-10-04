---
title: "The sigmoid function"
summary: "§I Large Language Models › Logistic Regression › The sigmoid : 4.2 • THE SIGMOID FUNCTION The goal of binary logistic regression is to train a classifier that can make a binary decision about the class of a new input observation."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "73-74"
---

# The sigmoid function

§I Large Language Models › Logistic Regression › The sigmoid function · pp. 73–74 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.2 • THE SIGMOID FUNCTION The goal of binary logistic regression is to train a classifier that can make a binary decision about the class of a new input observation. Here we introduce the sigmoid classifier that will help us make this decision. Consider a single input observation x, which we will represent by a vector of features [x1,x2,...,xn]. (We’ll show sample features in the next subsection.) The classifier output y can be 1 (meaning the observation is a member of the class) or 0 (the observation is not a member of the class). We want to know the probability P(y = 1|x) that this observation is a member of the class. So perhaps the decision is “positive sentiment” versus “negative sentiment”, the features represent counts of words in a document, P(y = 1|x) is the probability that the document has positive sentiment, and P(y = 0|x) is the probability that the document has negative sentiment. Logistic regression solves this task by learning, from a training set, a vector of weights and a bias term. Each weight wi is a real number, and is associated with one of the input features xi. The weight wi represents how important that input feature is to the classification decision, and can be positive (providing evidence that the instance being classified belongs in the positive class) or negative (providing evidence that the instance being classified belongs in the negative class).

## Key terms
- **sigmoid** — 14 mentions
- **function** — 11 mentions
- **probability** — 11 mentions
- **class** — 8 mentions
- **weight** — 8 mentions
- **logistic** — 7 mentions
- **input** — 7 mentions
- **number** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=73|Speech and Language Processing.pdf p. 73]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/machine-learning-and-classification]]
- Next: [[research/slp/classification-with-logistic-regression]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

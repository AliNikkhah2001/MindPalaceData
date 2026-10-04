---
title: "Classification with Logistic Regression"
summary: "§I Large Language Models › Logistic Regression › Classificati: 4.3 • CLASSIFICATION WITH LOGISTIC REGRESSION The sigmoid function from the prior section thus gives us a way to take an instance x and compute the probability P(y = 1|x)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "75-77"
---

# Classification with Logistic Regression

§I Large Language Models › Logistic Regression › Classification with Logistic Regression · pp. 75–77 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.3 • CLASSIFICATION WITH LOGISTIC REGRESSION The sigmoid function from the prior section thus gives us a way to take an instance x and compute the probability P(y = 1|x). How do we make a decision about which class to apply to a test instance x? For a given x, we say yes if the probability P(y = 1|x) is more than .5, and no otherwise. We call .5 the decision boundary: decision boundary decision(x) =  1 if P(y = 1|x) > 0.5 0 otherwise Let’s have some examples of applying logistic regression as a classifier for language tasks. Suppose we are doing binary sentiment classification on movie review text, and we would like to know whether to assign the sentiment class + or −to a review document doc. We’ll represent each input observation by the 6 features x1 ...x6 of the input shown in the following table; Fig. 4.2 shows features in a sample mini test document. Var Definition Value in Fig. 4.2 x1 count(positive lexicon words ∈doc) x2 count(negative lexicon words ∈doc) x3  1 if “no” ∈doc 0 otherwise x4 count(1st and 2nd pronouns ∈doc) x5  1 if “!” ∈doc 0 otherwise x6 ln(word+punctuation count of doc) ln(66) = 4.19 It's hokey . There are virtually no surprises , and the writing is second-rate .

## Key terms
- **feature** — 40 mentions
- **word** — 18 mentions
- **input** — 15 mentions
- **test** — 10 mentions
- **period** — 10 mentions
- **value** — 9 mentions
- **otherwise** — 7 mentions
- **positive** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=75|Speech and Language Processing.pdf p. 75]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/the-sigmoid-function]]
- Next: [[research/slp/learning-in-logistic-regression]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

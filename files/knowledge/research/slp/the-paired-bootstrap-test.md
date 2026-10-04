---
title: "The Paired Bootstrap Test"
summary: "§I Large Language Models › Logistic Regression › Statistical : CHAPTER 4 • LOGISTIC REGRESSION statistic (such as normality) that don’t generally hold in our cases. So in NLP we usually use non-parametric tests based on sampling: we artificially create many versions of the experi"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "96-96"
---

# The Paired Bootstrap Test

§I Large Language Models › Logistic Regression › Statistical Significance Testing › The Paired Bootstrap Test · pp. 96–96 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION statistic (such as normality) that don’t generally hold in our cases. So in NLP we usually use non-parametric tests based on sampling: we artificially create many versions of the experimental setup. For example, if we had lots of different test sets x′ we could just measure all the δ(x′) for all the x′. That gives us a distribution. Now we set a threshold (like .01) and if we see in this distribution that 99% or more of those deltas are smaller than the delta we observed, i.e., that p-value(x)-the probability of seeing a δ(x) as big as the one we saw-is less than .01, then we can reject the null hypothesis and agree that δ(x) was a sufficiently surprising difference and A is really a better algorithm than B. There are two common non-parametric tests used in NLP: approximate randomization (Noreen, 1989) and the bootstrap test. We will describe bootstrap approximate randomization below, showing the paired version of the test, which again is most common in NLP. Paired tests are those in which we compare two sets of observations that are aligned: paired each observation in one set can be paired with an observation in another. This happens naturally when we are comparing the performance of two systems on the same test set; we can pair the performance of system A on an individual observation xi with the performance of system B on the same xi.

## Key terms
- **test** — 20 mentions
- **sets** — 7 mentions
- **create** — 6 mentions
- **bootstrap** — 5 mentions
- **wrong** — 5 mentions
- **cell** — 5 mentions
- **sampling** — 4 mentions
- **paired** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=96|Speech and Language Processing.pdf p. 96]]

## Liens
- Up: [[research/slp/statistical-significance-testing]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

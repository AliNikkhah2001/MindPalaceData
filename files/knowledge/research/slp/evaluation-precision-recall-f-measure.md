---
title: "Evaluation: Precision, Recall, F-measure"
summary: "§I Large Language Models › Logistic Regression › Evaluation: : CHAPTER 4 • LOGISTIC REGRESSION The loss function for a single example x, generalizing from binary logistic regression, is the sum of the logs of the K output classes, each weighted by the indicator function yk (Eq."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "90-92"
---

# Evaluation: Precision, Recall, F-measure

§I Large Language Models › Logistic Regression › Evaluation: Precision, Recall, F-measure · pp. 90–92 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION The loss function for a single example x, generalizing from binary logistic regression, is the sum of the logs of the K output classes, each weighted by the indicator function yk (Eq. 4.38). This turns out to be just the negative log probability of the correct class c (Eq. 4.39): LCE(ˆy,y) = − K X k=1 yk log ˆyk (4.38) = −log ˆyc, (where c is the correct class) (4.39) = −log ˆp(yc = 1|x) (where c is the correct class) = −log exp(wc ·x+bc) PK j=1 exp(wj ·x+bj) (c is the correct class) (4.40) How did we get from Eq. 4.38 to Eq. 4.39? Because only one class (let’s call it c) is the correct one, the vector y takes the value 1 only for this value of k, i.e., has yc = 1 and yj = 0 ∀j̸ = c. That means the terms in the sum in Eq. 4.38 will all be 0 except for the term corresponding to the true class c. Hence the cross-entropy loss is simply the log of the output probability corresponding to the correct class, and we therefore also call Eq. 4.39 the negative log likelihood loss. negative log likelihood loss Of course for gradient descent we don’t need the loss, we need its gradient. The gradient for a single example turns out to be very similar to the gradient for binary logistic regression, (ˆy−y)x, that we saw in Eq.

## Key terms
- **positive** — 18 mentions
- **recall** — 18 mentions
- **precision** — 17 mentions
- **negative** — 15 mentions
- **system** — 14 mentions
- **class** — 13 mentions
- **spam** — 13 mentions
- **true** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=90|Speech and Language Processing.pdf p. 90]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/learning-in-multinomial-logistic-regression]]
- Next: [[research/slp/test-sets-and-cross-validation]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

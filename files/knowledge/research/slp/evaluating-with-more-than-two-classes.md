---
title: "Evaluating with more than two classes"
summary: "§I Large Language Models › Logistic Regression › Evaluation: : CHAPTER 4 • LOGISTIC REGRESSION Recall measures the percentage of items actually present in the input that were recall correctly identified by the system."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "92-92"
---

# Evaluating with more than two classes

§I Large Language Models › Logistic Regression › Evaluation: Precision, Recall, F-measure › Evaluating with more than two classes · pp. 92–92 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION Recall measures the percentage of items actually present in the input that were recall correctly identified by the system. Recall is defined as Recall = true positives true positives + false negatives Precision and recall will help solve the problem with the useless “nothing is pie” classifier. This classifier, despite having a fabulous accuracy of 99.99%, has a terrible recall of 0 (since there are no true positives, and 100 false negatives, the recall is 0/100). You should convince yourself that the precision at finding relevant tweets is equally problematic. Thus precision and recall, unlike accuracy, emphasize true positives: finding the things that we are supposed to be looking for. There are many ways to define a single metric that incorporates aspects of both precision and recall. The simplest of these combinations is the F-measure (van F-measure Rijsbergen, 1975) , defined as: Fβ = (β 2 +1)PR β 2P+R The β parameter differentially weights the importance of recall and precision, based perhaps on the needs of an application. Values of β > 1 favor recall, while values of β < 1 favor precision. When β = 1, precision and recall are equally balanced; this is the most frequently used metric, and is called Fβ=1 or just F1: F1 F1 = 2PR P+R (4.42) F-measure comes from a weighted harmonic mean of precision and recall.

## Key terms
- **recall** — 15 mentions
- **precision** — 10 mentions
- **mean** — 6 mentions
- **classes** — 5 mentions
- **positive** — 5 mentions
- **true** — 4 mentions
- **f-measure** — 4 mentions
- **values** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=92|Speech and Language Processing.pdf p. 92]]

## Liens
- Up: [[research/slp/evaluation-precision-recall-f-measure]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

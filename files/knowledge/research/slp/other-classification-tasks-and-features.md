---
title: "Other classification tasks and features"
summary: "§I Large Language Models › Logistic Regression › Classificati: CHAPTER 4 • LOGISTIC REGRESSION a positive sentiment decision, while w2 tells us the importance of negative lexicon words."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "76-76"
---

# Other classification tasks and features

§I Large Language Models › Logistic Regression › Classification with Logistic Regression › Other classification tasks and features · pp. 76–76 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 4 • LOGISTIC REGRESSION a positive sentiment decision, while w2 tells us the importance of negative lexicon words. Note that w1 = 2.5 is positive, while w2 = −5.0, meaning that negative words are negatively associated with a positive sentiment decision, and are about twice as important as positive words. Given these 6 features and the input review x, P(+|x) and P(−|x) can be computed using Eq. 4.5: P(+|x) = P(y = 1|x) = σ(w ·x+b) = σ([2.5,−5.0,−1.2,0.5,2.0,0.7]·[3,2,1,3,0,4.19]+0.1) = σ(.833) = 0.70 (4.8) P(−|x) = P(y = 0|x) = 1−σ(w ·x+b) = 0.30 Logistic regression is applied to all sorts of NLP tasks, and any property of the input can be a feature. Consider the task of period disambiguation: deciding if a period period disambiguation is the end of a sentence or part of a word, by classifying each period into one of two classes, EOS (end-of-sentence) and not-EOS. We might use features like x1 below expressing that the current word is lower case, perhaps with a positive weight. Or a feature expressing that the current word is in our abbreviations dictionary (“Prof.”), perhaps with a negative weight. A feature can also express a combination of properties. For example a period following an upper case word is likely to be an EOS, but if the word itself is St.

## Key terms
- **feature** — 23 mentions
- **word** — 13 mentions
- **period** — 10 mentions
- **positive** — 5 mentions
- **disambiguation** — 4 mentions
- **case** — 4 mentions
- **training** — 4 mentions
- **negative** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=76|Speech and Language Processing.pdf p. 76]]

## Liens
- Up: [[research/slp/classification-with-logistic-regression]]
- ← Prev: [[research/slp/sentiment-classification]]
- Next: [[research/slp/processing-many-examples-at-once]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

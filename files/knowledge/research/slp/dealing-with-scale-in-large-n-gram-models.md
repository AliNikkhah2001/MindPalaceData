---
title: "Dealing with scale in large n-gram models"
summary: "§I Large Language Models › N-gram Language Models › N-Grams ›: Here are a few other useful probabilities: P(i|<s>) = 0.25 P(english|want) = 0.0011 P(food|english) = 0.5 P(</s>|food) = 0.68 Now we can compute the probability of sentences like I want English food or I want Chinese "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "51-51"
---

# Dealing with scale in large n-gram models

§I Large Language Models › N-gram Language Models › N-Grams › Dealing with scale in large n-gram models · pp. 51–51 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.1 • N-GRAMS i want to eat chinese food lunch spend i 0.002 0.33 0.0036 0.00079 want 0.0022 0.66 0.0011 0.0065 0.0065 0.0054 0.0011 to 0.00083 0.0017 0.28 0.00083 0.0025 0.087 eat 0.0027 0.021 0.0027 0.056 chinese 0.0063 0.52 0.0063 food 0.014 0.014 0.00092 0.0037 lunch 0.0059 0.0029 spend 0.0036 0.0036 Figure 3.2 Bigram probabilities for eight words in the Berkeley Restaurant Project corpus of 9332 sentences. Zero probabilities are in gray. Here are a few other useful probabilities: P(i|<s>) = 0.25 P(english|want) = 0.0011 P(food|english) = 0.5 P(</s>|food) = 0.68 Now we can compute the probability of sentences like I want English food or I want Chinese food by simply multiplying the appropriate bigram probabilities together, as follows: P(<s> i want english food </s>) = P(i|<s>)P(want|i)P(english|want) P(food|english)P(</s>|food) = 0.25×0.33×0.0011×0.5×0.68 = 0.000031 We leave it as Exercise 3.2 to compute the probability of i want chinese food. What kinds of linguistic phenomena are captured in these bigram statistics? Some of the bigram probabilities above encode some facts that we think of as strictly syntactic in nature, like the fact that what comes after eat is usually a noun or an adjective, or that what comes after to is usually a verb.

## Key terms
- **probabilities** — 16 mentions
- **food** — 11 mentions
- **want** — 9 mentions
- **english** — 7 mentions
- **chinese** — 5 mentions
- **bigram** — 4 mentions
- **probability** — 4 mentions
- **multiplying** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=51|Speech and Language Processing.pdf p. 51]]

## Liens
- Up: [[research/slp/n-grams]]
- ← Prev: [[research/slp/how-to-estimate-probabilities]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

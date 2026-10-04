---
title: "Generalizing vs. overfitting the training set"
summary: "§I Large Language Models › N-gram Language Models › Generaliz: OVERFITTING THE TRAINING SET 0.06 the .06 0.03 of 0.02 a 0.02 to in .09 .11 .13 .15 … however (p=0.0003) polyphonic p=0.0000018 … 0.02 .66 .99 … Figure 3.3 A visualization of the sampling distribution for sampling sen"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "57-58"
---

# Generalizing vs. overfitting the training set

§I Large Language Models › N-gram Language Models › Generalizing vs. overfitting the training set · pp. 57–58 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.5 • GENERALIZING VS. OVERFITTING THE TRAINING SET 0.06 the .06 0.03 of 0.02 a 0.02 to in .09 .11 .13 .15 … however (p=0.0003) polyphonic p=0.0000018 … 0.02 .66 .99 … Figure 3.3 A visualization of the sampling distribution for sampling sentences by repeatedly sampling unigrams. The blue bar represents the relative frequency of each word (we’ve ordered them from most frequent to least frequent, but the choice of order is arbitrary). The number line shows the cumulative probabilities. If we choose a random number between 0 and 1, it will fall in an interval corresponding to some word. The expectation for the random number to fall in the larger intervals of one of the frequent words (the, of, a) is much higher than in the smaller interval of one of the rare words (polyphonic). proportional to its frequency. Fig. 3.3 shows a visualization, using a unigram LM computed from the text of this book. We choose a random value between 0 and 1, find that point on the probability line, and print the word whose interval includes this chosen value. We continue choosing random numbers and generating words until we randomly generate the sentence-final token </s>. We can use the same technique to generate bigrams by first generating a random bigram that starts with <s> (according to its bigram probability).

## Key terms
- **word** — 16 mentions
- **sentences** — 12 mentions
- **model** — 12 mentions
- **gram** — 11 mentions
- **training** — 10 mentions
- **bigram** — 10 mentions
- **n-gram** — 9 mentions
- **random** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=57|Speech and Language Processing.pdf p. 57]]

## Liens
- Up: [[research/slp/n-gram-language-models]]
- ← Prev: [[research/slp/sampling-sentences-from-a-language-model]]
- Next: [[research/slp/smoothing-interpolation-and-backoff]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "HMM Part-of-Speech Tagging"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: 17.4 • HMM PART-OF-SPEECH TAGGING In this section we introduce our first sequence labeling algorithm, the Hidden Markov Model, and show how to apply it to part-of-speech tagging."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "397-403"
---

# HMM Part-of-Speech Tagging

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › HMM Part-of-Speech Tagging · pp. 397–403 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
17.4 • HMM PART-OF-SPEECH TAGGING In this section we introduce our first sequence labeling algorithm, the Hidden Markov Model, and show how to apply it to part-of-speech tagging. Recall that a sequence labeler is a model whose job is to assign a label to each unit in a sequence, thus mapping a sequence of observations to a sequence of labels of the same length. The HMM is a classic model that introduces many of the key concepts of sequence modeling that we will see again in more modern models. An HMM is a probabilistic sequence model: given a sequence of units (words, letters, morphemes, sentences, whatever), it computes a probability distribution over possible sequences of labels and chooses the best label sequence. The HMM is based on augmenting the Markov chain. A Markov chain is a model Markov chain that tells us something about the probabilities of sequences of random variables, states, each of which can take on values from some set. These sets can be words, or tags, or symbols representing anything, for example the weather. A Markov chain makes a very strong assumption that if we want to predict the future in the sequence, all that matters is the current state. All the states before the current state have no impact on the future except via the current state.

## Key terms
- **state** — 34 mentions
- **sequence** — 32 mentions
- **probability** — 30 mentions
- **markov** — 23 mentions
- **model** — 14 mentions
- **chain** — 13 mentions
- **word** — 13 mentions
- **observation** — 13 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=397|Speech and Language Processing.pdf p. 397]]

## Liens
- Up: [[research/slp/sequence-labeling-for-parts-of-speech-and-named-entities]]
- ← Prev: [[research/slp/named-entities-and-named-entity-tagging]]
- Next: [[research/slp/conditional-random-fields-crfs]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

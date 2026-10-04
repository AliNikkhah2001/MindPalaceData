---
title: "The Hidden Markov Model"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES Formally, a Markov chain is specified by the following components: Q = q1q2 ...qN a set of N states A = a11a12 ...aN1 ...aNN a transition probabili"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "398-398"
---

# The Hidden Markov Model

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › HMM Part-of-Speech Tagging › The Hidden Markov Model · pp. 398–398 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES Formally, a Markov chain is specified by the following components: Q = q1q2 ...qN a set of N states A = a11a12 ...aN1 ...aNN a transition probability matrix A, each aij representing the probability of moving from state i to state j, s.t. Pn j=1 aij = 1 ∀i π = π1,π2,...,πN an initial probability distribution over states. πi is the probability that the Markov chain will start in state i. Some states j may have πj = 0, meaning that they cannot be initial states. Also, Pn i=1 πi = 1 Before you go on, use the sample probabilities in Fig. 17.8a (with π = [0.1,0.7,0.2]) to compute the probability of each of the following sequences: (17.4) hot hot hot hot (17.5) cold hot cold hot What does the difference in these probabilities tell you about a real-world weather fact encoded in Fig. 17.8a? A Markov chain is useful when we need to compute a probability for a sequence of observable events. In many cases, however, the events we are interested in are hidden: we don’t observe them directly. For example we don’t normally observe hidden part-of-speech tags in a text. Rather, we see words, and must infer the tags from the word sequence.

## Key terms
- **state** — 19 mentions
- **probability** — 13 mentions
- **markov** — 9 mentions
- **hidden** — 7 mentions
- **sequence** — 6 mentions
- **observation** — 6 mentions
- **chain** — 5 mentions
- **initial** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=398|Speech and Language Processing.pdf p. 398]]

## Liens
- Up: [[research/slp/hmm-part-of-speech-tagging]]
- ← Prev: [[research/slp/markov-chains]]
- Next: [[research/slp/the-components-of-an-hmm-tagger]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

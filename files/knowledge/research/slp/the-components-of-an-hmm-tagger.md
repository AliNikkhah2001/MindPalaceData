---
title: "The components of an HMM tagger"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: 17.4 • HMM PART-OF-SPEECH TAGGING An HMM has two components, the A and B probabilities, both estimated by counting on a tagged training corpus."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "399-399"
---

# The components of an HMM tagger

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › HMM Part-of-Speech Tagging › The components of an HMM tagger · pp. 399–399 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
17.4 • HMM PART-OF-SPEECH TAGGING An HMM has two components, the A and B probabilities, both estimated by counting on a tagged training corpus. (For this example we’ll use the tagged WSJ corpus.) The A matrix contains the tag transition probabilities P(ti|ti−1) which represent the probability of a tag occurring given the previous tag. For example, modal verbs like will are very likely to be followed by a verb in the base form, a VB, like race, so we expect this probability to be high. We compute the maximum likelihood estimate of this transition probability by counting, out of the times we see the first tag in a labeled corpus, how often the first tag is followed by the second: P(ti|ti−1) = C(ti−1,ti) C(ti−1) (17.8) In the WSJ corpus, for example, MD occurs 13124 times of which it is followed by VB 10471, for an MLE estimate of P(VB|MD) = C(MD,VB) C(MD) = 10471 13124 = .80 (17.9) The B emission probabilities, P(wi|ti), represent the probability, given a tag (say MD), that it will be associated with a given word (say will). The MLE of the emission probability is P(wi|ti) = C(ti,wi) C(ti) (17.10) Of the 13124 occurrences of MD in the WSJ corpus, it is associated with will 4046 times:…

## Key terms
- **probability** — 6 mentions
- **corpus** — 5 mentions
- **probabilities** — 4 mentions
- **likelihood** — 4 mentions
- **transition** — 3 mentions
- **likely** — 3 mentions
- **followed** — 3 mentions
- **times** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=399|Speech and Language Processing.pdf p. 399]]

## Liens
- Up: [[research/slp/hmm-part-of-speech-tagging]]
- ← Prev: [[research/slp/the-hidden-markov-model]]
- Next: [[research/slp/hmm-tagging-as-decoding]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "The Viterbi Algorithm"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: 17.4 • HMM PART-OF-SPEECH TAGGING function VITERBI(observations of len T,state-graph of len N) returns best-path, path-prob create a path probability matrix viterbi[N,T] create a backpointer matrix backpointer[N,T] fo"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "401-401"
---

# The Viterbi Algorithm

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › HMM Part-of-Speech Tagging › The Viterbi Algorithm · pp. 401–401 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
17.4 • HMM PART-OF-SPEECH TAGGING function VITERBI(observations of len T,state-graph of len N) returns best-path, path-prob create a path probability matrix viterbi[N,T] create a backpointer matrix backpointer[N,T] for each state s from 1 to N do ; initialization step viterbi[s,1]←πs ∗bs(o1) backpointer[s,1]←0 for each time step t from 2 to T do ; recursion step for each state s from 1 to N do viterbi[s,t]← N max s′=1 viterbi[s′,t −1] ∗as′,s ∗bs(ot) backpointer[s,t]← N argmax s′=1 viterbi[s′,t −1] ∗as′,s ∗bs(ot) bestpathprob← N max s=1 viterbi[s,T] ; termination step bestpathpointer← N argmax s=1 viterbi[s,T] ; termination step bestpath←the path starting at state bestpathpointer, that follows backpointer[] to states back in time return bestpath, bestpathprob Figure 17.10 Viterbi algorithm for finding the optimal sequence of tags. Given an observation sequence and an HMM λ = (A,B), the algorithm returns the state path through the HMM that assigns maximum likelihood to the observation sequence. The decoding algorithm for HMMs is the Viterbi algorithm shown in Fig. 17.10. Viterbi algorithm As an instance of dynamic programming, Viterbi resembles the dynamic programming minimum edit distance algorithm of Chapter 2.

## Key terms
- **viterbi** — 16 mentions
- **state** — 13 mentions
- **algorithm** — 8 mentions
- **path** — 7 mentions
- **probability** — 7 mentions
- **cell** — 7 mentions
- **backpointer** — 5 mentions
- **step** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=401|Speech and Language Processing.pdf p. 401]]

## Liens
- Up: [[research/slp/hmm-part-of-speech-tagging]]
- ← Prev: [[research/slp/hmm-tagging-as-decoding]]
- Next: [[research/slp/working-through-an-example-2]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

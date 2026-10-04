---
title: "Further Details "
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: 17.6 • EVALUATION OF NAMED ENTITY RECOGNITION The requisite changes from HMM Viterbi have to do only with how we fill each cell."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "409-410"
---

# Further Details 

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › Further Details  · pp. 409–410 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
17.6 • EVALUATION OF NAMED ENTITY RECOGNITION The requisite changes from HMM Viterbi have to do only with how we fill each cell. Recall from Eq. 17.19 that the recursive step of the Viterbi equation computes the Viterbi value of time t for state j as vt(j) = N max i=1 vt−1(i)aij bj(ot); 1 ≤j ≤N,1 < t ≤T (17.31) which is the HMM implementation of vt(j) = N max i=1 vt−1(i) P(sj|si) P(ot|s j) 1 ≤j ≤N,1 < t ≤T (17.32) The CRF requires only a slight change to this latter formula, replacing the a and b prior and likelihood probabilities with the CRF features: vt(j) = N max i=1 " vt−1(i)+ K X k=1 wk fk(yt−1,yt,X,t) 1 ≤j ≤N,1 < t ≤T # (17.33) Learning in CRFs relies on the same supervised learning algorithms we presented for logistic regression. Given a sequence of observations, feature functions, and corresponding outputs, we use stochastic gradient descent to train the weights to maximize the log-likelihood of the training corpus. The local nature of linear-chain CRFs means that the forward-backward algorithm introduced for HMMs in Appendix A can be extended to a CRF version that will efficiently compute the necessary derivatives. As with logistic regression, L1 or L2 regularization is important.

## Key terms
- **word** — 11 mentions
- **tagging** — 8 mentions
- **named** — 7 mentions
- **entity** — 7 mentions
- **labeled** — 7 mentions
- **part-of-speech** — 6 mentions
- **english** — 6 mentions
- **language** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=409|Speech and Language Processing.pdf p. 409]]

## Liens
- Up: [[research/slp/sequence-labeling-for-parts-of-speech-and-named-entities]]
- ← Prev: [[research/slp/evaluation-of-named-entity-recognition]]
- Next: [[research/slp/summary-16]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

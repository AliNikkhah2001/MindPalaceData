---
title: "Minimum Bayes Risk Decoding"
summary: "§I Large Language Models › Machine Translation › Decoding in : CHAPTER 12 • MACHINE TRANSLATION function BEAMDECODE(c, beam width) returns best paths y0, h0 ←0 path←() complete paths←() state←(c, y0, h0, path) ;initial state frontier←⟨state⟩ ;initial frontier while frontier conta"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "280-280"
---

# Minimum Bayes Risk Decoding

§I Large Language Models › Machine Translation › Decoding in MT: Beam Search › Minimum Bayes Risk Decoding · pp. 280–280 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 12 • MACHINE TRANSLATION function BEAMDECODE(c, beam width) returns best paths y0, h0 ←0 path←() complete paths←() state←(c, y0, h0, path) ;initial state frontier←⟨state⟩ ;initial frontier while frontier contains incomplete paths and beamwidth > 0 extended frontier←⟨⟩ for each state ∈frontier do y←DECODE(state) for each word i ∈Vocabulary do successor←NEWSTATE(state, i, yi) extended frontier←ADDTOBEAM(successor, extended frontier, beam width) for each state in extended frontier do if state is complete do complete paths←APPEND(complete paths, state) extended frontier←REMOVE(extended frontier, state) beam width←beam width - 1 frontier←extended frontier return completed paths function NEWSTATE(state, word, word prob) returns new state function ADDTOBEAM(state, frontier, width) returns updated frontier if LENGTH(frontier) < width then frontier←INSERT(state, frontier) else if SCORE(state) > SCORE(WORSTOF(frontier)) frontier←REMOVE(WORSTOF(frontier)) frontier←INSERT(state, frontier) return frontier Figure 12.10 Beam search decoding. same length.) For this reason we often apply length normalization methods, like dividing the logprob by the number of words: score(y) = 1 t logP(y|x) = 1 t tX i=1 logP(yi|y1,...,yi−1,x) (12.16) For MT we generally use beam widths k between 5 and 10, giving us k hypotheses at the end.

## Key terms
- **frontier** — 23 mentions
- **state** — 16 mentions
- **path** — 8 mentions
- **beam** — 7 mentions
- **width** — 7 mentions
- **extended** — 7 mentions
- **return** — 5 mentions
- **complete** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=280|Speech and Language Processing.pdf p. 280]]

## Liens
- Up: [[research/slp/decoding-in-mt-beam-search]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

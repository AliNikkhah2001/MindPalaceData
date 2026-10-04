---
title: "Conditional Random Fields (CRFs)"
summary: "§II Annotating Linguistic Structure › Sequence Labeling for P: CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES the observation likelihood of the word Janet given the tag for that cell."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "404-408"
---

# Conditional Random Fields (CRFs)

§II Annotating Linguistic Structure › Sequence Labeling for Parts of Speech and Named Entities › Conditional Random Fields (CRFs) · pp. 404–408 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 17 • SEQUENCE LABELING FOR PARTS OF SPEECH AND NAMED ENTITIES the observation likelihood of the word Janet given the tag for that cell. Most of the cells in the column are zero since the word Janet cannot be any of those tags. The reader should find this in Fig. 17.14. Next, each cell in the will column gets updated. For each state, we compute the value viterbi[s,t] by taking the maximum over the extensions of all the paths from the previous column that lead to the current cell according to Eq. 17.19. We have shown the values for the MD, VB, and NN cells. Each cell gets the max of the 7 values from the previous column, multiplied by the appropriate transition probability; as it happens in this case, most of them are zero from the previous column. The remaining value is multiplied by the relevant observation probability, and the (trivial) max is taken. In this case the final value, 2.772e-8, comes from the NNP state at the previous column. The reader should fill in the rest of the lattice in Fig. 17.14 and backtrace to see whether or not the Viterbi algorithm returns the gold state sequence NNP MD VB DT NN. While the HMM is a useful and powerful model, it turns out that HMMs need a number of augmentations to achieve high accuracy.

## Key terms
- **feature** — 54 mentions
- **word** — 35 mentions
- **sequence** — 20 mentions
- **model** — 11 mentions
- **value** — 10 mentions
- **output** — 10 mentions
- **these** — 9 mentions
- **shape** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=404|Speech and Language Processing.pdf p. 404]]

## Liens
- Up: [[research/slp/sequence-labeling-for-parts-of-speech-and-named-entities]]
- ← Prev: [[research/slp/hmm-part-of-speech-tagging]]
- Next: [[research/slp/evaluation-of-named-entity-recognition]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

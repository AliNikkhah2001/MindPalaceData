---
title: "Computing the mention and antecedent scores m and c "
summary: "§II Annotating Linguistic Structure › Coreference Resolution : CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING embedding for the first (start) token of the span, the encoder output for the last (end) token of the span, and a third vector which is an attention-based represe"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "546-546"
---

# Computing the mention and antecedent scores m and c 

§II Annotating Linguistic Structure › Coreference Resolution and Entity Linking › A neural mention-ranking algorithm › Computing the mention and antecedent scores m and c  · pp. 546–546 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 23 • COREFERENCE RESOLUTION AND ENTITY LINKING embedding for the first (start) token of the span, the encoder output for the last (end) token of the span, and a third vector which is an attention-based representation: gi = [hSTART(i),hEND(i),hATT(i)] (23.50) The goal of the attention vector is to represent which word/token is the likely syntactic head-word of the span; we saw in the prior section that head-words are a useful feature; a matching head-word is a good indicator of coreference. The attention representation is computed as usual; the system learns a weight vector wα, and computes its dot product with the hidden state ht transformed by a FFN: αt = wα · FFNα(ht) (23.51) The attention score is normalized into a distribution via a softmax: ai,t = exp(αt) PEND(i) k=START(i) exp(αk) (23.52) And then the attention distribution is used to create a vector hATT(i) which is an attention-weighted sum of the embeddings et of each of the words in span i: hATT(i) = END(i) X t=START(i) ai,t ·et (23.53) Fig. 23.5 shows the computation of the span representation and the mention score. Encodings (h) … Encoder General Electric said the Postal Service contacted the company Span head (…

## Key terms
- **span** — 11 mentions
- **vector** — 5 mentions
- **representation** — 5 mentions
- **score** — 5 mentions
- **mention** — 5 mentions
- **hatt** — 4 mentions
- **attention** — 4 mentions
- **start** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=546|Speech and Language Processing.pdf p. 546]]

## Liens
- Up: [[research/slp/a-neural-mention-ranking-algorithm]]
- ← Prev: [[research/slp/computing-span-representations]]
- Next: [[research/slp/learning-2]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

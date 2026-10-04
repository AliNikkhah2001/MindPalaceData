---
title: "More on Sampling"
summary: "§I Large Language Models › Transformers › More on Sampling: CHAPTER 8 • TRANSFORMERS Layer L Transformer Block Softmax over vocabulary V Unembedding layer … [1 x |V|] Logits Word probabilities [1 x |V|] hL w1 w2 wN hL hL N [d x |V|] [1 x d] Unembedding layer U = ET y1 y2 y|V| … u"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "198-199"
---

# More on Sampling

§I Large Language Models › Transformers › More on Sampling · pp. 198–199 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 8 • TRANSFORMERS Layer L Transformer Block Softmax over vocabulary V Unembedding layer … [1 x |V|] Logits Word probabilities [1 x |V|] hL w1 w2 wN hL hL N [d x |V|] [1 x d] Unembedding layer U = ET y1 y2 y|V| … u1 u2 u|V| … Language Model Head takes hL N and outputs a distribution over vocabulary V Figure 8.15 The language modeling head: the circuit at the top of a transformer that maps from the output embedding for token N from the last transformer layer (hL N) to a probability distribution over words in the vocabulary V. A softmax layer turns the logits u into the probabilities y over the vocabulary. u = hL N ET (8.46) y = softmax(u) (8.47) We can use these probabilities to do things like help assign a probability to a given text. But the most important usage is to generate text, which we do by sampling a word from these probabilities y. We might sample the highest probability word (‘greedy’ decoding), or use another of the sampling methods from Section 7.4 or Section 8.6. In either case, whatever entry yk we choose from the probability vector y, we generate the word that has that index k. Fig. 8.16 shows the total stacked architecture for one token i. Note that the input to each transformer layer xℓ i is the same as the output from the preceding layer hℓ−1 i .

## Key terms
- **layer** — 17 mentions
- **word** — 16 mentions
- **transformer** — 10 mentions
- **model** — 9 mentions
- **language** — 7 mentions
- **token** — 7 mentions
- **norm** — 7 mentions
- **probabilities** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=198|Speech and Language Processing.pdf p. 198]]

## Liens
- Up: [[research/slp/transformers]]
- ← Prev: [[research/slp/the-language-modeling-head]]
- Next: [[research/slp/training]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

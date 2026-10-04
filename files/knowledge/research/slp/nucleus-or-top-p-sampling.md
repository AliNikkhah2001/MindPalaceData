---
title: "Nucleus or top-p sampling"
summary: "§I Large Language Models › Transformers › More on Sampling › : Renormalize the scores of the k words to be a legitimate probability distribution. Randomly sample a word from within these remaining k most-probable words according to its probability."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "200-200"
---

# Nucleus or top-p sampling

§I Large Language Models › Transformers › More on Sampling › Nucleus or top-p sampling · pp. 200–200 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 8 • TRANSFORMERS 4. Renormalize the scores of the k words to be a legitimate probability distribution. 5. Randomly sample a word from within these remaining k most-probable words according to its probability. When k = 1, top-k sampling is identical to greedy decoding. Setting k to a larger number than 1 leads us to sometimes select a word which is not necessarily the most probable, but is still probable enough, and whose choice results in generating more diverse but still high-enough-quality text. One problem with top-k sampling is that k is fixed, but the shape of the probability distribution over words differs in different contexts. If we set k = 10, sometimes the top 10 words will be very likely and include most of the probability mass, but other times the probability distribution will be flatter and the top 10 words will only include a small part of the probability mass. An alternative, called top-p sampling or nucleus sampling (Holtzman et al., top-p sampling 2020), is to keep not the top k words, but the top p percent of the probability mass. The goal is the same; to truncate the distribution to remove the very unlikely words. But by measuring probability rather than the number of words, the hope is that the measure will be more robust in very different contexts, dynamically increasing and decreasing the pool of word candidates.

## Key terms
- **word** — 15 mentions
- **probability** — 10 mentions
- **distribution** — 7 mentions
- **training** — 7 mentions
- **loss** — 7 mentions
- **model** — 6 mentions
- **sequence** — 6 mentions
- **sampling** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=200|Speech and Language Processing.pdf p. 200]]

## Liens
- Up: [[research/slp/more-on-sampling]]
- ← Prev: [[research/slp/top-k-sampling]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

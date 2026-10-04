---
title: "Downstream tasks: Reasoning and world knowledge"
summary: "§I Large Language Models › Large Language Models › Evaluating: 7.6 • EVALUATING LARGE LANGUAGE MODELS smaller the longer the text is; this is clear from the chain rule, since if we are multiplying more probabilities, and each probability by definition is less than one, the produc"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "173-173"
---

# Downstream tasks: Reasoning and world knowledge

§I Large Language Models › Large Language Models › Evaluating Large Language Models › Downstream tasks: Reasoning and world knowledge · pp. 173–173 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
7.6 • EVALUATING LARGE LANGUAGE MODELS smaller the longer the text is; this is clear from the chain rule, since if we are multiplying more probabilities, and each probability by definition is less than one, the product will get smaller and smaller. So it’s useful to have a metric that is per-token, normalized by length, so we could compare across texts of different lengths. A function of probability called perplexity is such a length-normalized metric. perplexity Recall from page 46 that the perplexity of a model θ on an unseen test set is the inverse probability that θ assigns to the test set (one over the probability of the test set), normalized by the test set length in tokens. For a test set of n tokens w1:n, the perplexity is Perplexityθ(w1:n) = Pθ(w1:n)−1 n = n s Pθ(w1:n) (7.10) To visualize how perplexity can be computed as a function of the probabilities the LM computes for each new word, we can use the chain rule to expand the computation of probability of the test set: Perplexityθ(w1:n) = n v u u t n Y i=1 Pθ(wi|w<i) (7.11) Note that because of the inverse in Eq. 7.10, the higher the probability of the word sequence, the lower the perplexity. Thus the lower the perplexity of a model on the data, the better the model.

## Key terms
- **perplexity** — 16 mentions
- **probability** — 9 mentions
- **model** — 9 mentions
- **test** — 7 mentions
- **language** — 6 mentions
- **accuracy** — 6 mentions
- **inverse** — 5 mentions
- **question** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=173|Speech and Language Processing.pdf p. 173]]

## Liens
- Up: [[research/slp/evaluating-large-language-models]]
- ← Prev: [[research/slp/perplexity]]
- Next: [[research/slp/other-factors-for-evaluating-language-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

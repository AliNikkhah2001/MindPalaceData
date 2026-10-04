---
title: "Perplexity as Weighted Average Branching Factor"
summary: "§I Large Language Models › N-gram Language Models › Evaluatin: 3.3 • EVALUATING LANGUAGE MODELS: PERPLEXITY The perplexity of W computed with a bigram language model is still a geometric mean, but now of the inverse of the bigram probabilities: perplexity(W) = N v u u t N Y i=1 P"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "55-55"
---

# Perplexity as Weighted Average Branching Factor

§I Large Language Models › N-gram Language Models › Evaluating Language Models: Perplexity › Perplexity as Weighted Average Branching Factor · pp. 55–55 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.3 • EVALUATING LANGUAGE MODELS: PERPLEXITY The perplexity of W computed with a bigram language model is still a geometric mean, but now of the inverse of the bigram probabilities: perplexity(W) = N v u u t N Y i=1 P(wi|wi−1) (3.17) What we generally use for word sequence in Eq. 3.15 or Eq. 3.17 is the entire sequence of words in some test set. Since this sequence will cross many sentence boundaries, if our vocabulary includes a between-sentence token <EOS> or separate begin- and end-sentence markers <s> and </s> then we can include them in the probability computation. If we do, then we also include one token per sentence in the total count of word tokens N.2 We mentioned above that perplexity is a function of both the text and the language model: given a text W, different language models will have different perplexities. Because of this, perplexity can be used to compare different language models. For example, here we trained unigram, bigram, and trigram models on 38 million words from the Wall Street Journal newspaper. We then computed the perplexity of each of these models on a WSJ test set using Eq. 3.16 for unigrams, Eq. 3.17 for bigrams, and the corresponding equation for trigrams.

## Key terms
- **perplexity** — 18 mentions
- **model** — 15 mentions
- **language** — 12 mentions
- **word** — 9 mentions
- **probability** — 7 mentions
- **test** — 6 mentions
- **token** — 6 mentions
- **bigram** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=55|Speech and Language Processing.pdf p. 55]]

## Liens
- Up: [[research/slp/evaluating-language-models-perplexity]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "Temperature sampling"
summary: "§I Large Language Models › Large Language Models › Generation: 7.4 • GENERATION AND SAMPLING The algorithm is called random sampling, or random multinomial sampling random sampling (because we are sampling from a multinomial distribution across words)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "165-165"
---

# Temperature sampling

§I Large Language Models › Large Language Models › Generation and Sampling › Temperature sampling · pp. 165–165 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
7.4 • GENERATION AND SAMPLING The algorithm is called random sampling, or random multinomial sampling random sampling (because we are sampling from a multinomial distribution across words). We can formalize random sampling as follows: we are generating a sequence of tokens {w1,w2,...,wN} until we hit the end-of-sequence token, using x ∼p(x) to mean ‘choose x by sampling from the distribution p(x)’: i←1 wi ∼p(w) while wi != EOS i←i + 1 wi ∼p(wi | w<i) Transformer (or other decoder) long and thanks for So ? 1.2 0.9 all the your that … 0.1 -0.5 logits .44 .33 all the your that … .15 .08 probabilities softmax sample a word the u y Figure 7.9 Random multinomial sampling: we randomly chose a word according to its probability. Alas, it turns out random sampling doesn’t work well either. The problem is that even though random sampling is mostly going to generate sensible, high-probable tokens, there are many odd, low-probability tokens in the tail of the distribution, and even though each one is low-probability, if you add up all the rare tokens, they constitute a large enough portion of the distribution that they get chosen often enough to result in generating weird sentences. In other words, greedy decoding is too boring, and random sampling is too random.

## Key terms
- **sampling** — 17 mentions
- **random** — 10 mentions
- **token** — 9 mentions
- **probability** — 9 mentions
- **distribution** — 6 mentions
- **softmax** — 4 mentions
- **word** — 4 mentions
- **logit** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=165|Speech and Language Processing.pdf p. 165]]

## Liens
- Up: [[research/slp/generation-and-sampling]]
- ← Prev: [[research/slp/random-sampling]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

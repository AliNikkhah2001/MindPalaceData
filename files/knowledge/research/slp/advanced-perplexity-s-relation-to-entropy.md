---
title: "Advanced: Perplexity's Relation to Entropy"
summary: "§I Large Language Models › N-gram Language Models › Advanced:: 3.7 • ADVANCED: PERPLEXITY’S RELATION TO ENTROPY has zero counts, we approximate it by backing off to the (n-1)-gram. We continue backing off until we reach a history that has some counts."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "63-65"
---

# Advanced: Perplexity's Relation to Entropy

§I Large Language Models › N-gram Language Models › Advanced: Perplexity's Relation to Entropy · pp. 63–65 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.7 • ADVANCED: PERPLEXITY’S RELATION TO ENTROPY has zero counts, we approximate it by backing off to the (n-1)-gram. We continue backing off until we reach a history that has some counts. For a backoff model to give a correct probability distribution, we have to discount the higher-order n-grams discount to save some probability mass for the lower order n-grams. In practice, instead of discounting, it’s common to use a much simpler non-discounted backoff algorithm called stupid backoff (Brants et al., 2007). stupid backoff Stupid backoff gives up the idea of trying to make the language model a true probability distribution. There is no discounting of the higher-order probabilities. If a higher-order n-gram has a zero count, we simply backoff to a lower order n-gram, weighed by a fixed (context-independent) weight. This algorithm does not produce a probability distribution, so we’ll follow Brants et al. (2007) in referring to it as S: S(wi|wi−N+1:i−1) =    count(wi−N+1:i) count(wi−N+1:i−1) if count(wi−N+1:i) > 0 λS(wi|wi−N+2:i−1) otherwise (3.31) The backoff terminates in the unigram, which has score S(w) = count(w) N . Brants et al. (2007) find that a value of 0.4 worked well for λ.

## Key terms
- **entropy** — 27 mentions
- **horse** — 27 mentions
- **sequence** — 19 mentions
- **probability** — 17 mentions
- **model** — 14 mentions
- **words** — 11 mentions
- **distribution** — 10 mentions
- **cross-entropy** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=63|Speech and Language Processing.pdf p. 63]]

## Liens
- Up: [[research/slp/n-gram-language-models]]
- ← Prev: [[research/slp/smoothing-interpolation-and-backoff]]
- Next: [[research/slp/summary-2]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

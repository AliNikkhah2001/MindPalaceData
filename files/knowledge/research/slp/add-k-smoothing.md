---
title: "Add-k smoothing"
summary: "§I Large Language Models › N-gram Language Models › Smoothing: Previously-zero probabilities are in gray. Rearranging terms, we can solve for C∗(wn−1wn) : C∗(wn−1wn) = [C(wn−1wn)+1]×C(wn−1) C(wn−1)+V (3.27) Figure 3.8 shows the reconstructed counts, computed by Eq."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "61-61"
---

# Add-k smoothing

§I Large Language Models › N-gram Language Models › Smoothing, Interpolation, and Backoff › Add-k smoothing · pp. 61–61 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
3.6 • SMOOTHING, INTERPOLATION, AND BACKOFF i want to eat chinese food lunch spend i 0.0015 0.21 0.00025 0.0025 0.00025 0.00025 0.00025 0.00075 want 0.0013 0.00042 0.26 0.00084 0.0029 0.0029 0.0025 0.00084 to 0.00078 0.00026 0.0013 0.18 0.00078 0.00026 0.0018 0.055 eat 0.00046 0.00046 0.0014 0.00046 0.0078 0.0014 0.02 0.00046 chinese 0.0012 0.00062 0.00062 0.00062 0.00062 0.052 0.0012 0.00062 food 0.0063 0.00039 0.0063 0.00039 0.00079 0.002 0.00039 0.00039 lunch 0.0017 0.00056 0.00056 0.00056 0.00056 0.0011 0.00056 0.00056 spend 0.0012 0.00058 0.0012 0.00058 0.00058 0.00058 0.00058 0.00058 Figure 3.7 Add-one smoothed bigram probabilities for eight of the words (out of V = 1446) in the BeRP corpus of 9332 sentences computed by Eq. 3.26. Previously-zero probabilities are in gray. Rearranging terms, we can solve for C∗(wn−1wn) : C∗(wn−1wn) = [C(wn−1wn)+1]×C(wn−1) C(wn−1)+V (3.27) Figure 3.8 shows the reconstructed counts, computed by Eq. 3.27. i want to eat chinese food lunch spend i 3.8 0.64 6.4 0.64 0.64 0.64 1.9 want 1.2 0.39 0.78 2.7 2.7 2.3 0.78 to 1.9 0.63 3.1 1.9 0.63 4.4 eat 0.34 0.34 0.34 5.8 0.34 chinese 0.2 0.098 0.098 0.098 0.098 8.2 0.2 0.098 food 6.9 0.43 6.9 0.43 0.86 2…

## Key terms
- **count** — 9 mentions
- **want** — 7 mentions
- **smoothing** — 5 mentions
- **chinese** — 5 mentions
- **food** — 5 mentions
- **add-k** — 5 mentions
- **lunch** — 4 mentions
- **spend** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=61|Speech and Language Processing.pdf p. 61]]

## Liens
- Up: [[research/slp/smoothing-interpolation-and-backoff]]
- ← Prev: [[research/slp/laplace-smoothing]]
- Next: [[research/slp/language-model-interpolation]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

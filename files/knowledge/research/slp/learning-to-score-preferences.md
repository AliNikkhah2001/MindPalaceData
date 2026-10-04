---
title: "Learning to Score Preferences"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: 10.2 • LEARNING FROM PREFERENCES exp(δ) = P(oi ≻oj|x) 1−P(oi ≻oj|x) exp(δ)(1−P(oi ≻oj|x)) = P(oi ≻oj|x) exp(δ)−exp(δ)(oi ≻oj|x) = P(oi ≻oj|x) exp(δ) = P(oi ≻oj|x)+exp(δ)P(oi ≻oj|x) exp(δ) = P(oi ≻oj|x)(1+exp(δ)) P(oi "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "235-235"
---

# Learning to Score Preferences

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › Learning from Preferences › Learning to Score Preferences · pp. 235–235 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
10.2 • LEARNING FROM PREFERENCES exp(δ) = P(oi ≻oj|x) 1−P(oi ≻oj|x) exp(δ)(1−P(oi ≻oj|x)) = P(oi ≻oj|x) exp(δ)−exp(δ)(oi ≻oj|x) = P(oi ≻oj|x) exp(δ) = P(oi ≻oj|x)+exp(δ)P(oi ≻oj|x) exp(δ) = P(oi ≻oj|x)(1+exp(δ)) P(oi ≻oj|x) = exp(δ) 1+exp(δ) = 1+exp(−δ) = 1+exp(−(zi −zj)) Bringing us right back to our original formulation. P(oi ≻oj|x) = σ(zi −zj) This approach requires access to the scores, zi, that underlie the given preferences, which we don’t have. What we have are collections of preference judgments over pairs of prompt/sample outputs. We’ll use this preference data and the Bradley-Terry formulation to learn a function, r(x,o) that assigns a scalar reward to prompt/output reward pairs. That is, r(x,o) calculates the z score from above. P(oi ≻oj|x) = σ(zi −zj) (10.1) = σ(r(oi,x)−r(oj,x)) (10.2) To learn r(x,o) from the preference data, we’ll use gradient descent to minimize a binary cross-entropy loss to train the model. Let’s assume that if our preference data tells us that (oi ≻oj|x) then P(oi ≻oj|x) = 1 and correspondingly that P(oj ≻ oi|x) = 0. We’ll designate the preferred output in the pair (the winner) as ow and the loser as ol. With this, the cross-entropy loss for a sin…

## Key terms
- **preference** — 7 mentions
- **output** — 6 mentions
- **model** — 6 mentions
- **loss** — 5 mentions
- **reward** — 4 mentions
- **pair** — 4 mentions
- **prompt** — 3 mentions
- **data** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=235|Speech and Language Processing.pdf p. 235]]

## Liens
- Up: [[research/slp/learning-from-preferences]]
- ← Prev: [[research/slp/modeling-preferences]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

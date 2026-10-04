---
title: "Units"
summary: "§I Large Language Models › Neural Networks › Units: 6.1 • UNITS The building block of a neural network is a single computational unit. A unit takes a set of real valued numbers as input, performs some computation on them, and produces an output."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "129-130"
---

# Units

§I Large Language Models › Neural Networks › Units · pp. 129–130 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
6.1 • UNITS The building block of a neural network is a single computational unit. A unit takes a set of real valued numbers as input, performs some computation on them, and produces an output. At its heart, a neural unit is taking a weighted sum of its inputs, with one additional term in the sum called a bias term. Given a set of inputs x1...xn, a unit has bias term a set of corresponding weights w1...wn and a bias b, so the weighted sum z can be represented as: z = b+ X i wixi (6.1) Often it’s more convenient to express this weighted sum using vector notation; recall from linear algebra that a vector is, at heart, just a list or array of numbers. Thus vector we’ll talk about z in terms of a weight vector w, a scalar bias b, and an input vector x, and we’ll replace the sum with the convenient dot product: z = w ·x+b (6.2) As defined in Eq. 6.2, z is just a real valued number. Finally, instead of using z, a linear function of x, as the output, neural units apply a non-linear function f to z. We will refer to the output of this function as the activation value for the unit, a. Since we are just modeling a single unit, the activation activation for the node is in fact the final output of the network, which we’ll generally call y.

## Key terms
- **unit** — 17 mentions
- **function** — 14 mentions
- **output** — 12 mentions
- **sigmoid** — 9 mentions
- **input** — 8 mentions
- **neural** — 7 mentions
- **bias** — 7 mentions
- **vector** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=129|Speech and Language Processing.pdf p. 129]]

## Liens
- Up: [[research/slp/neural-networks]]
- Next: [[research/slp/the-xor-problem]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "Beyond Multi-Variable Derivatives"
summary: "§Derivatives as Linear Operators › Beyond Multi-Variable Deri: matrix matrix × row matrix × matrix matrix × row matrix × = fast! Correspondingly, the order in which you carry out the chain rule has dramatic consequences for the computational effort required."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "18-19"
---

# Beyond Multi-Variable Derivatives

§Derivatives as Linear Operators › Beyond Multi-Variable Derivatives · pp. 18–19 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
matrix matrix × row matrix × matrix matrix × row matrix × = fast! slow! Figure 3: Matrix multiplication is associative-that is, (AB)C = A(BC) for all A, B, C-but multiplying left-toright can be much more efficient than right-to-left if the leftmost matrix has only one (or few) rows, as shown here. Correspondingly, the order in which you carry out the chain rule has dramatic consequences for the computational effort required. Left-to-right is known as “reverse mode” or “backpropagation”, and is best suited to situations where there are many fewer outputs than inputs. So why does the order of the chain rule matter? Consider the following two examples. Example 16 Suppose you have a lot of inputs n ≫1, and only one output m = 1, with lots of intermediate values, i.e. q = p = n. Then reverse mode (left-to-right) will cost Θ(n2) scalar operations while forward mode (right-to-left) would cost Θ(n3)! This is a huge cost difference, depicted schematically in Fig. 3. Conversely, suppose you have a lot of outputs m ≫1 and only one input n = 1, with lots of intermediate values q = p = m. Then reverse mode would cost Θ(m3) operations but forward mode would be only Θ(m2)! Moral: If you have a lot of inputs and few outputs (the usual case in machine learning and optimization), compute the chain rule left-to-right (reverse mode).

## Key terms
- **matrix** — 14 mentions
- **mode** — 7 mentions
- **output** — 7 mentions
- **rule** — 6 mentions
- **input** — 6 mentions
- **compute** — 6 mentions
- **chain** — 5 mentions
- **reverse** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=18|Matrix Calculus.pdf p. 18]]

## Liens
- Up: [[research/matrix-calculus/derivatives-as-linear-operators]]
- ← Prev: [[research/matrix-calculus/the-chain-rule]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section

---
title: "Forward-over-reverse mode: Second derivatives"
summary: "§Forward and Reverse-Mode Automatic Differentiation › Forward: • Reverse-mode differentiation proceeds in the opposite direction to ordinary computation. This makes reverse- mode AD much more complicated to implement, and adds a lot of storage overhead to the function compu- tati"
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "62-64"
---

# Forward-over-reverse mode: Second derivatives

§Forward and Reverse-Mode Automatic Differentiation › Forward- vs. Reverse-mode Differentiation › Forward-over-reverse mode: Second derivatives · pp. 62–64 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
• Reverse-mode differentiation proceeds in the opposite direction to ordinary computation. This makes reverse- mode AD much more complicated to implement, and adds a lot of storage overhead to the function compu- tation. First you evaluate the function from inputs to outputs, but you (or the AD system) keep a record (a “tape”) of all the intermediate steps of the computation; then, you run the computation in reverse (“play the tape backwards”) to backpropagate the derivatives. As a result of these practical advantages, even for the case of many (n > 1) inputs and a single (m = 1) output, practitioners tell us that they’ve found forward mode to be more efficient until n becomes sufficiently large (perhaps even until n > 100, depending on the function being differentiated and the AD implementation). (You may also be interested in the blog post Engineering Trade-offs in AD by Chris Rackauckas, which is mainly about reverse-mode implementations.) If n = m, where neither approach has a scaling advantage, one typically prefers the lower overhead and simplicity of forward-mode differentiation. This case arises in computing explicit Jacobian matrices for nonlinear root-finding (Sec. 6.1), or Hessian matrices of second derivatives (Sec.

## Key terms
- **function** — 19 mentions
- **mode** — 18 mentions
- **derivative** — 15 mentions
- **reverse** — 14 mentions
- **julia** — 12 mentions
- **differentiation** — 11 mentions
- **forward** — 10 mentions
- **hessian** — 10 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=62|Matrix Calculus.pdf p. 62]]

## Liens
- Up: [[research/matrix-calculus/forward-vs-reverse-mode-differentiation]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section

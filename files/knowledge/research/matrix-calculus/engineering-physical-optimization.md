---
title: "Engineering/Physical Optimization"
summary: "§Nonlinear Root-Finding, Optimization, and Adjoint Differenti: (We’ll return to Hessians in a later lecture.) • Ultimately, there are a lot of techniques and a zoo of competing algorithms that you might need to experiment with to find the best approach for a given problem."
level: "research"
series: "Matrix Calculus (MIT 18.S096 Notes)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, calculus, backprop, section]
pages: "42-42"
---

# Engineering/Physical Optimization

§Nonlinear Root-Finding, Optimization, and Adjoint Differentiation › Optimization › Engineering/Physical Optimization · pp. 42–42 · Matrix Calculus (MIT 18.S096 Notes)

## Extrait
steps (for the root ∇f = 0). (We’ll return to Hessians in a later lecture.) • Ultimately, there are a lot of techniques and a zoo of competing algorithms that you might need to experiment with to find the best approach for a given problem. (There are many books on optimization algorithms, and even a whole book can only cover a small slice of what is out there!) Some parting advice: Often the main trick is less about the choice of algorithms than it is about finding the right mathematical formulation of your problem-e.g. what function, what constraints, and what parameters should you be considering-to match your problem to a good algorithm. However, if you have many (≫10) parameters, try hard to use an analytical gradient (not finite differences), computed efficiently in reverse mode. There are many, many applications of optimization besides machine learning (fitting models to data). It is inter- esting to also consider engineering/physical optimization. (For instance, suppose you want to make an airplane wing that is as strong as possible.) The general outline of such problems is typically: 1. You start with some design parameters p, e.g. describing the geometry, materials, forces, or other degrees of freedom.

## Key terms
- **optimization** — 6 mentions
- **there** — 5 mentions
- **parameters** — 5 mentions
- **physical** — 5 mentions
- **model** — 5 mentions
- **problem** — 4 mentions
- **algorithm** — 4 mentions
- **design** — 4 mentions

## Practice — open in app
- [[pdf:Matrix Calculus.pdf#page=42|Matrix Calculus.pdf p. 42]]

## Liens
- Up: [[research/matrix-calculus/optimization]]
- ← Prev: [[research/matrix-calculus/nonlinear-optimization]]
- Document: [[research/matrix-calculus]]

#ml #math #calculus #backprop #research #section

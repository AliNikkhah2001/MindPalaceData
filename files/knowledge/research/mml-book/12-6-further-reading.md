---
title: "12.6 Further Reading"
summary: "§Part II Central Machine Learning Problems › 12 Classificatio: Classification with Support Vector Machines is an N by N matrix where the elements of the diagonal are from y, and X ∈RN×D is the matrix obtained by concatenating all the examples."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "398-400"
---

# 12.6 Further Reading

§Part II Central Machine Learning Problems › 12 Classification with Support Vector Machines › 12.6 Further Reading · pp. 398–400 · Mathematics for Machine Learning (MML Book)

## Extrait
Classification with Support Vector Machines is an N by N matrix where the elements of the diagonal are from y, and X ∈RN×D is the matrix obtained by concatenating all the examples. We can similarly perform a collection of terms for the dual version of the SVM (12.41). To express the dual SVM in standard form, we first have to express the kernel matrix K such that each entry is Kij = k(xi, xj). If we have an explicit feature representation xi then we define Kij = ⟨xi, xj⟩. For convenience of notation we introduce a matrix with zeros everywhere except on the diagonal, where we store the labels, that is, Y = diag(y). The dual SVM can be written as min α 2α⊤Y KY α −1⊤ N,1α subject to   y⊤ −y⊤ −IN IN  α ⩽ 0N+2,1 C1N,1  . (12.57) Remark. In Sections 7.3.1 and 7.3.2, we introduced the standard forms of the constraints to be inequality constraints. We will express the dual SVM’s equality constraint as two inequality constraints, i.e., Ax = b is replaced by Ax ⩽b and Ax ⩾b . (12.58) Particular software implementations of convex optimization methods may provide the ability to express equality constraints. ♢ Since there are many different possible views of the SVM, there are many approaches for solving the resulting optimization problem.

## Key terms
- **function** — 9 mentions
- **output** — 9 mentions
- **binary** — 8 mentions
- **approaches** — 7 mentions
- **classification** — 6 mentions
- **kernel** — 6 mentions
- **optimization** — 6 mentions
- **there** — 6 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=398|mml-book.pdf p. 398]]

## Liens
- Up: [[research/mml-book/12-classification-with-support-vector-machines]]
- ← Prev: [[research/mml-book/12-5-numerical-solution]]
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section

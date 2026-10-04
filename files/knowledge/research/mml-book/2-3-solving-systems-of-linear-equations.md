---
title: "2.3 Solving Systems of Linear Equations"
summary: "§Part I Mathematical Foundations › 2 Linear Algebra › 2.3 Sol: 2.3 Solving Systems of Linear Equations In (2.3), we introduced the general form of an equation system, i.e., a11x1 + · · · + a1nxn = b1 ..."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "33-40"
---

# 2.3 Solving Systems of Linear Equations

§Part I Mathematical Foundations › 2 Linear Algebra › 2.3 Solving Systems of Linear Equations · pp. 33–40 · Mathematics for Machine Learning (MML Book)

## Extrait
2.3 Solving Systems of Linear Equations In (2.3), we introduced the general form of an equation system, i.e., a11x1 + · · · + a1nxn = b1 ... am1x1 + · · · + amnxn = bm , (2.37) where aij ∈R and bi ∈R are known constants and xj are unknowns, i = 1, . . . , m, j = 1, . . . , n. Thus far, we saw that matrices can be used as a compact way of formulating systems of linear equations so that we can write Ax = b, see (2.10). Moreover, we defined basic matrix operations, such as addition and multiplication of matrices. In the following, we will focus on solving systems of linear equations and provide an algorithm for finding the inverse of a matrix. 2.3.1 Particular and General Solution Before discussing how to generally solve systems of linear equations, let us have a look at an example. Consider the system of equations 1 −4    x1 x2 x3 x4  = 42  . (2.38) The system has two equations and four unknowns. Therefore, in general we would expect infinitely many solutions. This system of equations is in a particularly easy form, where the first two columns consist of a 1 and a 0. Remember that we want to find scalars x1, . . . , x4, such that P4 i=1 xici = b, where we define ci to be the ith column of the matrix and b the right-hand-side of (2.38).

## Key terms
- **solution** — 32 mentions
- **system** — 25 mentions
- **form** — 19 mentions
- **matrix** — 15 mentions
- **linear** — 14 mentions
- **general** — 13 mentions
- **variable** — 11 mentions
- **particular** — 10 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=33|mml-book.pdf p. 33]]

## Liens
- Up: [[research/mml-book/2-linear-algebra]]
- ← Prev: [[research/mml-book/2-2-matrices]]
- Next: [[research/mml-book/2-4-vector-spaces]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section

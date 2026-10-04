---
title: "12.5 Numerical Solution"
summary: "§Part II Central Machine Learning Problems › 12 Classificatio: Classification with Support Vector Machines and Williams, 2006). Note that we are still solving for hyperplanes, that is, the hypothesis class of functions are still linear."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "396-397"
---

# 12.5 Numerical Solution

§Part II Central Machine Learning Problems › 12 Classification with Support Vector Machines › 12.5 Numerical Solution · pp. 396–397 · Mathematics for Machine Learning (MML Book)

## Extrait
Classification with Support Vector Machines and Williams, 2006). Figure 12.10 illustrates the effect of different kernels on separating hyperplanes on an example dataset. Note that we are still solving for hyperplanes, that is, the hypothesis class of functions are still linear. The non-linear surfaces are due to the kernel function. Remark. Unfortunately for the fledgling machine learner, there are multiple meanings of the word “kernel.” In this chapter, the word “kernel” comes from the idea of the reproducing kernel Hilbert space (RKHS) (Aronszajn, 1950; Saitoh, 1988). We have discussed the idea of the kernel in linear algebra (Section 2.7.3), where the kernel is another word for the null space. The third common use of the word “kernel” in machine learning is the smoothing kernel in kernel density estimation (Section 11.5). ♢ Since the explicit representation ϕ(x) is mathematically equivalent to the kernel representation k(xi, xj), a practitioner will often design the kernel function such that it can be computed more efficiently than the inner product between explicit feature maps. For example, consider the polynomial kernel (Sch¨olkopf and Smola, 2002), where the number of terms in the explicit expansion grows very quickly (even for polynomials of low degree) when the input dimension is large.

## Key terms
- **kernel** — 20 mentions
- **function** — 9 mentions
- **optimization** — 9 mentions
- **product** — 6 mentions
- **space** — 5 mentions
- **loss** — 5 mentions
- **problem** — 5 mentions
- **primal** — 5 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=396|mml-book.pdf p. 396]]

## Liens
- Up: [[research/mml-book/12-classification-with-support-vector-machines]]
- ← Prev: [[research/mml-book/12-4-kernels]]
- Next: [[research/mml-book/12-6-further-reading]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section

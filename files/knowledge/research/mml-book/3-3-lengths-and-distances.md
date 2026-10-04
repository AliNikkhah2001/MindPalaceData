---
title: "3.3 Lengths and Distances"
summary: "§Part I Mathematical Foundations › 3 Analytic Geometry › 3.3 : 3.3 Lengths and Distances In Section 3.1, we already discussed norms that we can use to compute the length of a vector. Inner products and norms are closely related in the sense that any inner product induces a norm I"
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "81-81"
---

# 3.3 Lengths and Distances

§Part I Mathematical Foundations › 3 Analytic Geometry › 3.3 Lengths and Distances · pp. 81–81 · Mathematics for Machine Learning (MML Book)

## Extrait
3.3 Lengths and Distances In Section 3.1, we already discussed norms that we can use to compute the length of a vector. Inner products and norms are closely related in the sense that any inner product induces a norm Inner products induce norms. ∥x∥:= q ⟨x, x⟩ (3.16) in a natural way, such that we can compute lengths of vectors using the inner product. However, not every norm is induced by an inner product. The Manhattan norm (3.3) is an example of a norm without a corresponding inner product. In the following, we will focus on norms that are induced by inner products and introduce geometric concepts, such as lengths, distances, and angles. Remark (Cauchy-Schwarz Inequality). For an inner product vector space (V, ⟨·, ·⟩) the induced norm ∥· ∥satisfies the Cauchy-Schwarz inequality Cauchy-Schwarz inequality | ⟨x, y⟩| ⩽∥x∥∥y∥. (3.17) ♢ Example 3.5 (Lengths of Vectors Using Inner Products) In geometry, we are often interested in lengths of vectors. We can now use an inner product to compute them using (3.16). Let us take x = [1, 1]⊤∈ R2. If we use the dot product as the inner product, with (3.16) we obtain ∥x∥= √ x⊤x = √ 12 + 12 = √ (3.18) as the length of x. Let us now choose a different inner product: ⟨x, y⟩:= x⊤  1 −1 −1  y = x1y1 −1 2(x1y2 + x2y1) + x2y2 .

## Key terms
- **product** — 22 mentions
- **inner** — 17 mentions
- **norm** — 10 mentions
- **distance** — 8 mentions
- **length** — 7 mentions
- **vector** — 6 mentions
- **compute** — 4 mentions
- **induced** — 3 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=81|mml-book.pdf p. 81]]

## Liens
- Up: [[research/mml-book/3-analytic-geometry]]
- ← Prev: [[research/mml-book/3-2-inner-products]]
- Next: [[research/mml-book/3-4-angles-and-orthogonality]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section

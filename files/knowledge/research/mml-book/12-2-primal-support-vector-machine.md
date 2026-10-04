---
title: "12.2 Primal Support Vector Machine"
summary: "§Part II Central Machine Learning Problems › 12 Classificatio: Classification with Support Vector Machines Figure 12.3 Possible separating hyperplanes. There are many linear classifiers (green lines) that separate orange crosses from blue discs."
level: "research"
series: "Mathematics for Machine Learning (MML Book)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [ml, math, foundations, book, section]
pages: "380-388"
---

# 12.2 Primal Support Vector Machine

§Part II Central Machine Learning Problems › 12 Classification with Support Vector Machines › 12.2 Primal Support Vector Machine · pp. 380–388 · Mathematics for Machine Learning (MML Book)

## Extrait
Classification with Support Vector Machines Figure 12.3 Possible separating hyperplanes. There are many linear classifiers (green lines) that separate orange crosses from blue discs. x(1) x(2) Based on the concept of distances from points to a hyperplane, we now are in a position to discuss the support vector machine. For a dataset {(x1, y1), . . . , (xN, yN)} that is linearly separable, we have infinitely many candidate hyperplanes (refer to Figure 12.3), and therefore classifiers, that solve our classification problem without any (training) errors. To find a unique solution, one idea is to choose the separating hyperplane that maximizes the margin between the positive and negative examples. In other words, we want the positive and negative examples to be separated by a large margin (Section 12.2.1). In the following, we compute the disA classifier with large margin turns out to generalize well (Steinwart and Christmann, 2008). tance between an example and a hyperplane to derive the margin. Recall that the closest point on the hyperplane to a given point (example xn) is obtained by the orthogonal projection (Section 3.8). 12.2.1 Concept of the Margin The concept of the margin is intuitively simple: It is the distance of the margin separating hyperplane to the closest examples in the dataset, assuming There could be two or more closest examples to a hyperplane.

## Key terms
- **hyperplane** — 31 mentions
- **margin** — 22 mentions
- **distance** — 18 mentions
- **vector** — 15 mentions
- **scale** — 7 mentions
- **machine** — 6 mentions
- **positive** — 6 mentions
- **negative** — 6 mentions

## Practice — open in app
- [[pdf:mml-book.pdf#page=380|mml-book.pdf p. 380]]

## Liens
- Up: [[research/mml-book/12-classification-with-support-vector-machines]]
- ← Prev: [[research/mml-book/12-1-separating-hyperplanes]]
- Next: [[research/mml-book/12-3-dual-support-vector-machine]] →
- Document: [[research/mml-book]]

#ml #math #foundations #book #research #section

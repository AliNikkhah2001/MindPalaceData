---
title: LIME (Local Interpretable Model-agnostic Explanations)
summary: Surrogate model explaining individual predictions by training an interpretable model locally around the prediction.
course: ML Research
tags: [xai, lime, interpretability]
book: SHAP.pdf
page: 2
read: false
---
# LIME (Local Interpretable Model-agnostic Explanations)

> **Source**: [[pdf:SHAP.pdf#page=2|SHAP.pdf (p. 2)]]

## Definition & Core Intuition
Surrogate model explaining individual predictions by training an interpretable model locally around the prediction.

## Mathematical Formulation
$$
\xi(x) = \arg\min_{g \in G} \mathcal{L}(f, g, \pi_x) + \Omega(g)
$$

## Connected Learning Assets
---
title: Shapley Values & Additive Feature Attribution
summary: Cooperative game theory solution distributing total payoff fairly among features according to marginal contributions.
course: ML Research
tags: [xai, shap, game-theory, interpretability]
book: SHAP.pdf
page: 3
read: false
---
# Shapley Values & Additive Feature Attribution

> **Source**: [[pdf:SHAP.pdf#page=3|SHAP.pdf (p. 3)]]

## Definition & Core Intuition
Cooperative game theory solution distributing total payoff fairly among features according to marginal contributions.

## Mathematical Formulation
$$
\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(|N|-|S|-1)!}{|N|!} (v(S \cup \{i\}) - v(S))
$$

## Connected Learning Assets

## Related Concepts
- [[concept:kernel-shap|Kernel Shap]]
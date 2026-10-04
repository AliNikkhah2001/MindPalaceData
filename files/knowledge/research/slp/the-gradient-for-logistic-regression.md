---
title: "The Gradient for Logistic Regression"
summary: "§I Large Language Models › Logistic Regression › Gradient Des: 4.6 • GRADIENT DESCENT Formally, then, the gradient of a multi-variable function f is a vector in which each component expresses the partial derivative of f with respect to one of the variables."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "83-83"
---

# The Gradient for Logistic Regression

§I Large Language Models › Logistic Regression › Gradient Descent › The Gradient for Logistic Regression · pp. 83–83 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.6 • GRADIENT DESCENT Formally, then, the gradient of a multi-variable function f is a vector in which each component expresses the partial derivative of f with respect to one of the variables. We’ll use the inverted Greek delta symbol ∇to refer to the gradient, and represent ˆy as f(x;θ) to make the dependence on θ more obvious: ∇L(f(x;θ),y) =   ∂ ∂w1 L(f(x;θ),y) ∂ ∂w2 L(f(x;θ),y) ... ∂ ∂wn L(f(x;θ),y) ∂ ∂bL(f(x;θ),y)   (4.23) The final equation for updating θ based on the gradient is thus θt+1 = θt −η∇L(f(x;θ),y) (4.24) In order to update θ, we need a definition for the gradient ∇L(f(x;θ),y). Recall that for logistic regression, the cross-entropy loss function is: LCE(ˆy,y) = −[ylogσ(w ·x+b)+(1−y)log(1−σ(w ·x+b))] (4.25) It turns out that the derivative of this function for one observation vector x is Eq. 4.26 (the interested reader can see Section 4.15 for the derivation of this equation): ∂LCE(ˆy,y) ∂w j = [σ(w ·x+b)−y]xj = (ˆy−y)xj (4.26) You’ll also sometimes see this equation in the equivalent form: ∂LCE(ˆy,y) ∂w j = −(y−ˆy)xj (4.27) Note in these equations that the gradient with respect to a single weight w j represents a very intuitive value: the difference between the true y and our estimated ˆy = σ(w · x + b) for that observation, multiplied by the corresponding input value x j.

## Key terms
- **gradient** — 10 mentions
- **function** — 4 mentions
- **descent** — 3 mentions
- **derivative** — 3 mentions
- **respect** — 3 mentions
- **input** — 3 mentions
- **stochastic** — 3 mentions
- **vector** — 2 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=83|Speech and Language Processing.pdf p. 83]]

## Liens
- Up: [[research/slp/gradient-descent]]
- Next: [[research/slp/the-stochastic-gradient-descent-algorithm]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

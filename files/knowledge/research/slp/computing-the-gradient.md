---
title: "Computing the Gradient"
summary: "§I Large Language Models › Neural Networks › Training Neural : Let’s briefly summarize the explanation here for convenience. First, when we have more than 2 classes we’ll need to represent both y and ˆy as vectors."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "146-146"
---

# Computing the Gradient

§I Large Language Models › Neural Networks › Training Neural Nets › Computing the Gradient · pp. 146–146 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 6 • NEURAL NETWORKS page 82. Let’s briefly summarize the explanation here for convenience. First, when we have more than 2 classes we’ll need to represent both y and ˆy as vectors. Let’s assume we’re doing hard classification, where only one class is the correct one. The true label y is then a vector with K elements, each corresponding to a class, with yc = 1 if the correct class is c, with all other elements of y being 0. Recall that a vector like this, with one value equal to 1 and the rest 0, is called a one-hot vector. And our classifier will produce an estimate vector with K elements ˆy, each element ˆyk of which represents the estimated probability p(yk = 1|x). The loss function for a single example x is the negative sum of the logs of the K output classes, each weighted by their probability yk: LCE(ˆy,y) = − K X k=1 yk log ˆyk (6.26) We can simplify this equation further; let’s first rewrite the equation using the function 1{} which evaluates to 1 if the condition in the brackets is true and to 0 otherwise. This makes it more obvious that the terms in the sum in Eq. 6.26 will be 0 except for the term corresponding to the true class for which yk = 1: LCE(ˆy,y) = − K X…

## Key terms
- **probability** — 10 mentions
- **loss** — 9 mentions
- **negative** — 9 mentions
- **class** — 8 mentions
- **correct** — 8 mentions
- **classes** — 7 mentions
- **vector** — 6 mentions
- **classifier** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=146|Speech and Language Processing.pdf p. 146]]

## Liens
- Up: [[research/slp/training-neural-nets]]
- ← Prev: [[research/slp/loss-function]]
- Next: [[research/slp/computation-graphs]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

---
title: "Evaluating Parsers"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: 18.8 • EVALUATING PARSERS And we can choose the final parse tree as the tree with the maximum score: ˆT = argmax T s(T) (18.9) The simplest method to produce the most likely parse is to greedily choose the highest sco"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "433-433"
---

# Evaluating Parsers

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › Evaluating Parsers · pp. 433–433 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
18.8 • EVALUATING PARSERS And we can choose the final parse tree as the tree with the maximum score: ˆT = argmax T s(T) (18.9) The simplest method to produce the most likely parse is to greedily choose the highest scoring label for each span. This greedy method is not guaranteed to produce a tree, since the best label for a span might not fit into a complete tree. In practice, however, the greedy method tends to find trees; in their experiments Gaddy et al. (2018) finds that 95% of predicted bracketings form valid trees. Nonetheless it is more common to use a variant of the CKY algorithm to find the full parse. The variant defined in Gaddy et al. (2018) works as follows. Let’s define sbest(i, j) as the score of the best subtree spanning (i, j). For spans of length one, we choose the best label: sbest(i,i+1) = max l s(i,i+1,l) (18.10) For other spans (i, j), the recursion is: sbest(i, j) = max l s(i, j,l) + max k [sbest(i,k)+sbest(k, j)] (18.11) Note that the parser is using the max label for span (i, j) + the max labels for spans (i,k) and (k, j) without worrying about whether those decisions make sense given a grammar. The role of the grammar in classical parsing is to help constrain possible combinations of constituents (NPs like to be followed by VPs).

## Key terms
- **parse** — 14 mentions
- **tree** — 9 mentions
- **constituent** — 9 mentions
- **span** — 7 mentions
- **label** — 5 mentions
- **sbest** — 5 mentions
- **hypothesis** — 5 mentions
- **reference** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=433|Speech and Language Processing.pdf p. 433]]

## Liens
- Up: [[research/slp/context-free-grammars-and-constituency-parsing]]
- ← Prev: [[research/slp/span-based-neural-constituency-parsing]]
- Next: [[research/slp/heads-and-head-finding]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

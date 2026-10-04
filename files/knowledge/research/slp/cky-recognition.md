---
title: "CKY Recognition"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING is a non-unit production in our grammar, then we add A →γ for each such rule in the grammar and discard all the intervening unit productions."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "426-427"
---

# CKY Recognition

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › CKY Parsing: A Dynamic Programming Approach › CKY Recognition · pp. 426–427 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING is a non-unit production in our grammar, then we add A →γ for each such rule in the grammar and discard all the intervening unit productions. As we demonstrate with our toy grammar, this can lead to a substantial flattening of the grammar and a consequent promotion of terminals to fairly high levels in the resulting trees. Rules with right-hand sides longer than 2 are normalized through the introduction of new non-terminals that spread the longer sequences over several new rules. Formally, if we have a rule like A →B C γ we replace the leftmost pair of non-terminals with a new non-terminal and introduce a new production, resulting in the following new rules: A →X1 γ X1 →B C In the case of longer right-hand sides, we simply iterate this process until the offending rule has been replaced by rules of length 2. The choice of replacing the leftmost pair of non-terminals is purely arbitrary; any systematic scheme that results in binary rules would suffice. In our current grammar, the rule S →Aux NP VP would be replaced by the two rules S →X1 VP and X1 →Aux NP. The entire conversion process can be summarized as follows: 1. Copy all conforming rules to the new grammar unchanged.

## Key terms
- **rule** — 16 mentions
- **grammar** — 14 mentions
- **nominal** — 12 mentions
- **verb** — 10 mentions
- **non-terminal** — 8 mentions
- **cell** — 8 mentions
- **matrix** — 7 mentions
- **input** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=426|Speech and Language Processing.pdf p. 426]]

## Liens
- Up: [[research/slp/cky-parsing-a-dynamic-programming-approach]]
- ← Prev: [[research/slp/conversion-to-chomsky-normal-form]]
- Next: [[research/slp/cky-parsing]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

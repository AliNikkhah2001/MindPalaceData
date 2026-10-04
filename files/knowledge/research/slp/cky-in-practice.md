---
title: "CKY in Practice"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: 18.6 • CKY PARSING: A DYNAMIC PROGRAMMING APPROACH ... [0,n] [i,i+1] [i,i+2] [i,j-2] [i,j-1] [i+1,j] [i+2,j] [j-1,j] [j-2,j] [i,j] ..."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "429-430"
---

# CKY in Practice

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › CKY Parsing: A Dynamic Programming Approach › CKY in Practice · pp. 429–430 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
18.6 • CKY PARSING: A DYNAMIC PROGRAMMING APPROACH ... ... [0,n] [i,i+1] [i,i+2] [i,j-2] [i,j-1] [i+1,j] [i+2,j] [j-1,j] [j-2,j] [i,j] ... [0,1] [n-1, n] Figure 18.13 All the ways to fill the [i, j]th cell in the CKY table. parse consists of choosing an S from cell [0,n] and then recursively retrieving its component constituents from the table. Of course, instead of returning every parse for a sentence, we usually want just the best parse; we’ll see how to do that in the next section. Finally, we should note that while the restriction to CNF does not pose a problem theoretically, it does pose some non-trivial problems in practice. The returned CNF trees may not be consistent with the original grammar built by the grammar developers, and will complicate any syntax-driven approach to semantic analysis. One approach to getting around these problems is to keep enough information around to transform our trees back to the original grammar as a post-processing step of the parse. This is trivial in the case of the transformation used for rules with length greater than 2. Simply deleting the new dummy non-terminals and promoting their daughters restores the original tree. In the case of unit productions, it turns out to be more convenient to alter the basic CKY algorithm to handle them directly than it is to store the information needed to recover the correct trees.

## Key terms
- **nominal** — 14 mentions
- **noun** — 10 mentions
- **houston** — 6 mentions
- **book** — 5 mentions
- **flight** — 5 mentions
- **through** — 5 mentions
- **verb** — 5 mentions
- **prep** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=429|Speech and Language Processing.pdf p. 429]]

## Liens
- Up: [[research/slp/cky-parsing-a-dynamic-programming-approach]]
- ← Prev: [[research/slp/cky-parsing]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

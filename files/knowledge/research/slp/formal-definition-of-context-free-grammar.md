---
title: "Formal Definition of Context-Free Grammar"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING language models generating text.) We conclude this section with a quick, formal description of a context-free grammar and the language it generates."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "420-420"
---

# Formal Definition of Context-Free Grammar

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › Context-Free Grammars › Formal Definition of Context-Free Grammar · pp. 420–420 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING language models generating text.) We conclude this section with a quick, formal description of a context-free grammar and the language it generates. A context-free grammar G is defined by four parameters: N, Σ, R, S (technically it is a “4-tuple”). N a set of non-terminal symbols (or variables) Σ a set of terminal symbols (disjoint from N) R a set of rules or productions, each of the form A →β , where A is a non-terminal, β is a string of symbols from the infinite set of strings (Σ∪N)∗ S a designated start symbol and a member of N For the remainder of the book we adhere to the following conventions when discussing the formal properties of context-free grammars (as opposed to explaining particular facts about English or other languages). Capital letters like A, B, and S Non-terminals S The start symbol Lower-case Greek letters like α, β, and γ Strings drawn from (Σ∪N)∗ Lower-case Roman letters like u, v, and w Strings of terminals A language is defined through the concept of derivation. One string derives another one if it can be rewritten as the second one by some series of rule applications. More formally, following Hopcroft and Ullman (1979), if A →β is a production of R and α and γ are any strings in the set (Σ∪N)∗, then we say that αAγ directly derives αβγ, or αAγ ⇒αβγ.

## Key terms
- **string** — 9 mentions
- **symbol** — 7 mentions
- **language** — 5 mentions
- **grammar** — 5 mentions
- **derives** — 5 mentions
- **context-free** — 4 mentions
- **parsing** — 3 mentions
- **non-terminal** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=420|Speech and Language Processing.pdf p. 420]]

## Liens
- Up: [[research/slp/context-free-grammars]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

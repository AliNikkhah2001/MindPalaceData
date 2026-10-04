---
title: "Grammar Equivalence and Normal Form"
summary: "§II Annotating Linguistic Structure › Context-Free Grammars a: CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING Grammar Lexicon S →NP VP . DT →the | that S →NP VP JJ →cold | empty | full NP →CD RB NN →sky | fire | light | flight | tomorrow NP →DT NN CC →and NP →NN CC N"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "422-422"
---

# Grammar Equivalence and Normal Form

§II Annotating Linguistic Structure › Context-Free Grammars and Constituency Parsing › Grammar Equivalence and Normal Form · pp. 422–422 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING Grammar Lexicon S →NP VP . DT →the | that S →NP VP JJ →cold | empty | full NP →CD RB NN →sky | fire | light | flight | tomorrow NP →DT NN CC →and NP →NN CC NN IN →of | at NP →DT JJ , JJ NN CD →eleven NP →NN RB →a.m. VP →MD VP VB →arrive VP →VBD ADJP VBD →was | said VP →MD VP MD →should | would VP →VB PP NP ADJP →JJ PP PP →IN NP Figure 18.7 CFG grammar rules and lexicon from the treebank sentences in Fig. 18.5. among the approximately 4,500 different rules for expanding VPs are separate rules for PP sequences of any length and every possible arrangement of verb arguments: VP →VBD PP VP →VBD PP PP VP →VBD PP PP PP VP →VBD PP PP PP PP VP →VB ADVP PP VP →VB PP ADVP VP →ADVP VB PP A formal language is defined as a (possibly infinite) set of strings of words. This suggests that we could ask if two grammars are equivalent by asking if they generate the same set of strings. In fact, it is possible to have two distinct context-free grammars generate the same language. We say that two grammars are strongly equivalent if strongly equivalent they generate the same set of strings and if they assign the same phrase structure to each sentence (allowing merely for renaming of the non-terminal symbols).

## Key terms
- **grammar** — 12 mentions
- **form** — 9 mentions
- **equivalent** — 6 mentions
- **normal** — 6 mentions
- **rule** — 6 mentions
- **chomsky** — 5 mentions
- **context-free** — 4 mentions
- **strings** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=422|Speech and Language Processing.pdf p. 422]]

## Liens
- Up: [[research/slp/context-free-grammars-and-constituency-parsing]]
- ← Prev: [[research/slp/treebanks]]
- Next: [[research/slp/ambiguity]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

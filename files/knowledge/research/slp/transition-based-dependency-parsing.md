---
title: "Transition-Based Dependency Parsing"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Tr: CHAPTER 19 • DEPENDENCY PARSING ADV PRON NOUN ADV VERB VERB NOUN 但 我 昨天 才 收 到 信 but I yesterday only-then receive arrive letter ."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "444-452"
---

# Transition-Based Dependency Parsing

§II Annotating Linguistic Structure › Dependency Parsing › Transition-Based Dependency Parsing · pp. 444–452 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 19 • DEPENDENCY PARSING ADV PRON NOUN ADV VERB VERB NOUN 但 我 昨天 才 收 到 信 but I yesterday only-then receive arrive letter . adv nsubj obj:tmod advmod compound:vv obj [Chinese] 但我昨天才收到信“But I didn’t receive the letter until yesterday”(19.6) Our first approach to dependency parsing is called transition-based parsing. This transition-based architecture draws on shift-reduce parsing, a paradigm originally developed for analyzing programming languages (Aho and Ullman, 1972). In transition-based parsing we’ll have a stack on which we build the parse, a buffer of tokens to be parsed, and a parser which takes actions on the parse via a predictor called an oracle, as illustrated in Fig. 19.4. wn w1 w2 s2 ... s1 sn Parser Input buffer Stack Oracle LEFTARC RIGHTARC SHIFT Action Dependency Relations w3 w2 Figure 19.4 Basic transition-based parser. The parser examines the top two elements of the stack and selects an action by consulting an oracle that examines the current configuration. The parser walks through the sentence left-to-right, successively shifting items from the buffer onto the stack. At each time point we examine the top two elements on the stack, and the oracle makes a decision about what transition to apply to build the parse.

## Key terms
- **stack** — 31 mentions
- **word** — 29 mentions
- **operator** — 23 mentions
- **root** — 23 mentions
- **book** — 23 mentions
- **configuration** — 21 mentions
- **relation** — 19 mentions
- **flight** — 19 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=444|Speech and Language Processing.pdf p. 444]]

## Liens
- Up: [[research/slp/dependency-parsing]]
- ← Prev: [[research/slp/dependency-relations]]
- Next: [[research/slp/graph-based-dependency-parsing]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

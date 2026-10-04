---
title: "Rule-based tokenization"
summary: "§I Large Language Models › Words and Tokens › Rule-based toke: Alternatively, we can collapse all the upper case to lower case: tr -sc ’A-Za-z’ ’\n’ < sh.txt | tr A-Z a-z | sort | uniq -c whose output is 14725 a 97 aaron 1 abaissiez 10 abandon 2 abandoned 2 abase 1 abash 14 abate"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "36-37"
---

# Rule-based tokenization

§I Large Language Models › Words and Tokens › Rule-based tokenization · pp. 36–37 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS 1945 A ... Alternatively, we can collapse all the upper case to lower case: tr -sc ’A-Za-z’ ’\n’ < sh.txt | tr A-Z a-z | sort | uniq -c whose output is 14725 a 97 aaron 1 abaissiez 10 abandon 2 abandoned 2 abase 1 abash 14 abate ... Now we can sort again to find the frequent words. The -n option to sort means to sort numerically rather than alphabetically, and the -r option means to sort in reverse order (highest-to-lowest): tr -sc ’A-Za-z’ ’\n’ < sh.txt | tr A-Z a-z | sort | uniq -c | sort -n -r The results show that the most frequent words in Shakespeare, as in any other corpus, are the short function words like articles, pronouns, prepositions: 27378 the 26084 and 22538 i 19771 to 17481 of 14725 a 13826 you ... Unix tools of this sort can be very handy in building quick word count statistics for any corpus in English. For anything more complex, we generally turn to the more sophisticated tokenization algorithms we’ve discussed above. While data-based tokenization like BPE is the most common way of doing tokenization, there are also situations where we want to constrain our tokens to be words and not subwords. This might be useful if we are running parsing algorithms for English where the parser might need grammatical words as input.

## Key terms
- **word** — 15 mentions
- **tokenization** — 14 mentions
- **sort** — 9 mentions
- **token** — 8 mentions
- **english** — 7 mentions
- **useful** — 6 mentions
- **algorithms** — 5 mentions
- **rule-based** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=36|Speech and Language Processing.pdf p. 36]]

## Liens
- Up: [[research/slp/words-and-tokens]]
- ← Prev: [[research/slp/simple-unix-tools-for-word-tokenization]]
- Next: [[research/slp/minimum-edit-distance]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

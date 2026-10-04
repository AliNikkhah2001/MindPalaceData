---
title: "Extracting Temporal Expressions"
summary: "§II Annotating Linguistic Structure › Information Extraction:: CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME <TIMEX3 tid=t57 type=DATE value=1989-10-26 functionInDocument=CREATION_TIME> 10/26/89 </TIMEX3> Delta Air Lines earnings <EVENT eid=e1 class="
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "480-480"
---

# Extracting Temporal Expressions

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Automatic Temporal Analysis › Extracting Temporal Expressions · pp. 480–480 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME <TIMEX3 tid="t57" type="DATE" value="1989-10-26" functionInDocument="CREATION_TIME"> 10/26/89 </TIMEX3> Delta Air Lines earnings <EVENT eid="e1" class="OCCURRENCE"> soared </EVENT> 33% to a record in <TIMEX3 tid="t58" type="DATE" value="1989-Q1" anchorTimeID="t57"> the fiscal first quarter </TIMEX3>, <EVENT eid="e3" class="OCCURRENCE">bucking</EVENT> the industry trend toward <EVENT eid="e4" class="OCCURRENCE">declining</EVENT> profits. Figure 20.13 Example from the TimeBank corpus. • Declininge4 includes soaringe1 We can also visualize the links as a graph. The TimeBank snippet in Eq. 20.35 would be represented with a graph like Fig. 20.14. (20.35) [DCT:11/02/891]1: Pacific First Financial Corp. said2 shareholders approved3 its acquisition4 by Royal Trustco Ltd. of Toronto for $27 a share, or $212 million. The thrift holding company said5 it expects6 to obtain7 regulatory approval8 and complete9 the transaction10 by year-end11. BEFORE BEFORE AFTER SIMULTANEOUS ENDS CULMINATES BEFORE EVIDENTIAL MODAL FACTIVE MODAL EVIDENTIAL MODAL Figure 20.14 A graph of the text in Eq. 20.35, adapted from (Ocal et al., 2022). TLINKS are shown in blue, ALINKS in red, and SLINKS in green.

## Key terms
- **time** — 10 mentions
- **event** — 8 mentions
- **temporal** — 7 mentions
- **expressions** — 6 mentions
- **timex3** — 4 mentions
- **graph** — 4 mentions
- **date** — 3 mentions
- **class** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=480|Speech and Language Processing.pdf p. 480]]

## Liens
- Up: [[research/slp/automatic-temporal-analysis]]
- Next: [[research/slp/temporal-normalization]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

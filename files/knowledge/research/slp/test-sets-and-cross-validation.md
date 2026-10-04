---
title: "Test sets and Cross-validation"
summary: "§I Large Language Models › Logistic Regression › Test sets an: 4.10 • TEST SETS AND CROSS-VALIDATION urgent normal gold labels system output recallu = 8+5+3 precisionu= 8+10+1 spam urgent normal spam recalln = recalls = precisionn= 5+60+50 precisions= 3+30+200 10+60+30 1+50+200 F"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "93-93"
---

# Test sets and Cross-validation

§I Large Language Models › Logistic Regression › Test sets and Cross-validation · pp. 93–93 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
4.10 • TEST SETS AND CROSS-VALIDATION urgent normal gold labels system output recallu = 8+5+3 precisionu= 8+10+1 spam urgent normal spam recalln = recalls = precisionn= 5+60+50 precisions= 3+30+200 10+60+30 1+50+200 Figure 4.8 Confusion matrix for a three-class categorization task, showing for each pair of classes (c1,c2), how many documents from c1 were (in)correctly assigned to c2. The matrix shows, for example, that the system mistakenly labeled one spam document as urgent, and we have shown how to compute a distinct precision and recall value for each class. In order to derive a single metric that tells us how well the system is doing, we can combine these values in two ways. In macroaveraging, macroaveraging we compute the performance for each class, and then average over classes. In microaveraging, we collect the decisions for all classes into a single confusion matrix, microaveraging and then compute precision and recall from that table. Fig. 4.9 shows the confusion matrix for each class separately, and shows the computation of microaveraged and macroaveraged precision. true urgent true not system urgent system not true normal true not system normal system not true spam true…

## Key terms
- **system** — 11 mentions
- **precision** — 10 mentions
- **true** — 8 mentions
- **spam** — 7 mentions
- **class** — 7 mentions
- **urgent** — 6 mentions
- **classes** — 6 mentions
- **normal** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=93|Speech and Language Processing.pdf p. 93]]

## Liens
- Up: [[research/slp/logistic-regression]]
- ← Prev: [[research/slp/evaluation-precision-recall-f-measure]]
- Next: [[research/slp/statistical-significance-testing]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

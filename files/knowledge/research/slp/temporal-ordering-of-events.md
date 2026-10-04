---
title: "Temporal Ordering of Events"
summary: "§II Annotating Linguistic Structure › Information Extraction:: 20.7 • AUTOMATIC TEMPORAL ANALYSIS to as the document’s temporal anchor. The values of temporal expressions such temporal anchor as today, yesterday, or tomorrow can all be computed with respect to this temporal ancho"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "483-483"
---

# Temporal Ordering of Events

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Automatic Temporal Analysis › Temporal Ordering of Events · pp. 483–483 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
20.7 • AUTOMATIC TEMPORAL ANALYSIS to as the document’s temporal anchor. The values of temporal expressions such temporal anchor as today, yesterday, or tomorrow can all be computed with respect to this temporal anchor. The semantic procedure for today simply assigns the anchor, and the attachments for tomorrow and yesterday add a day and subtract a day from the anchor, respectively. Of course, given the cyclic nature of our representations for months, weeks, days, and times of day, our temporal arithmetic procedures must use modulo arithmetic appropriate to the time unit being used. Unfortunately, even simple expressions such as the weekend or Wednesday introduce a fair amount of complexity. In our current example, the weekend clearly refers to the weekend of the week that immediately precedes the document date. But this won’t always be the case, as is illustrated in the following example. (20.38) Random security checks that began yesterday at Sky Harbor will continue at least through the weekend. In this case, the expression the weekend refers to the weekend of the week that the anchoring date is part of (i.e., the coming weekend). The information that signals this meaning comes from the tense of continue, the verb governing the weekend.

## Key terms
- **temporal** — 14 mentions
- **expression** — 11 mentions
- **time** — 10 mentions
- **event** — 9 mentions
- **weekend** — 8 mentions
- **week** — 8 mentions
- **anchor** — 5 mentions
- **date** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=483|Speech and Language Processing.pdf p. 483]]

## Liens
- Up: [[research/slp/automatic-temporal-analysis]]
- ← Prev: [[research/slp/temporal-normalization]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

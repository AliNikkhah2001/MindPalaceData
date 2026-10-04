---
title: "Training Large Language Models"
summary: "§I Large Language Models › Large Language Models › Training L: CHAPTER 7 • LARGE LANGUAGE MODELS That is, normally we convert from logits to softmax as shown in Fig. But when we use a temperature parameter we first scale the logit as in Fig."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "166-170"
---

# Training Large Language Models

§I Large Language Models › Large Language Models › Training Large Language Models · pp. 166–170 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 7 • LARGE LANGUAGE MODELS That is, normally we convert from logits to softmax as shown in Fig. 7.10(a). But when we use a temperature parameter we first scale the logit as in Fig. 7.10(b). a b c d logits probabilities … MxFIXv1Pf4qrp0M1iEuikzIupSdONSwT6wU0omvVODmQfJHbEM8xPduPN3uHGhaPoQ1NoLIYfz3UuSkyCVQpPrvlilufmFxaXlFXt1bX1js7y13dBJpjWeSIT1QqYRilirJMgia1UIYsCic3g/mLImw+otEjiGxqk2IlYPxah4IyM1S3/VAxnvuEj5TjY1pU2UGR3xa+b0+RYCbhM0lvQrliltzR+VMC28iKjCpq2752e8lPIswJi6Z1m3PTamTM0WCSyxsP9OYMn7P+tg2MmYR6k4+CqRw9o3Tc8JEmRWTM3J/TuQs0noQBaYzYnSn/7Kh+R9rZxSednIRpxlhzMcHhZl0KHG6To9oZCTHBjBuBLmrg6/YyYTMn9gmxC8v0+eFo3DmndcO74+qpydT+JYhl3Ygyp4cAJncAlXUAcOT/AK7/BhPVtv1mfJGrd+7ADv6pkfwHMyrcq</latexit>exp(a) Z exp(b) Z exp(c) Z exp(d) Z … where Z = exp(a) +exp(b) +exp(c) +exp(d) +... u y a b c d logits probabilities … with temperature … where 8eiWumFgcP57uXOnPETwRU6zqdhbmxubReKO6Xdvf2DQ6t81FZxKhm0WCxi2fWpAsEjaCFHAd1EAg19AR1/9DlnXeQisfRM04S6If0NeIBZxS1NbAyL5CUZR7CGDMYJ/kFvfKQpd59pJ7XmkF+sxW4+Hy3hgVZ2aMyt7VbgLUSWLag6sD28YszSECJmgSvVcJ8F+RiVyJiAveamChLIRfYWelhENQfWzWUi5fa6doR3EUp8I7Zm7PJHRUKlJ6OvOkOKb+sum5n+sl2Jw1894lKQIEZsvClJhY2xPE7eHXAJDMdGCMsn1XW32RnUwqP+lpENw/z5VbSva269Vn+6qTbuF3EUyQk5IxfEJbekQR5Jk7QI19GwbCMsvFt7pkV83jeahqLmQr5VebpD24juks=</latexit>exp(a/⌧) Z exp(b/⌧) Z exp(c/⌧) Z exp(d/⌧) Z Z = exp(a/⌧) +exp(b/⌧) +exp(c/⌧) +exp(d/⌧) +...

## Key terms
- **model** — 36 mentions
- **token** — 22 mentions
- **word** — 21 mentions
- **next** — 20 mentions
- **loss** — 19 mentions
- **language** — 18 mentions
- **probability** — 18 mentions
- **temperature** — 14 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=166|Speech and Language Processing.pdf p. 166]]

## Liens
- Up: [[research/slp/large-language-models]]
- ← Prev: [[research/slp/generation-and-sampling]]
- Next: [[research/slp/evaluating-large-language-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

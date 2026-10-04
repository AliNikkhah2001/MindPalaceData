---
title: "Learning from Preferences"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE appropriate metric for the held-out evaluation."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "232-235"
---

# Learning from Preferences

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › Learning from Preferences · pp. 232–235 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE appropriate metric for the held-out evaluation. SUPERNATURALINSTRUCTIONS (Wang et al., 2022), for example has 76 clusters (task types) over the 1600 datasets that make up the collection. Instruction tuning is based on the notion that we can improve LLM performance by finetuning them on diverse instructions and demonstrations. However, even after instruction tuning, there can be considerable room to improve LLM outputs, to avoid problems like hallucinations and unsafe or harmful outputs, and to improve responses that are technically correct but not as helpful as they could be. The goal of preference-based learning is to use preference judgments to further preference- based learning improve the performance of finetuned LLMs, in terms of general performance and also specifically with respect to qualities like honesty, helpfulness, and harmlessness. Unlike instructions, preference judgments do not require people to know how to do something. We simply have to have an opinion about the end result. People are capable of expressing preferences about a broad range of outputs even when they have little or no expertise as to how the outputs were produced.

## Key terms
- **preference** — 36 mentions
- **output** — 27 mentions
- **model** — 16 mentions
- **pair** — 14 mentions
- **judgments** — 12 mentions
- **prompt** — 11 mentions
- **annotator** — 10 mentions
- **score** — 10 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=232|Speech and Language Processing.pdf p. 232]]

## Liens
- Up: [[research/slp/post-training-instruction-tuning-alignment-and-test-time-compute]]
- ← Prev: [[research/slp/instruction-tuning]]
- Next: [[research/slp/llm-alignment-via-preference-based-learning]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

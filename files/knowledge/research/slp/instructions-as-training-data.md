---
title: "Instructions as Training Data"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE Pretrained LLM Continue training all parameters on finetuning domain Finetuning Inference Pretraining On finetuning domain Finetuning as"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "228-230"
---

# Instructions as Training Data

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › Instruction Tuning › Instructions as Training Data · pp. 228–230 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE Pretrained LLM Continue training all parameters on finetuning domain Finetuning Inference Pretraining On finetuning domain Finetuning as Continued Pretraining Parameter Efficient Finetuning (e.g., LoRA) Pretrained LLM A B Pretrained LLM MLM Finetuning … … … … … … … Instruction Tuning (SFT) On finetuning domain On finetuning task On unseen tasks Next word prediction objective Data from finetuning domain Train only new parameters on domain Next word prediction objective Data from finetuning domain Train only classification head on finetuning task Task specific loss Supervised data from task Instruction tuning on diverse tasks Next word prediction objective Supervised instructions + … Figure 10.1 Instruction tuning compared to the other kinds of finetuning. tion (e.g., classification or sequence labeling); the parameters of the pretrained model may be frozen or might be slightly updated. Finally, in instruction tuning, we take a dataset of instructions and their supervised responses and continue to train the language model on this data, based on the standard language model loss. Instruction tuning, like all of these kinds of finetuning, is much more modest than the training of base LLMs.

## Key terms
- **instruction** — 25 mentions
- **task** — 19 mentions
- **finetuning** — 15 mentions
- **language** — 14 mentions
- **question** — 13 mentions
- **data** — 11 mentions
- **dataset** — 11 mentions
- **tuning** — 10 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=228|Speech and Language Processing.pdf p. 228]]

## Liens
- Up: [[research/slp/instruction-tuning]]
- Next: [[research/slp/evaluation-of-instruction-tuned-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

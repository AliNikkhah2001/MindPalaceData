---
title: "In-Context Learning and Induction Heads"
summary: "§I Large Language Models › Transformers › Interpreting the Tr: CHAPTER 8 • TRANSFORMERS h Pretrained Weights W k d r d A B r x d d k × Figure 8.19 The intuition of LoRA. We freeze W to its pretrained values, and instead finetune by training a pair of matrices A and B, updating th"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "204-204"
---

# In-Context Learning and Induction Heads

§I Large Language Models › Transformers › Interpreting the Transformer › In-Context Learning and Induction Heads · pp. 204–204 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 8 • TRANSFORMERS h Pretrained Weights W k d r d A B r x d d k × Figure 8.19 The intuition of LoRA. We freeze W to its pretrained values, and instead finetune by training a pair of matrices A and B, updating those instead of W, and just sum W and the updated AB. How does a transformer-based language model manage to do so well at language tasks? The subfield of interpretability, sometimes called mechanistic interpretabilinterpretability ity, focuses on ways to understand mechanistically what is going on inside the transformer. In the next two subsections we discuss two well-studied aspects of transformer interpretability. As a way of getting a model to do what we want, we can think of prompting as being fundamentally different than pretraining. Learning via pretraining means updating the model’s parameters by using gradient descent according to some loss function. But prompting with demonstrations can teach a model to do a new task. The model is learning something about the task from those demonstrations as it processes the prompt. Even without demonstrations, we can think of the process of prompting as a kind of learning. For example, the further a model gets in a prompt, the better it tends to get at predicting the upcoming tokens.

## Key terms
- **model** — 10 mentions
- **learning** — 8 mentions
- **language** — 4 mentions
- **task** — 4 mentions
- **in-context** — 4 mentions
- **transformer** — 3 mentions
- **prompting** — 3 mentions
- **demonstrations** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=204|Speech and Language Processing.pdf p. 204]]

## Liens
- Up: [[research/slp/interpreting-the-transformer]]
- Next: [[research/slp/logit-lens]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

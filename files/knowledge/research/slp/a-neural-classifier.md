---
title: "A neural classifier"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Tr: CHAPTER 19 • DEPENDENCY PARSING The correct transition here is SHIFT (you should convince yourself of this before proceeding)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "450-450"
---

# A neural classifier

§II Annotating Linguistic Structure › Dependency Parsing › Transition-Based Dependency Parsing › A neural classifier · pp. 450–450 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 19 • DEPENDENCY PARSING The correct transition here is SHIFT (you should convince yourself of this before proceeding). The application of our set of feature templates to this configuration would result in the following set of instantiated features. ⟨s1.w = flights,op = shift⟩ (19.11) ⟨s2.w = canceled,op = shift⟩ ⟨s1.t = NNS,op = shift⟩ ⟨s2.t = VBD,op = shift⟩ ⟨b1.w = to,op = shift⟩ ⟨b1.t = TO,op = shift⟩ ⟨s1.wt = flightsNNS,op = shift⟩ Given that the left and right arc transitions operate on the top two elements of the stack, features that combine properties from these positions are even more useful. For example, a feature like s1.t ◦s2.t concatenates the part of speech tag of the word at the top of the stack with the tag of the word beneath it. ⟨s1.t ◦s2.t = NNSVBD,op = shift⟩ (19.12) Given the training data and features, any classifier, like multinomial logistic regression or support vector machines, can be used. The oracle can also be implemented by a neural classifier. A standard architecture is simply to pass the sentence through an encoder, then take the presentation of the top 2 words on the stack and the first word of the buffer, concatenate them, and present to a feedforward network that predicts the transition to take (Kiperwasser and Goldberg, 2016; Kulmizev et al., 2019).

## Key terms
- **shift** — 10 mentions
- **word** — 6 mentions
- **feature** — 5 mentions
- **stack** — 5 mentions
- **transition** — 4 mentions
- **parser** — 4 mentions
- **classifier** — 3 mentions
- **oracle** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=450|Speech and Language Processing.pdf p. 450]]

## Liens
- Up: [[research/slp/transition-based-dependency-parsing]]
- ← Prev: [[research/slp/a-feature-based-classifier]]
- Next: [[research/slp/advanced-methods-in-transition-based-parsing]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

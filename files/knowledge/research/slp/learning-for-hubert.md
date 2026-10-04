---
title: "Learning for HuBERT"
summary: "§I Large Language Models › Automatic Speech Recognition › Sel: CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION and the output at each 20ms time frame will be a probability distribution over a set of induced phonetic classes C (100 classes or 500 classes, depending on the stage)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "360-361"
---

# Learning for HuBERT

§I Large Language Models › Automatic Speech Recognition › Self-supervised models: HuBERT › Learning for HuBERT · pp. 360–361 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION and the output at each 20ms time frame will be a probability distribution over a set of induced phonetic classes C (100 classes or 500 classes, depending on the stage). Fig. 15.8 shows a sketch of the components. The wavefile is passed through 7 512-channel convolutional layers which learn both to extract spectral information, and to shorten the input sequence down to a 20 ms frame, after which positional encodings are added, and then GELU and layer norm. Selected tokens are then replaced with a mask token, a trained embedding that is shared by all masked frames. The whole sequence is passed through a transformer stack, and the output is passed through a linear projection layer A. The output embedding at each 20ms frame is then compared via cosine with each of the embeddings for the 100 (/500) phonetic classes, resulting in a set of 100 logits representing the similarity of the current 20ms audio timestep to each class. These are then passed through a softmax to get a probability distribution over the classes. Let’s first discuss how we induce the 100 or 500 phonetic classes that are the target of training. To bootstrap these units, HuBERT starts with mel frequency cepstral coefficients, or MFCC vectors, a 39-dimensional feature vector that emphasizes aspects of the signal that are relevant for detection of phonetic units.

## Key terms
- **training** — 16 mentions
- **layer** — 12 mentions
- **vector** — 12 mentions
- **classes** — 10 mentions
- **mfcc** — 10 mentions
- **through** — 9 mentions
- **cosine** — 9 mentions
- **unit** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=360|Speech and Language Processing.pdf p. 360]]

## Liens
- Up: [[research/slp/self-supervised-models-hubert]]
- ← Prev: [[research/slp/hubert-forward-pass]]
- Next: [[research/slp/k-means-clustering]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

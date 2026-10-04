---
title: "The LSTM"
summary: "§I Large Language Models › RNNs and LSTMs › The LSTM: 13.11 illustrates such a bidirectional network that concatenates the outputs of the forward and backward pass. Other simple ways to combine the forward and backward contexts include element-wise addition or multiplication."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "304-307"
---

# The LSTM

§I Large Language Models › RNNs and LSTMs › The LSTM · pp. 304–307 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 13 • RNNS AND LSTMS Fig. 13.11 illustrates such a bidirectional network that concatenates the outputs of the forward and backward pass. Other simple ways to combine the forward and backward contexts include element-wise addition or multiplication. The output at each step in time thus captures information to the left and to the right of the current input. In sequence labeling applications, these concatenated outputs can serve as the basis for a local labeling decision. RNN 2 RNN 1 x1 y2 y1 y3 yn concatenated outputs x2 x3 xn Figure 13.11 A bidirectional RNN. Separate models are trained in the forward and backward directions, with the output of each model at each time point concatenated to represent the bidirectional state at that time point. Bidirectional RNNs have also proven to be quite effective for sequence classification. Recall from Fig. 13.8 that for sequence classification we used the final hidden state of the RNN as the input to a subsequent feedforward classifier. A difficulty with this approach is that the final state naturally reflects more information about the end of the sentence than its beginning. Bidirectional RNNs provide a simple solution to this problem; as shown in Fig.

## Key terms
- **lstm** — 21 mentions
- **context** — 20 mentions
- **information** — 19 mentions
- **layer** — 19 mentions
- **unit** — 19 mentions
- **hidden** — 18 mentions
- **input** — 17 mentions
- **output** — 16 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=304|Speech and Language Processing.pdf p. 304]]

## Liens
- Up: [[research/slp/rnns-and-lstms]]
- ← Prev: [[research/slp/stacked-and-bidirectional-rnn-architectures]]
- Next: [[research/slp/summary-common-rnn-nlp-architectures]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section

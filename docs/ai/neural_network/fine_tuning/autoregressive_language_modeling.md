# Autoregressive Language Modeling [Self-Sup]

## Description

In autoregressive language modeling, which is used in models such as GPT, the model predicts the next word in a sentence given all the preceding words.
It's trained to maximize the likelihood of a word given its previous words in the sentence.

## Formula

The objective of an autoregressive language model is to maximize:

$$
L = \sum_i \log \big( P(w_i \mid w_1, \ldots, w_{i-1}; \theta) \big)
$$

- $w_i$ is the current word, w1,....
- $wi−1$ are the previous words
- $θ$ represents the model parameters

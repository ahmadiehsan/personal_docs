# Autoregressive Language Modeling {Self-Sup}

## Description

In autoregressive language modeling, which is used in models such as GPT, the model predicts the next word in a sentence given all the preceding words. It's trained to maximize the likelihood of a word given its previous words in the sentence.

## Formula

The objective of an autoregressive language model is to maximize:

<img src="image1.png" style="width:2.96354in" />

where w_i is the current word, w1,...., and wi−1 are the previous words, and θ represents the model parameters.

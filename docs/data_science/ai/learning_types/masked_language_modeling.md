# Masked Language Modeling (MLM) [Self-Sup]

## Description

This strategy, used in the training of BERT, randomly masks some percentage of the input tokens and tasks the model with predicting the masked words based on the context provided by the unmasked words. For instance, in the sentence "The cat is on the mat," we could mask "cat," and the model’s job would be to predict this word. Please note that more than one word can also be masked.

## Formula

Mathematically, the objective of an MLM is to maximize the following likelihood:

<img src="image1.png" style="width:2.27377in" />

where w\_i is a masked word, w\_{-i} are the non-masked words, and θ represents the model parameters.

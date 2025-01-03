# Overview

## Supervised

Involves training a model on labeled data, where each data point is associated with a target label or category. The model then uses this labeled data to learn the patterns and relationships between the input text and the target labels.

## Unsupervised

Unsupervised learning is useful when there is no labeled data available or when the number of categories or topics is not known.

## Semi-Supervised

Combines both supervised and unsupervised learning approaches. It involves using a small amount of labeled data to train a model and then using the model to classify the remaining unlabeled data. The model then uses the unlabeled data to improve its classification performance.

Semi-supervised learning is useful when labeled data is scarce or expensive to obtain.

## Self-Supervised

Self-supervised learning is a form of unsupervised learning where the data provides the supervision. In other words, the model learns to predict certain parts of the input data from other parts of the same input data. It does not require explicit labels provided by humans, hence the term self-supervised.

In the context of language models, self-supervision is typically implemented by predicting parts of a sentence when given other parts. For example, given the sentence "The cat is on the __," the model would be trained to predict the missing word ("mat," in this case).

# Weighted Sampling {Sampling}

## Description

In weighted sampling, each sample is assigned a weight—the probability of being sampled. For example, for a population containing classes A and B, if you assign weights of 0.8 to class A and 0.2 to class B, the probabilities of being sampled for class A and B are 80% and 20%, respectively.

**Weight sampling can leverage domain expertise, which is important for reducing sampling biases.** For example, in training some online learning models, recent data is much more important than old data. Through assigning bigger weights to recent data and smaller weights to old data, you can train a model more reliably.

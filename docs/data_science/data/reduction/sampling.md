# Sampling

## Description

Sampling is the process of selecting a subset of data from a larger population to analyze, model, or draw conclusions.
It helps reduce computational costs, manage large datasets, and address data imbalance or bias by choosing representative samples using various methods.

## Varieties

=== "Random"

    Random sampling is the simplest form of probabilistic sampling.
    All the samples in the population have the same chance of being sampled, thus their probabilities form a uniform distribution.
    For example, if you want to sample 5 out of a 10 population, the probability of every element being selected is 0.5.

    The method is straightforward and easy to implement, but the rare classes in the population might not be sampled in the selection.
    Suppose you want to sample 1% from your data, but a rare class appears only in 0.01% of the population: samples of this rare class might not be selected.
    **In this condition, models trained with the sampled subsets might not know the existence of the rare class.**

=== "Systematic"

    Systematic sampling selects every kth item from a list after a random starting point.
    It is more structured than random sampling and can be useful when the data is ordered in a meaningful way, though it risks introducing bias if the ordering aligns with hidden periodic patterns.

=== "Stratified"

    To avoid the drawbacks of simple random sampling, you can **divide the population to several groups according to your requirements, for example the labels, and sample from each group separately.** Each group is called a stratum and this method is called stratified sampling.

    For example, to sample 1% of a population that has classes A and B, you can divide the population to two groups and sample 1% from the two groups, respectively.
    In this way, **no matter how rare A or B is, the sampled subsets are ensured to contain both of the two classes.**

    However, a drawback of stratified sampling is that the population is not always divisible.
    For example, in a multi-label learning task in which each sample has multiple labels, it is challenging to divide the population according to different labels.

=== "Weighted"

    In weighted sampling, each sample is assigned a weight—the probability of being sampled.
    For example, for a population containing classes A and B, if you assign weights of 0.8 to class A and 0.2 to class B, the probabilities of being sampled for class A and B are 80% and 20%, respectively.

    **Weight sampling can leverage domain expertise, which is important for reducing sampling biases.** For example, in training some online learning models, recent data is much more important than old data.
    Through assigning bigger weights to recent data and smaller weights to old data, you can train a model more reliably.

=== "Importance"

    Importance sampling is one of the most important sampling methods.
    It allows us to sample from a distribution when we only have access to another distribution.

    For example, we want to sample from a distribution $P(x)$, but can't access it.
    However, we can access another distribution $Q(x)$.
    **The following equation shows that, in expectation, $x$ sampled from $P(x)$ equals to x sampled from $Q(x)$ weighted by $P(x)/Q(x)$.**

    Therefore, **instead of sampling from $P(x)$, we can alternatively sample from $Q(x)$ which is accessible, and weight the sampled results by $P(x)/Q(x)$.** The results are the same as we directly sample from $P(x)$.

=== "Reservoir"

    Reservoir sampling is an interesting and elegant algorithm to deal with streaming data in online learning models, which is quite popular in products.

    Suppose the data is generated in a sequential streaming manner, for example, a time series, and you can't fit all the data to the memory, nor do you know how much data will be generated in the future.
    **You need to sample a subset with k samples to train a model, but you don't know which sample to select because many samples haven't been generated yet.**

    Reservoir sampling can deal with this problem that **1) all the samples are selected with equal probability and 2) if you stop the algorithm at any time, the samples are always selected with correct probability.**

    The algorithm contains 3 steps:

    1. Put the first k samples in a reservoir, which could be an array or a list
    2. When the nth sample is generated, randomly select a number m within the range of 1 to n. If the selected number m is within the range of 1 to k, replace the mth sample in the reservoir with the nth generated sample, otherwise do nothing.
    3. Repeat 2 until the stop of the algorithm.

    **We can easily prove that for each newly generated sample, the probability of being selected to the reservoir is k/n.
    We can also prove that for each sample that is already in the reservoir, the probability of not being replaced is also k/n.** Thus when the algorithm stops, all the samples in the reservoir are selected with correct probability.

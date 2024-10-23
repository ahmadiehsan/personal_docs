# Reservoir Sampling

## Description

Reservoir sampling is an interesting and elegant algorithm to deal with streaming data in online learning models, which is quite popular in products.

Suppose the data is generated in a sequential streaming manner, for example, a time series, and you can't fit all the data to the memory, nor do you know how much data will be generated in the future. **You need to sample a subset with k samples to train a model, but you don't know which sample to select because many samples haven't been generated yet.**

Reservoir sampling can deal with this problem that **1) all the samples are selected with equal probability and 2) if you stop the algorithm at any time, the samples are always selected with correct probability.**

The algorithm contains 3 steps:

1. Put the first k samples in a reservoir, which could be an array or a list
2. When the nth sample is generated, randomly select a number m within the range of 1 to n. If the selected number m is within the range of 1 to k, replace the mth sample in the reservoir with the nth generated sample, otherwise do nothing.
3. Repeat 2 until the stop of the algorithm.

**We can easily prove that for each newly generated sample, the probability of being selected to the reservoir is k/n. We can also prove that for each sample that is already in the reservoir, the probability of not being replaced is also k/n.** Thus when the algorithm stops, all the samples in the reservoir are selected with correct probability.

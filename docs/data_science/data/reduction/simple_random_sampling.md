# Simple Random Sampling {Sampling}

## Description

It is the simplest form of probabilistic sampling.
All the samples in the population have the same chance of being sampled, thus their probabilities form a uniform distribution.
For example, if you want to sample 5 out of a 10 population, the probability of every element being selected is 0.5.

The method is straightforward and easy to implement, but the rare classes in the population might not be sampled in the selection.
Suppose you want to sample 1% from your data, but a rare class appears only in 0.01% of the population: samples of this rare class might not be selected. **In this condition, models trained with the sampled subsets might not know the existence of the rare class.**

# Multiple Negative Ranking (MNR) (InfoNCE7) (NTXentLoss) [Embedding]

## Description

Multiple negative ranking (MNR) loss, often referred to as InfoNCE7 or NTXentLoss, is a loss that uses either positive pairs of sentences or triplets that contain a pair of positive sentences and an additional unrelated sentence. This unrelated sentence is called a negative and represents the dissimilarity between the positive sentences.

!!! info

    Have very effect on the embedding model, it is recommended to use it instead of other loss functions.

!!! info

    Larger batch sizes tend to be better with MNR loss as a larger batch makes the task more difficult. The reason for this is that the model needs to find the best matching sentence from a larger set of potential pairs of sentences. You can adapt the code to try out different batch sizes and get a feeling of the effects.

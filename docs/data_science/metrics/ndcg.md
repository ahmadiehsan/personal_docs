# NDCG [Ranking]

## Description

Normalized Discounted Cumulative Gain (NDCG) is a more sophisticated metric that **considers both the relevance of retrieved documents and their position in the ranking**.
It uses a graded relevance scale (e.g., 0, 1, 2, where 2 is highly relevant) and assigns higher scores to relevant documents retrieved at higher ranks.

!!! info

    A higher NDCG indicates that highly relevant documents are retrieved at higher ranks.

## Formula

NDCG involves calculating the Discounted Cumulative Gain (DCG) of the retrieved list and normalizing it by the Ideal Discounted Cumulative Gain (IDCG), which is the DCG of the perfectly ranked list.

!!! info

    The formula is complex but can be easily computed using libraries such as sklearn.

# Mean Reciprocal Rank (MRR) [Ranking]

## Description

MRR considers the rank of the first relevant document retrieved.
It emphasizes the importance of retrieving relevant documents early in the ranking.

!!! info

    A higher MRR indicates that relevant documents are retrieved at higher ranks (closer to the top).

## Formula

$$
\mathrm{MRR} = \frac{1}{\lvert Q\rvert} \sum_{i=1}^{\lvert Q\rvert} \frac{1}{\mathrm{rank}_i}
$$

- $\lvert Q\rvert$ is the number of queries
- $\mathrm{rank}_i$ is the rank of the first relevant document for query $i$

## Example

If the first relevant document for a query is retrieved at rank 3, the reciprocal
rank is $1/3$. MRR averages these reciprocal ranks across multiple queries.

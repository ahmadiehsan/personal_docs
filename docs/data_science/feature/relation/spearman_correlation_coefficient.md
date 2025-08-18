# Spearman Correlation Coefficient ($Rs$ or $\rho$) {Not Normal} {2 Continuous}

## Description

The Spearman Correlation Coefficient, denoted as Rs ($\rho$), is a non-parametric measure of statistical dependence between two variables.
It assesses how well the relationship between the variables can be described by a monotonic function.
Unlike Pearson's correlation, which measures linear relationships, Spearman's correlation evaluates the rank-order relationship.

Spearman's correlation coefficient ranges from -1 to 1:

- 1 indicates a perfect positive monotonic relationship
- -1 indicates a perfect negative monotonic relationship
- 0 indicates no monotonic relationship

## Formula

$$
\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}
$$

- $\rho$  = Spearman's rank correlation coefficient
- $d_i$  = difference between the two ranks of each observation
- $n$  = number of observations

To compute it:

1. Convert the raw scores to ranks.
2. Find the difference between the ranks for each pair of data points.
3. Apply the formula.

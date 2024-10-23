# Pearson Correlation Coefficient (R) [Normal] [2 Continuous]

## Description

Correlation coefficients serve as indicators of the strength and direction of the linear relationship between two variables. In the realm of feature selection, these coefficients prove useful in identifying features highly correlated with the target variable, thus serving as potentially valuable predictors.

The prevalent correlation coefficient employed for feature selection is the Pearson correlation coefficient, also referred to as Pearson's r. Pearson's r measures the linear relationship between two continuous variables, ranging from -1 (indicating a perfect negative correlation) to 1 (indicating a perfect positive correlation), with 0 denoting no correlation.

## Formula

Its calculation involves dividing the covariance between the two variables by the product of their standard deviations, as depicted in the following equation:

$$
r = \frac{cov(X, Y)}{std(X) \cdot std(Y)}
$$

- $X$ and $Y$ represent the two variables of interest.
- $cov()$ denotes the covariance function.
- $std()$ represents the standard deviation function.

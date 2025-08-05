# Pearson Correlation Coefficient (R) {Normal} {2 Continuous}

## Description

Correlation coefficients serve as indicators of the strength and direction of the linear relationship between two variables. In the realm of feature selection, these coefficients prove useful in identifying features highly correlated with the target variable, thus serving as potentially valuable predictors.

**Multicollinearity** occurs when two or more independent variables in a regression model are highly correlated, making it difficult to determine each variable’s true effect on the target. By examining the correlation matrix, we can identify pairs of variables with high correlation and consider removing or combining them to reduce multicollinearity and improve model reliability.

The prevalent correlation coefficient employed for feature selection is the Pearson correlation coefficient, also referred to as Pearson's r. Pearson's r measures the linear relationship between two continuous variables, ranging from -1 (indicating a perfect negative correlation) to 1 (indicating a perfect positive correlation), with 0 denoting no correlation.

## Formula

Its calculation involves dividing the covariance between the two variables by the product of their standard deviations, as depicted in the following equation:

$$
r = \frac{cov(X, Y)}{std(X) \cdot std(Y)}
$$

- $X$ and $Y$ represent the two variables of interest.
- $cov()$ denotes the covariance function.
- $std()$ represents the standard deviation function.

## Vs Causation

Correlation is the statistical measure that shows a relationship between two variables. When one changes, the other changes as well, positively or negatively. However, this doesn't mean that one variable causes the other to change. Causation means that one variable directly causes a change in the other. It implies a cause-and-effect relationship, not just an association. Proving causation requires deeper analysis and additional evidence.

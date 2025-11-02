# Pearson Correlation Coefficient (R) [2 Continuous] [Normal]

## Description

Correlation coefficients serve as indicators of the strength and direction of the linear relationship between two variables.
In the realm of feature selection, these coefficients prove useful in identifying features highly correlated with the target variable, thus serving as potentially valuable predictors.

**Multicollinearity** occurs when two or more independent variables in a regression model are highly correlated, making it difficult to determine each variable's true effect on the target.
By examining the correlation matrix, we can identify pairs of variables with high correlation and consider removing or combining them to reduce multicollinearity and improve model reliability.

The prevalent correlation coefficient employed for feature selection is the Pearson correlation coefficient, also referred to as Pearson's r.
Pearson's r measures the linear relationship between two continuous variables, ranging from -1 (indicating a perfect negative correlation) to 1 (indicating a perfect positive correlation), with 0 denoting no correlation.

## Formula

Its calculation involves dividing the covariance between the two variables by the product of their standard deviations, as depicted in the following equation:

$$
r = \frac{cov(X, Y)}{std(X) \cdot std(Y)}
$$

- $X$ and $Y$ represent the two variables of interest.
- $cov()$ denotes the covariance function.
- $std()$ represents the standard deviation function.

## Vs Causation

Correlation is the statistical measure that shows a relationship between two variables.
When one changes, the other changes as well, positively or negatively.
However, this doesn't mean that one variable causes the other to change. Causation means that one variable directly causes a change in the other. It implies a cause-and-effect relationship, not just an association. Proving causation requires deeper analysis and additional evidence.

## Example

=== "Simple"

    ```python
    corr_matrix = housing.corr(numeric_only=True)
    corr_matrix["median_house_value"].sort_values(ascending=False)

    # median_house_value  1.000000
    # median_income       0.688380
    # total_rooms         0.137455
    # housing_median_age  0.102175
    # households          0.071426
    # total_bedrooms      0.054635
    # population         -0.020153
    # longitude          -0.050859
    # latitude           -0.139584
    # Name: median_house_value, dtype: float64
    ```

=== "Scatter Matrix"

    ```python
    from pandas.plotting import scatter_matrix

    attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
    scatter_matrix(housing[attributes], figsize=(12, 8))
    plt.show()
    ```

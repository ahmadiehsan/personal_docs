# Chi-Squared [Not Normal] [2 Categorical]

## Description

The chi-squared test is a widely employed statistical method in ML for feature selection that's particularly effective for categorical variables. This test gauges the dependence between two random variables, providing a P-value that signifies the likelihood of obtaining a result as extreme as or more extreme than the actual observations.

In hypothesis testing, the chi-squared test assesses whether the collected data aligns with the expected data. A small chi-squared test statistic indicates a robust match, while a large statistic implies a weak match. A P-value less than or equal to 0.05 leads to the rejection of the null hypothesis, considering it highly improbable. Conversely, a P-value greater than 0.05 results in accepting or "failing to reject" the null hypothesis. When the P-value hovers around 0.05, further scrutiny of the hypothesis is warranted.

In feature selection, the chi-squared test evaluates the relationship between each feature and the target variable in the dataset. It determines significance based on whether a statistically significant difference exists between the observed and expected frequencies of the feature, assuming independence between the feature and target. Features with a high chi-squared score exhibit a stronger dependence on the target variable, making them more informative for classification or regression tasks.

**An exemplary application of chi-squared feature selection lies in text classification**, particularly in scenarios where the presence or absence of specific words in a document serves as features. The chi-squared test helps identify words strongly associated with a particular class or category of documents, subsequently enabling their use as features in an ML model. In categorical data, especially where the relationship between features and the target variable is non-linear, chi-squared proves to be a valuable method for feature selection. However, its suitability diminishes for continuous or highly correlated features, where alternative feature selection methods may be more fitting.

## Formula

The formula for calculating the chi-squared is presented in the following equation:

$$
X^2 = \sum \frac{(O_i - E_i)^2}{E_i}
$$

In this equation, $O_i$ represents the observed value and $E_i$ represents the expected value. The computation involves finding the difference between the observed frequency and the expected frequency, squaring the result, and then dividing by the expected frequency. The summation of these values across all categories of the feature yields the overall chi-squared statistic for that feature.

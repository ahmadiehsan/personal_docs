# Chi-Squared {Not Normal} {2 Categorical}

## Description

The chi-squared measures the dependence between two random variables and provides a P-value indicating the likelihood of observing the given data under the null hypothesis.

The chi-squared test is mainly used for selecting informative categorical features (such as in text classification), but is less suitable for continuous or highly correlated data.

## Workflow

In hypothesis testing, the chi-squared test compares observed data to expected data. A small test statistic means the data matches expectations well; a large statistic suggests a poor match. Typically, a P-value ≤ 0.05 leads to rejecting the null hypothesis (indicating a significant relationship), while a P-value > 0.05 means we fail to reject it. If the P-value is close to 0.05, further investigation is recommended.

## Formula

The formula for calculating the chi-squared is presented in the following equation:

$$
X^2 = \sum \frac{(O_i - E_i)^2}{E_i}
$$

In this equation, $O_i$ represents the observed value and $E_i$ represents the expected value. The computation involves finding the difference between the observed frequency and the expected frequency, squaring the result, and then dividing by the expected frequency. The summation of these values across all categories of the feature yields the overall chi-squared statistic for that feature.

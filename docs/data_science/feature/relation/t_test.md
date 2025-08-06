# T-Test {Normal} {Continuous vs Categorical}

## Description

A t-test is a statistical method used to determine if there is a significant difference between the means of **two groups**.

It's commonly used when you have a small sample size and want to compare the means to see if they are different from each other.

There are two main types:

- **Independent t-test (Two-sample t-test)**: Used when comparing the means of two independent groups (e.g., test scores of two different classes).
- **Paired t-test (Dependent t-test)**: Used when comparing means from the same group at different times (e.g., before and after a treatment on the same group).

Key Concepts:

- **Null Hypothesis (H0)**: Assumes no difference between group means.
- **Alternative Hypothesis (H1)**: Assumes a difference exists.
- **p-value**: Helps decide if the observed difference is statistically significant. A p-value less than 0.05 typically indicates significance.

You run a t-test to find out if the difference in means is due to chance or if it reflects a true difference in the population.

## Example

```python
from scipy import stats

# Sample data with two groups (The null hypothesis (H₀) states: The two groups have the same mean)
group1 = [5, 7, 8, 6, 9]       # e.g., test scores of group 1
group2 = [10, 12, 11, 14, 13]  # test scores of group 2

# Perform independent two-sample t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

print("t-statistic:", t_stat)
print("p-value:", p_value)

# Interpret the p-value
if p_value < 0.05:  # if p-value is less that 50%
    print("Result: Reject the null hypothesis — groups likely have different means.")
else:
    print("Result: Fail to reject the null hypothesis — no strong evidence of difference.")
```

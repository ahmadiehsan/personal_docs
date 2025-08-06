# ANOVA {Normal} {Continuous vs Categorical}

## Description

ANOVA stands for Analysis of Variance, which is a statistical method used to analyze whether there are significant differences between the means of three or more groups.

It's commonly used in experiments or studies where you want to compare multiple groups to see if there's a statistically significant difference between them.

It's like an extended version of a **t-test** but for **more than two groups**.

## Example

```python
from scipy import stats

# Sample data: three groups (The null hypothesis (H₀) states: All groups have the same mean)
group1 = [5, 7, 8, 6, 9]       # e.g., scores from class A
group2 = [10, 12, 11, 14, 13]  # scores from class B
group3 = [8, 9, 7, 6, 10]      # scores from class C

# Perform one-way ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)

print("F-statistic:", f_stat)
print("p-value:", p_value)

# Interpret the p-value
if p_value < 0.05:  # if p-value is less that 50%
    print("Result: Reject the null hypothesis — at least one group mean differs.")
else:
    print("Result: Fail to reject the null hypothesis — no strong evidence of difference.")
```

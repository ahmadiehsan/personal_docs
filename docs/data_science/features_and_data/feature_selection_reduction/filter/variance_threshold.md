# Variance Threshold [Not Normal] [1 Continuous]

## Description

Variance Threshold is a baseline approach to feature selection. As the name suggests, it drops all features where the variance along the column does not exceed a threshold value. The premise is that a feature that doesn't vary much within itself, has very little predictive power.

## Example

```python
X = [[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]]
selector = VarianceThreshold()
selector.fit_transform(X)

# Output:
# array([[2, 0],
#        [1, 4],
#        [1, 1]])
```

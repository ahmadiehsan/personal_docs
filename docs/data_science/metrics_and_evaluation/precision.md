# Precision (PPV) [Categorical] [Imbalance]

## Description

Precision gauges the ratio of correctly identified positive instances to the total instances predicted as positive by the model.
It is also referred to as **positive predictive value (PPV)**.

Precision proves valuable in scenarios where the expense associated with false positives is significant.

## Formula

Precision is defined as the number of true positives divided by the number of true positives plus the number of false positives.

$$
\text{Precision} = \frac{\text{Relevant retrieved instances}}{\text{All retrieved instances}}
$$

- **Relevant retrieved instances**: Total correctly identified positive instances (True Positives)
- **All retrieved instances**: Total instances predicted as positive (True Positives + False Positives)

## Example

```python
from sklearn.metrics import precision_score

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]  # TP=2, FP=0, TN=2, FN=1

print(precision_score(y_true, y_pred))  # 1.0
```

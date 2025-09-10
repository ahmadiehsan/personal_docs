# Recall (TPR) [Classification] [Imbalance]

## Description

Recall, also recognized as sensitivity or the **true positive rate (TPR)**, assesses the ratio of correctly identified positive instances among the total **actual** positive instances.

Recall is useful when the cost of false negatives is high.

## Formula

The precise definition of recall is the number of true positives divided by the number of true positives plus the number of false negatives.

$$
\text{Recall} = \frac{\text{Relevant retrieved instances}}{\text{All relevant instances}}
$$

- **Relevant retrieved instances**: Total correctly identified positive instances (True Positives)
- **All relevant instances**: Total actual positive instances (True Positives + False Negative)

## Example

```python
from sklearn.metrics import recall_score

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]  # TP=2, FP=0, TN=2, FN=1

print(recall_score(y_true, y_pred))  # 0.6666666666666666
```

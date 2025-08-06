# AUC-ROC {Categorical}

## Description

The AUC-ROC curve is a tool for evaluating the performance of binary classification models.

It plots the True Positive Rate (TPR) against the False Positive Rate (FPR) at different thresholds, showing how well a model can distinguish between two classes, such as positive and negative outcomes.

It provides a graphical representation of the model's ability to distinguish between two classes, like a positive class for the presence of a disease and a negative class for the absence of a disease.

## Example

```python
from sklearn.metrics import roc_auc_score

y_true = [1, 0, 1, 1, 0]
y_scores = [0.9, 0.4, 0.8, 0.3, 0.2]

print(roc_auc_score(y_true, y_scores))  # 0.8333333333333333
```

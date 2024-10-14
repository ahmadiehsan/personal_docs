# Accuracy [Balance]

## Description

In classification problems is the number of correct predictions made by the model divided by the total number of predictions.

For example, if the test set was 100 messages and our model correctly predicted 80 messages, then we have 80/100 = 0.8 or 80% accuracy.

- Is useful when target classes are **well balanced**
- Is **not** a good choice with **unbalanced** classes! (Imagine we had 99 legitimate ham messages and 1 spam text message. lf our model was simply a line that always predicted HAM we would get 99% accuracy!

## Formula

<img src="image1.jpg" style="width:5.17959in" />

## Examples

|              | Predicted: NO | Predicted: YES | Total |
|--------------|---------------|----------------|-------|
| Actual: NO   | TN = 50       | FP = 10        | 60    |
| Actual: YES  | FN = 5        | TP = 100       | 105   |
| Total        | 55            | 110            |       |

Accuracy:

- Overall, how often is it **correct**?
- (TP + TN) / total = 150 / 165 = 0.91

---

| n = 165     | Predicted: NO  | Predicted: YES | Total |
|-------------|----------------|----------------|-------|
| Actual: NO  | TN = 50        | FP = 10        | 60    |
| Actual: YES | FN = 5         | TP = 100       | 105   |
| Total       | 55             | 110            |       |

Misclassification Rate (Error Rate):

- Overall, how often is it **wrong**?
- (FP + FN) / total = 15/165 = 0.09

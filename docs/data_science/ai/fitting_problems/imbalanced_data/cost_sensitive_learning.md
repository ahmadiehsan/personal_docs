# Cost-Sensitive Learning

## Description

Cost-sensitive learning is a technique for handling **imbalanced datasets** where one class (usually the minority class) has far fewer examples than the other. **Standard machine learning models** often favor the majority class, leading to poor performance on the minority class. Cost-sensitive learning addresses this by **assigning different misclassification costs** to each class, ensuring the model gives appropriate attention to the minority class.

To improve model performance, different strategies can be applied:

- **Error Costs:** Assign higher costs to false negatives (FN) when the minority class is more important.
- **Ensemble Methods (Bagging/Boosting):** Combine multiple models to ensure both minority and majority classes are well learned.
- **Anomaly Detection:** Treat the minority class as an "anomaly" so that the model actively detects its rare occurrence.

By adjusting the **cost function or loss function**, the model **learns with sensitivity toward minority class instances**, improving its predictive performance on imbalanced data.

## Workflow

We can assign costs in the form of a confusion matrix:

|                     | Predicted Positive | Predicted Negative |
|---------------------|--------------------|--------------------|
| **Actual Positive** | TP_cost            | FN_cost            |
| **Actual Negative** | FP_cost            | TN_cost            |

To incorporate the cost matrix into the training process, we can modify the standard loss function that the model optimizes during training. One common cost-sensitive loss function is the weighted cross-entropy loss, which is defined as follows:

$$
\text{loss} = - (w_{\text{pos}} \cdot y \cdot \log(\hat{y}) + w_{\text{neg}} \cdot (1 - y) \cdot \log(1 - \hat{y}))
$$

Weights \(w_{\text{pos}}\) and \(w_{\text{neg}}\) depend on the **cost matrix**, ensuring the model correctly classifies minority examples.

# Mean Absolute Error (MAE)

## Description

MAE is a regression metric that measures the average of the absolute differences between the predicted values and the actual values. It gives an idea of how far off the predictions are from the true values, regardless of direction.

- Is **intuitive** and **easy to interpret**
- Sensitive to **large errors**, but doesn't penalize outliers as much as squared error (MSE)
- MAE is **easy to understand** and provides a straightforward measure of model performance.
- It doesn't **squash errors**, unlike MSE, so large deviations are treated equally.
- **Lower values** indicate better model performance.

## Formula

$$
\text{MAE} = \dfrac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

- $y_i$ = actual value
- $\hat{y}_i$ = predicted value
- $n$ = number of samples

## Example

| Actual | Predicted | Absolute Error |
|--------|-----------|----------------|
| 5      | 3         | 2              |
| 7      | 9         | 2              |
| 10     | 8         | 2              |

Average of absolute errors (MAE): $(2 + 2 + 2) / 3 = 2.0$

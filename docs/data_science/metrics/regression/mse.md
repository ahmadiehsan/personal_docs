# Mean Squared Error (MSE)

## Description

MSE is a regression metric that measures the average of the squared differences between the predicted values and the actual values.

It gives a sense of how far off predictions are from the true values, with a heavier penalty for larger errors.

- **Penalizes large errors** more heavily than MAE, due to the squaring of differences
- Sensitive to **outliers**, as large errors are disproportionately penalized
- **Less interpretable** than MAE due to squaring of errors
- **Lower values** indicate better model performance, but values are in squared units of the target variable.

## Formula

$$
\text{MSE} = \dfrac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

- $y_i$ = actual value
- $\hat{y}_i$ = predicted value
- $n$ = number of samples

## Example

| Actual | Predicted | Squared Error |
| ------ | --------- | ------------- |
| 5      | 3         | 4             |
| 7      | 9         | 4             |
| 10     | 8         | 4             |

Average of squared errors (MSE): $(4 + 4 + 4) / 3 = 4.0$

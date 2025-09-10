# Root Mean Squared Error (RMSE) [Regression]

## Description

RMSE is a regression metric that measures the square root of the average of the squared differences between predicted values and actual values.
It penalizes large errors more heavily than MAE due to the squaring of differences, making it sensitive to outliers.

RMSE is directly derived from **Mean Squared Error (MSE)**, which is the average of squared errors.

- **Sensitive to outliers** due to the squaring of errors
- **Penalizes large errors** more than MAE, which makes it more useful when large errors are particularly undesirable
- **Lower values** indicate better model performance.

## Formula

$$
\text{RMSE} = \sqrt{\dfrac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
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

RMSE: $\sqrt{4.0} = 2.0$

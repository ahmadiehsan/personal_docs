# Vs (MSE & RMSE)

## Description

**MSE** (Mean Squared Error) and **RMSE** (Root Mean Squared Error) are both used to measure the accuracy of a model's predictions, with a focus on regression tasks.

- **MSE** quantifies the average squared difference between predicted and actual values. The larger the MSE, the worse the model's performance.
- **RMSE** is simply the square root of MSE, bringing the error back to the same unit scale as the original data, making it more interpretable.

## Differences

- **MSE** emphasizes larger errors more due to the squaring of the differences. It can be sensitive to outliers.
- **RMSE** provides a more tangible error metric as it's in the same units as the target variable.

## Use Cases

- Use **MSE** when you want to penalize larger errors more heavily.
- Use **RMSE** when you want a metric that is in the same units as the target for easier interpretation.

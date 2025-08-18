# LASSO (L1)

## Description

**LASSO (Least Absolute Shrinkage and Selection Operator)** is a **linear regression technique** used for **feature selection**.
It adds a **penalty term** to shrink less important coefficients to zero, effectively removing them.

LASSO is **especially useful for high-dimensional data**, where features outnumber samples, helping identify key predictors.

- **Advantages**: Handles correlated features, performs feature selection and regression simultaneously.
- **Limitations**: May select only one feature from correlated groups and struggle with very high-dimensional data.

## Formula

$$
\min_{\beta} \sum_{i=1}^{n} (y_i - X_i \beta)^2 + \lambda \sum_{j=1}^{p} |\beta_j|
$$

- $y_i$ = target variable
- $X_i$ = feature vector
- $\beta$ = regression coefficients
- $\lambda$ = regularization parameter controlling sparsity

## Example

LASSO aids feature selection for house price prediction.
Given a dataset (e.g., bedrooms, lot size, year built, prices), LASSO identifies key features while fitting a linear model, enabling price forecasting for new houses.

```python
from sklearn.linear_model import LogisticRegression

# Train logistic regression with L1 (Lasso) penalty
model = LogisticRegression(solver='liblinear', penalty='l1', max_iter=1000)
model.fit(X, y)
```

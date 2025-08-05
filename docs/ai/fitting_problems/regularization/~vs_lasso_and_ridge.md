# Vs (LASSO & Ridge)

## Description

Both LASSO and Ridge prevent overfitting by penalizing coefficients but differ in approach.

- **Ridge Regression** adds an SSE penalty proportional to the square of coefficients, shrinking them but **not setting them to zero**. It’s useful for reducing the impact of irrelevant features while keeping all.
- **LASSO** penalizes the absolute value of coefficients, with high regularization setting some exactly **to zero**. This makes LASSO useful for **feature selection**.
- **LASSO is better** when few features matter, creating a simpler model.
- **Ridge is better** when most features are relevant, preserving them but reducing their impact.

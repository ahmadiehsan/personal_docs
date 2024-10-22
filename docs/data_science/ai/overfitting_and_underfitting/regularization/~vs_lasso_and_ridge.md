# Vs (LASSO & Ridge)

## Description

Ridge regression and LASSO are both regularization techniques that are used in linear regression to prevent overfitting of the model by penalizing the model’s coefficients. While both methods seek to prevent overfitting, they differ in their approach to how the coefficients are penalized.

Ridge regression adds a penalty term to the sum of squared errors (SSE) that is proportional to the square of the magnitude of the coefficients. The penalty term is controlled by a regularization parameter (α), which determines the amount of shrinkage applied to the coefficients. This penalty term shrinks the values of the coefficients toward zero but does not set them exactly to zero. **Therefore, ridge regression can be used to reduce the impact of irrelevant features in a model, but it will not eliminate them completely**.

On the other hand, LASSO also adds a penalty term to the SSE, but the penalty term is proportional to the absolute value of the coefficients. Like ridge, LASSO also has a regularization parameter ($\lambda$) that determines the amount of shrinkage applied to the coefficients. However, LASSO has a unique property of setting some of the coefficients exactly to zero when the regularization parameter is sufficiently high. **Therefore, LASSO can be used for feature selection as it can eliminate irrelevant features and set their corresponding coefficients to zero.**

In general, **if the dataset has many features** and a small number of them are expected to be important, **LASSO regression is a better choice** as it will set the coefficients of irrelevant features to zero, leading to a simpler and more interpretable model. On the other hand, **if most of the features in the dataset are expected to be relevant, ridge regression is a better choice** as it will shrink the coefficients toward zero but not set them exactly to zero, preserving all the features in the model.

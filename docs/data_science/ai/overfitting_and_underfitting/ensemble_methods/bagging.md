# Bagging (Bootstrap Aggregating)

## Description

Bootstrap aggregating, also known as bagging, is an ensemble method that combines multiple independent models trained on different subsets of the training data to reduce variance and improve model generalization.

The bagging algorithm can be summarized as follows:

1. Given a training dataset of size n, create m bootstrap samples of size n (that is, sample n instances with replacement m times).

2. Train a base model (for example, a decision tree) on each bootstrap sample independently.

3. Aggregate the predictions of all base models to obtain the ensemble prediction. This can be done by either taking the majority vote (in the case of classification) or the average (in the case of regression).

The bagging algorithm is particularly effective when the base models are unstable (that is, have high variance), such as decision trees, and when the training dataset is small.

The advantages of bagging are as follows:

- Improved model generalization by reducing variance and overfitting
- Ability to handle high-dimensional datasets with complex relationships
- Can be used with a variety of base models

The disadvantages of bagging are as follows:

- Increased model complexity and computation time due to the use of multiple base models
- It can sometimes lead to overfitting if the base models are too complex or the dataset is too small
- It does not work well when the base models are highly correlated or biased

## Final Result Formula

The equation for aggregating the predictions of the base models depends on the type of problem (classification or regression).

For classification, the ensemble prediction is obtained by taking the majority vote:

<img src="image2.jpg" style="width:2.20959in" />

For regression, the ensemble prediction is obtained by taking the average score:

<img src="image1.jpg" style="width:1.1073in" />

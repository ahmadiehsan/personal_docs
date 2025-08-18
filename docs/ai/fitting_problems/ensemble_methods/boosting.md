# Boosting

## Description

Boosting is an **ensemble learning** technique that **iteratively improves weak classifiers** by focusing on misclassified examples.
Unlike bagging, it adjusts **training example weights** to enhance accuracy.

Advantages:

- **Boosts weak classifiers' accuracy** significantly.
- **Easy to implement & widely applicable**.
- **Handles noisy data** & reduces overfitting.

Disadvantages:

- **Sensitive to outliers** (risk of overfitting).
- **Computationally expensive** for large datasets.
- **Hard to interpret**, as it combines multiple classifiers.

## Workflow

There are several boosting algorithms, but one of the most popular ones is AdaBoost (short for adaptive boosting).
The AdaBoost algorithm works as follows:

1. **Initialize** equal weights for training examples.
2. Train a **weak classifier**.
3. Compute its **weighted error rate**.
4. Determine its **importance** based on error rate.
5. **Increase weights** of misclassified examples.
6. **Normalize weights**.
7. Repeat for a set number of iterations or until desired accuracy.
8. Combine weak classifiers into a **strong model** with weighted importance.

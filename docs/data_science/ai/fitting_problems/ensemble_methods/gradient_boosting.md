# Gradient Boosting

## Description

Gradient boosting is an ensemble model for **classification** and **regression**. It starts with a **weak classifier** (e.g., a simple tree) and improves it iteratively by **focusing on errors** from previous steps.

Advantages:

- **High accuracy**
- Supports **regression & classification**
- Handles **missing data & outliers**
- Works with **various loss functions**
- Effective for **high-dimensional data**

Disadvantages:

- Prone to **overfitting** with too many trees
- **Computationally expensive** for large datasets
- Requires careful **hyperparameter tuning** (trees, learning rate, depth)

## Workflow

Each iteration:

1. Computes the **negative gradient** of the loss function.
2. Fits a **decision tree** to these values.
3. Combines predictions using a **learning rate** to control influence.

The final prediction is the weighted sum of all trees.

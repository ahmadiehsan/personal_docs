# Bagging (Bootstrap Aggregating)

## Description

Bagging is an ensemble method that reduces variance and improves generalization by combining multiple models trained on different bootstrap samples.

Advantages:

- **Reduces overfitting** and variance.
- **Handles complex datasets** with high dimensions.
- **Flexible** with different base models.

Disadvantages:

- **Computationally expensive** due to multiple models.
- **Can overfit** if models are too complex.
- **Less effective** if base models are highly correlated.

## Workflow

1. **Create** m bootstrap samples from the training data.
2. **Train** a base model (e.g., decision tree) on each sample.
3. **Aggregate** predictions using majority vote (classification) or averaging (regression).

## Formula

For classification, bagging takes the **majority vote**:

$$
Y_{\text{ensemble}} = \arg\max_j \sum_{i=1}^{m} I(y_{ij} = j)
$$

For regression, it takes the **average**:

$$
Y_{\text{ensemble}} = \frac{1}{m} \sum_{i=1}^{m} y_i
$$

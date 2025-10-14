# Ensemble Methods {Bagging} {Boosting}

## Description

Ensemble methods are techniques that are used to combine multiple models to improve their performance and prevent overfitting.

This can be done by using techniques such as:

- Bagging
- Boosting
- Stacking

## Varieties

=== "Bagging"

    Bagging (Bootstrap Aggregating) is an ensemble method that reduces variance and improves generalization by combining multiple models trained on different bootstrap samples.

    Advantages:

    - **Reduces overfitting** and variance.
    - **Handles complex datasets** with high dimensions.
    - **Flexible** with different base models.

    Disadvantages:

    - **Computationally expensive** due to multiple models.
    - **Can overfit** if models are too complex.
    - **Less effective** if base models are highly correlated.

=== "Boosting"

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

=== "Stacking"

    Stacking is a popular ensemble learning technique that improves predictive performance by combining the outputs of multiple base models.
    It does this by training a higher-level model on the predictions of these base models.

=== "Gradient Boosting"

    Gradient boosting is an ensemble model for **classification** and **regression**.
    It starts with a **weak classifier** (e.g., a simple tree) and improves it iteratively by **focusing on errors** from previous steps.

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

=== "Bagging"

    1. **Create** m bootstrap samples from the training data.
    2. **Train** a base model (e.g., decision tree) on each sample.
    3. **Aggregate** predictions using majority vote (classification) or averaging (regression).

=== "Boosting"

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

=== "Stacking"

    1. **Split the training data** into two parts:

       - The first part is used to train the base models.
       - The second part is used to generate a new dataset of predictions from the base models.

    2. **Train multiple base models** on the first part of the training data.
    3. **Generate predictions** using the trained base models on the second part of the training data, creating a new dataset of predictions.
    4. **Train a higher-level model** (also called a meta-model or blender) using this new dataset of predictions as input features.
    5. **Make final predictions** on test data using the trained higher-level model.

    The higher-level model is typically a simple algorithm, such as linear regression, logistic regression, or a decision tree.
    Its goal is to learn how to optimally combine the predictions of the base models, leading to improved overall accuracy.

=== "Gradient Boosting"

    Each iteration:

    1. Computes the **negative gradient** of the loss function.
    2. Fits a **decision tree** to these values.
    3. Combines predictions using a **learning rate** to control influence.

    The final prediction is the weighted sum of all trees.

## Formula

=== "Bagging"

    For classification, bagging takes the **majority vote**:

    $$
    Y_{\text{ensemble}} = \arg\max_j \sum_{i=1}^{m} I(y_{ij} = j)
    $$

    For regression, it takes the **average**:

    $$
    Y_{\text{ensemble}} = \frac{1}{m} \sum_{i=1}^{m} y_i
    $$

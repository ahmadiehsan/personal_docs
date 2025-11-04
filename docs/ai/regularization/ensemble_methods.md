# Ensemble Methods {Bagging} {Boosting}

## Description

Ensemble methods are techniques that are used to combine multiple models to improve their performance and prevent overfitting.

This can be done by using techniques such as:

- Bagging
- Boosting
- Stacking

## Varieties

=== "Bagging"

    Bagging (Bootstrap Aggregating) trains multiple models (e.g., decision trees) **in parallel** on different random subsets (bootstrap samples) of the training data.
    The final prediction is made by **averaging** (for regression) or **voting** (for classification) the results from all models.
    Random Forest is a popular example.

    Advantages:

    - **Reduces overfitting** and variance.
    - **Handles complex datasets** with high dimensions.
    - **Flexible** with different base models.

    Disadvantages:

    - **Computationally expensive** due to multiple models.
    - **Less effective** if base models are highly correlated.

    !!! info

        **Hard voting** is like a basic election: every model gets one vote (e.g., "Class A" or "Class B"), and the class that gets the **most votes** wins. It only cares about the final decision.

        **Soft voting** is about *confidence*: each model provides a probability (e.g., "I'm 90% sure it's A," "I'm 60% sure it's B"). We **average the probabilities** from all models, and the class with the highest average confidence wins.

        Soft voting is usually preferred because it gives more weight to models that are highly confident in their predictions, rather than treating every model's vote as equal.

=== "Boosting"

    Boosting trains models **sequentially**, where each new model tries to correct the errors made by the previous ones.
    It focuses on "hard" examples that were misclassified.
    Models are weighted based on their performance, and their predictions are combined for the final result.

    Advantages:

    - **Boosts weak classifiers' accuracy** significantly.
    - **Handles noisy data** & reduces overfitting.

    Disadvantages:

    - **Sensitive to outliers** (risk of overfitting).
    - **Computationally expensive** for large datasets.

=== "Stacking"

    Stacking trains multiple different types of models (called "level-0" or "base" models) on the same data.
    Then, a new "level-1" model (or "meta-model") is trained using the **predictions** of the base models as its input features.
    It learns how to best combine the outputs of the different base models.

=== "Gradient Boosting"

    Gradient boosting is a specific type of boosting.
    It builds models sequentially, like other boosting methods, but each new model is specifically trained to predict the **residual errors** (the difference between the true value and the current prediction) of the ensemble so far.
    It iteratively minimizes a loss function by fitting models along the gradient of that loss.

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

## Example

=== "Bagging"

    ```python
    from sklearn.datasets import make_moons
    from sklearn.ensemble import RandomForestClassifier, VotingClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC

    X, y = make_moons(n_samples=500, noise=0.30, random_state=42)  # Load sample data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    voting_clf = VotingClassifier(
        estimators=[
            ("lr", LogisticRegression(random_state=42)),
            ("rf", RandomForestClassifier(random_state=42)),
            ("svc", SVC(random_state=42))
        ]
    )
    voting_clf.fit(X_train, y_train)  # Hard voting
    ```

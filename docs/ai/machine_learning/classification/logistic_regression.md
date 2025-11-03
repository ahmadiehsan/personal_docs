# Logistic Regression [Sup]

## Description

Logistic regression is a statistical model that transforms a linear regression model to predict categorical dependent variables.
Unlike linear regression which predicts continuous values, logistic regression applies a logistic function to map predictions to probabilities in the range [0,1], making it suitable for classification tasks.
This versatile algorithm can be used for both binary and multiclass classification problems.

<img src="image2.png" style="width:3.5in" />

## Varieties

=== "Binary"

    Logistic regression in its basic form is used for binary classification, where the dependent variable has two possible outcomes, such as "true" and "false" or "yes" and "no." It's commonly applied in various domains for problems like spam identification, disease diagnosis, or customer churn prediction.

=== "Multinomial"

    Multinomial Logistic Regression is a classification method that generalizes logistic regression to multiclass problems, i.e. with more than two possible discrete outcomes.
    That is, it is a model used to predict the probabilities of the different possible outcomes of a categorically distributed dependent variable, given a set of independent variables (which may be real-valued, binary-valued, categorical-valued, etc.).

## Example

=== "Binary"

    ```python
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import f1_score

    X, y = load_breast_cancer(return_X_y=True)  # Load a binary classification dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("F1 Score:", f1_score(y_test, y_pred))
    ```

=== "Multinomial"

    ```python
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import f1_score

    X, y = load_iris(return_X_y=True)  # Load sample data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("F1 Score:", f1_score(y_test, y_pred, average="macro"))
    ```

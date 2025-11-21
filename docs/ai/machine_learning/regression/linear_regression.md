# Linear Regression [Sup] {Polynomial}

## Description

Linear regression is used to identify the relationship between a dependent variable and one or more independent variables and is typically leveraged to make predictions about future outcomes.
When there is only one independent variable and one dependent variable, it is known as simple linear regression.
As the number of independent variables increases, it is referred to as multiple linear regression.
For each type of linear regression, it seeks to plot a line of best fit, which is calculated through the method of least squares.
However, unlike other regression models, this line is straight when plotted on a graph.

<img src="image1.png" style="width:2.5in" />

## Varieties

=== "Standard"

    Standard Linear Regression models the relationship between variables as a straight line, using the least squares method to find the best fit.

=== "Polynomial"

    Polynomial Regression is a form of Linear regression known as a special case of Multiple linear regression which estimates the relationship as an nth degree polynomial.
    It is sensitive to outliers so the presence of one or two outliers can also badly affect the performance.

## Formula

=== "Standard"

    <img src="image3.png" style="width:2in" />

    <img src="image2.png" style="width:2in" />

=== "Polynomial"

    <img src="image4.png" style="width:5in" />

## Example

=== "Polynomial (Scikit-Learn)"

    ```python
    from sklearn.datasets import load_diabetes
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import root_mean_squared_error

    X, y = load_diabetes(return_X_y=True)  # Load sample regression data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("RMSE:", root_mean_squared_error(y_test, y_pred))
    ```

=== "Polynomial (PyTorch - High-Level API)"

    ```python
    import torch
    import torch.nn as nn
    from sklearn.datasets import load_diabetes
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import root_mean_squared_error

    X, y = load_diabetes(return_X_y=True)  # Load sample regression data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    X_train = torch.FloatTensor(X_train)
    X_test = torch.FloatTensor(X_test)
    y_train = torch.FloatTensor(y_train).reshape(-1, 1)
    y_test = torch.FloatTensor(y_test).reshape(-1, 1)

    torch.manual_seed(42)
    n_features = X_train.shape[1]
    model = nn.Linear(in_features=n_features, out_features=1)
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    mse = nn.MSELoss()
    learning_rate = 0.4
    n_epochs = 20

    for epoch in range(n_epochs):
        y_pred = model(X_train)
        loss = mse(y_pred, y_train)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        print(f"Epoch {epoch + 1}/{n_epochs}, Loss: {loss.item()}")

    with torch.no_grad():
        y_pred = model(X_test)

    print("RMSE:", root_mean_squared_error(y_test, y_pred))
    ```

=== "Polynomial (PyTorch - Low-Level API)"

    ```python
    import torch
    from sklearn.datasets import load_diabetes
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import root_mean_squared_error

    X, y = load_diabetes(return_X_y=True)  # Load sample regression data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    X_train = torch.FloatTensor(X_train)
    X_test = torch.FloatTensor(X_test)
    y_train = torch.FloatTensor(y_train).reshape(-1, 1)
    y_test = torch.FloatTensor(y_test).reshape(-1, 1)

    torch.manual_seed(42)
    n_features = X_train.shape[1]
    w = torch.randn((n_features, 1), requires_grad=True)
    b = torch.tensor(0., requires_grad=True)
    learning_rate = 0.4
    n_epochs = 20

    for epoch in range(n_epochs):
        y_pred = X_train @ w + b
        loss = ((y_pred - y_train) ** 2).mean()
        loss.backward()

        with torch.no_grad():
            b -= learning_rate * b.grad
            w -= learning_rate * w.grad
            b.grad.zero_()
            w.grad.zero_()

        print(f"Epoch {epoch + 1}/{n_epochs}, Loss: {loss.item()}")

    with torch.no_grad():
        y_pred = X_test @ w + b  # Use the trained parameters to make predictions

    print("RMSE:", root_mean_squared_error(y_test, y_pred))
    ```

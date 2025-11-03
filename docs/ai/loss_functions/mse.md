# MSE [Regression]

## Description

Mean Squared Error (MSE) is the most commonly used loss function for regression.
The loss is the mean overseen data of the squared differences between true and predicted values

- **Use case**: Regression problems
- **When to use**: Is typically used when you are solving regression problems where the goal is to predict continuous numerical values. Squaring ensures that both positive and negative differences contribute equally to the loss.
- **Key Property**: Sensitive to outliers. Large errors are penalized more due to squaring.
- **Example applications**:

    - Predicting house prices
    - Estimating sales revenue
    - Forecasting temperature

## Formula

=== "Normal"

    <img src="image8.jpg" style="width:4.5in" />

=== "Regularized"

    <img src="image6.png" style="width:3.5in" />

## Gradient Descent

=== "Normal"

    <img src="image1.jpg" style="width:3.5in" />

=== "Regularized"

    <img src="image3.png" style="width:3.5in" />

## Sample Derivative Calculation for Linear Regression

=== "1. Cost Function"

    The goal is to find the partial derivatives of the cost function $J(\vec{w}, b)$ with respect to $\vec{w}$ and $b$.

    $$J(\vec{w}, b) = \frac{1}{2m} \sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})^2$$

    Substituting $f_{\vec{w},b}(\vec{x}^{(i)}) = \vec{w} \cdot \vec{x}^{(i)} + b$:

    $$J(\vec{w}, b) = \frac{1}{2m} \sum_{i=1}^{m} (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)})^2$$

=== "2. Derivative With Respect to $\vec{w}$"

    We use the chain rule. Let $u = \vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)}$. We are finding $\frac{\partial}{\partial \vec{w}} [u^2]$.

    $$\frac{\partial J}{\partial \vec{w}} = \frac{1}{2m} \sum_{i=1}^{m} \frac{\partial}{\partial \vec{w}} \left[ (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)})^2 \right]$$

    - **Apply Chain Rule:** $\frac{\partial (u^2)}{\partial \vec{w}} = 2u \cdot \frac{\partial u}{\partial \vec{w}}$
    - **Part 1:** $2u = 2(\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)})$
    - **Part 2:** $\frac{\partial u}{\partial \vec{w}} = \frac{\partial}{\partial \vec{w}} (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)}) = \vec{x}^{(i)}$

    **Combine:**

    $$\frac{\partial J}{\partial \vec{w}} = \frac{1}{2m} \sum_{i=1}^{m} \left[ 2(\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)}) \cdot \vec{x}^{(i)} \right]$$

    **Simplify:** The $\frac{1}{2}$ and $2$ cancel.

    $$\frac{\partial J}{\partial \vec{w}} = \frac{1}{m} \sum_{i=1}^{m} (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)}) \vec{x}^{(i)}$$

    Or, substituting $f_{\vec{w},b}$ back in:

    $$\frac{\partial J}{\partial \vec{w}} = \frac{1}{m} \sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)}) \vec{x}^{(i)}$$

=== "3. Derivative with respect to $b$"

    We use the same chain rule setup. Let $u = \vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)}$. We are finding $\frac{\partial}{\partial b} [u^2]$.

    $$\frac{\partial J}{\partial b} = \frac{1}{2m} \sum_{i=1}^{m} \frac{\partial}{\partial b} \left[ (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)})^2 \right]$$

    - **Apply Chain Rule:** $\frac{\partial (u^2)}{\partial b} = 2u \cdot \frac{\partial u}{\partial b}$
    - **Part 1:** $2u = 2(\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)})$
    - **Part 2:** $\frac{\partial u}{\partial b} = \frac{\partial}{\partial b} (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)}) = 1$

    **Combine:**

    $$\frac{\partial J}{\partial b} = \frac{1}{2m} \sum_{i=1}^{m} \left[ 2(\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)}) \cdot 1 \right]$$

    **Simplify:** The $\frac{1}{2}$ and $2$ cancel.

    $$\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)})$$

    Or, substituting $f_{\vec{w},b}$ back in:

    $$\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})$$

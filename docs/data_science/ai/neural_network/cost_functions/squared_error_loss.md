# Squared Error Loss [Regression]

## Description

Mean squared error (MSE) is the most commonly used loss function for regression. The loss is the mean overseen data of the squared differences between true and predicted values

- **Use case**: Regression problems
- **When to use**: Is typically used when you are solving regression problems where the goal is to predict continuous numerical values. Squaring ensures that both positive and negative differences contribute equally to the loss.
- **Key Property**: Sensitive to outliers. Large errors are penalized more due to squaring.
- **Example applications**:

   - Predicting house prices
   - Estimating sales revenue
   - Forecasting temperature

## Formula

Normal:

<img src="image8.jpg" style="width:2.29411in" />

Regularized:

<img src="image6.png" style="width:3.02841in" />

## Gradient Descent

Normal:

<img src="image1.jpg" style="width:2.81512in" />

Regularized:

<img src="image3.png" style="width:2.68545in" />

## Sample Derivative Calculation for Linear Regression

<img src="image11.gif" style="width:2.875in" />

<img src="image2.gif" style="width:2.80556in" />

<img src="image5.gif" style="width:4.54167in" />

<img src="image10.gif" style="width:5.625in" />

<img src="image4.gif" style="width:4.11111in" />

<img src="image9.gif" style="width:3.73611in" />

<img src="image7.gif" style="width:3.58333in" />

<img src="image12.gif" style="width:3.25in" />

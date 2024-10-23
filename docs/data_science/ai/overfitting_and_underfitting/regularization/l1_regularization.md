# L1 regularization (LASSO)

## Description

**LASSO**, an acronym for **Least Absolute Shrinkage and Selection Operator**, serves as a linear regression technique that's commonly employed for feature selection in machine learning. Its mechanism involves **introducing a penalty term to the standard regression loss function. This penalty encourages the model to reduce the coefficients of less important features to zero**, effectively eliminating them from the model.

The LASSO method proves especially **valuable when grappling with high-dimensional data, where the number of features far exceeds the number of samples**. In such scenarios, discerning the most crucial features for predicting the target variable can be challenging. LASSO comes to the fore by automatically identifying the most relevant features while simultaneously shrinking the coefficients of others.

**LASSO has several advantages over other feature selection methods**, such as its ability to handle correlated features and its ability to perform feature selection and regression simultaneously. However, LASSO has some limitations, such as its tendency to select only one feature from a group of correlated features, and its performance may deteriorate if the number of features is much larger than the number of samples.

## Example

Consider the application of LASSO for feature selection in predicting house prices. Imagine a dataset encompassing details about houses – such as the number of bedrooms, lot size, construction year, and so on – alongside their respective sale prices. Employing LASSO, we can pinpoint the most crucial features to predict the sale price while concurrently fitting a linear regression model to the dataset. The outcome is a model that's ready to forecast the sale price of a new house based on its features.

![](l1_regularization/image2.jpg)

## Formula

The LASSO method works by finding the solution for the following optimization problem, which is a minimization problem:

<img src="image1.png" style="width:2.00388in" />

In the given equation, vector y represents the target variable, X denotes the feature matrix, w signifies the vector of regression coefficients, $\lambda$ is a hyperparameter dictating the intensity of the penalty term, and ||w|| 1 stands for the 𝓁 1 norm of the coefficients (that is, the sum of their absolute values).

The inclusion of the 𝓁 1 penalty term in the objective function prompts the model to precisely zero out certain coefficients, essentially eliminating the associated features from the model. The degree of penalty strength is governed by the $\lambda$ hyperparameter, which can be fine-tuned through the use of cross-validation.

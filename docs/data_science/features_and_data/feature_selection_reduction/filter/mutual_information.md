# Mutual Information (Information Gain) [Not Normal] [Continuous or Categorical]

## Description

Mutual information acts as a metric to gauge the interdependence of two random variables. In the context of feature selection, it quantifies the information a feature provides about the target variable. The core methodology entails calculating the mutual information between each feature and the target variable, ultimately selecting features with the highest mutual information scores.

In the context of feature selection, mutual information calculation involves treating the feature as X and the target variable as Y. By computing the mutual information score for each feature, we can then select features with the highest scores.

In practical applications, mutual information **is often employed alongside other feature selection methods**, such as chi-squared or correlation-based methods, to enhance the overall performance of the feature selection process.

## Formula

Mathematically, the mutual information between two discrete random variables, X and Y, can be defined as follows:

<img src="image1.png" style="width:3.22525in" />

In the given equation, p(x, y) represents the joint probability mass function of X and Y, while p(x) and p(y) denote the marginal probability mass functions of X and Y, respectively.

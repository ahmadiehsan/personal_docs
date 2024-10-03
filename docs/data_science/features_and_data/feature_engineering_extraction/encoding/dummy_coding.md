# Dummy Coding

## Specifications

- **Good for:** Low number of values

## Description

The dummy coding scheme is similar to the one-hot encoding scheme, except in the case of the dummy coding scheme, when applied on a categorical feature with m distinct labels, we get m - 1 binary features. Thus each value of the categorical variable gets converted into a vector of size m - 1. The extra feature is completely disregarded and thus if the category values range from {0, 1, …, m-1} the 0th or the m - 1th feature column is dropped and corresponding category values are usually represented by a vector of all zeros (0).

<img src="image1.jpg" style="width:2.37509in" />

## Example

<img src="image2.jpg" style="width:5.28615in" />

# Linear Discriminant Analysis (LDA) {Linear}

## Description

It is often used in classification tasks to reduce the number of features by transforming them into a lower-dimensional space while retaining as much class-discriminatory information as possible.

In LDA, the goal is to find a linear combination of the original features that maximizes the separation between classes. **The input to LDA is a dataset of labeled examples**, where each example is a feature vector with a corresponding class label.
The output of LDA is a set of linear combinations of the original features, which can be used as new features in a machine learning model.

- Projects data in a way that the class separability is maximised.
- Examples from the same class are put closely together by the projection.
- Examples from different classes are placed far apart by the projection.

<img src="image8.jpg" style="width:3.05039in" />

LDA is particularly useful when the number of features is large and the number of examples is small.
It can be used in a variety of applications, including image recognition, speech recognition, and NLP.
However, it assumes that the classes are normally distributed and that the class covariance matrices are equal, which may not always be the case in practice.

## LDA Steps

To perform LDA, the first step is to compute the mean and covariance matrix of each class.
The overall mean and covariance matrix are then calculated from the class means and covariance matrices.
The goal is to project the data onto a lower-dimensional space while still retaining the class information.
This is achieved by finding the eigenvectors and eigenvalues of the covariance matrix, sorting them in descending order of the eigenvalues, and selecting the top k eigenvectors that correspond to the k largest eigenvalues.
The selected eigenvectors form the basis for the new feature space.

The LDA algorithm can be summarized in the following steps:

1. Compute the mean vector of each class.
2. Compute the covariance matrix of each class.
3. Compute the overall mean vector and overall covariance matrix.
4. Compute the between-class scatter matrix.
5. Compute the within-class scatter matrix.
6. Compute the eigenvectors and eigenvalues of the matrix using the following equation:

  $S_w^{-1} * S_b$

  Here, $S_w$ is the within-class scatter matrix and $S_b$ is the between-class scatter matrix.

7. Select the top k eigenvectors with the highest eigenvalues as the new feature space.

## Workflow

### How LDA Creates New Axis

The new axis created according to two criteria (considered simultaneously)

<img src="image6.jpg" style="width:5in" />

### Why Both Distance & Scatter Are Important

**Distance**: Minimizing the distance between means of two categories

**Scatter**: Minimizing the variation of each category

<img src="image5.jpg" style="width:4.09907in" />

### LDA With 3 Features

LDA will reduce the number of features to: **Number of categories - 1**

<img src="image4.jpg" style="width:3.39152in" />

<img src="image7.jpg" style="width:3.40602in" />

### LDA With 3 Categories

LDA will reduce the dimensionality to: **Number of categories - 1**

<img src="image2.jpg" style="width:3.24826in" />

<img src="image1.jpg" style="width:3.77141in" />

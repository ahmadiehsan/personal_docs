# Principal Component Analysis (PCA) {Linear}

## Description

The idea of PCA is simple — **reduce the number of variables of a data set, while preserving as much information as possible**.

The basic idea of PCA is to transform a set of correlated variables into a set of uncorrelated variables known as principal components.

It's good for **unsupervised continuous data**.

When faced with the issue of high-dimensional, unlabeled data (e.g., hundreds to thousands of columns), you can employ unsupervised **dimensionality reduction** techniques.
One of the most common unsupervised learning methods of dimensionality reduction is principal component analysis (PCA).
PCA represents a data set with a large number of columns and a smaller data set with fewer columns, called principal components.
These can then analyze trends, clusters, and outliers and help frame a supervised learning problem.

PCA can be used for feature selection by selecting the top k principal components that explain the most variance in the data.
This can be useful for reducing the dimensionality of high-dimensional datasets and improving the performance of machine learning models.
However, it's important to note that PCA may not always lead to improved performance, especially if the data is already low-dimensional or if the features are not highly correlated. It's also important to consider the interpretability of the selected principal components as they may not always correspond to meaningful features in the data.

## Workflow

Principal components are new variables that are constructed as linear combinations or mixtures of the initial variables.
These combinations are done in such a way that the new variables (i.e., principal components) are uncorrelated and most of the information within the initial variables is squeezed or compressed into the first components.
So, the idea is that 10-dimensional data gives you 10 principal components.
Still, PCA tries to put the maximum possible information in the first component, then the maximum remaining information in the second, and so on.

An important thing to realize here is that the principal components are less interpretable and don't have any real meaning since they are constructed as linear combinations of the initial variables.

As there are as many principal components as there are variables in the data, principal components are constructed in such a manner that the first principal component accounts for the largest possible variance in the data set.

![](principal_component_analysis/image1.gif)

For example in the above image, the first principal component approximately is the line that matches the purple marks because it goes through the origin and it's the line in which the projection of the points (red dots) is the most spread out.

The second principal component is calculated in the same way, with the condition that it is uncorrelated with (i.e., perpendicular to) the first principal component and that it accounts for the next highest variance.

This continues until a total of principal components have been calculated, equal to the original number of variables.

It is eigenvectors and eigenvalues that are behind all the magic explained above, because the eigenvectors of the Covariance matrix are actually the directions of the axes where there is the most variance(most information) and that we call Principal Components.
And eigenvalues are simply the coefficients attached to eigenvectors, which give the amount of variance carried in each Principal Component.

## PCA Steps

The PCA algorithm involves the following steps:

1. Standardize the data: PCA requires the data to be standardized – that is, each feature must have zero mean and unit variance.
2. Compute the covariance matrix: The covariance matrix is a square matrix that measures the linear relationships between pairs of features in the data.
3. Compute the eigenvectors and eigenvalues of the covariance matrix: The eigenvectors represent the primary directions of the highest variance within the dataset, while the eigenvalues quantify the extent of variance elucidated by each eigenvector.
4. Select the number of principal components: The number of principal components to retain can be determined by analyzing the eigenvalues and selecting the top k eigenvectors that explain the most variance.
5. Project the data onto the selected principal components: The original data is projected onto the selected principal components, resulting in a lower-dimensional representation of the data.

## Vs Random Forest

- In each of the supervised learning use cases, the random forest can be used to reduce the number of dimensions in data.
- For unsupervised dimensionality reduction tasks, PCA can be helpful.

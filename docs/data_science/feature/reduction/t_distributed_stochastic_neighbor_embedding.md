# T-Distributed Stochastic Neighbor Embedding (T-SNE) {Manifold}

## Description

Computes the probability that pairs of data points in the high-dimensional space are related and then chooses a low-dimensional embedding that produces a similar distribution.

The basic idea behind t-SNE is to preserve the pairwise similarities of data points in a low-dimensional space, as opposed to preserving the distances between them. In other words, it tries to retain the local structure of the data while discarding the global structure. This can be useful in situations where the high-dimensional data is difficult to visualize, but there may be meaningful patterns and relationships among the data points.

t-SNE is a powerful technique for visualizing high-dimensional data by reducing it to a low-dimensional space. However, it is not typically used for feature selection as its primary purpose is to create visualizations of complex datasets.

t-SNE can be used to help identify clusters of data points that share similar features, which may be useful in identifying groups of features that are important for a particular task.

It's worth noting that **t-SNE is primarily a visualization tool and should not be used as the sole method for feature selection.** Instead, it can be used in conjunction with other techniques, such as LDA or PCA, to gain a more complete understanding of the underlying structure of your data.

## Workflow

t-SNE starts by calculating the pairwise similarity between each pair of data points in the highdimensional space. The similarity is usually measured using a Gaussian kernel, which gives higher weights to nearby points and lower weights to distant points. The similarity matrix is then converted into a probability distribution using a softmax function. This distribution is used to create a low-dimensional space, typically 2D or 3D.

In the low-dimensional space, t-SNE again calculates the pairwise similarities between each pair of data points, but this time using a student's t-distribution instead of a Gaussian distribution. The t-distribution has heavier tails than the Gaussian distribution, which helps to better preserve the local structure of the data. t-SNE then adjusts the position of the points in the low-dimensional space to minimize the difference between the pairwise similarities in the high-dimensional space and the pairwise similarities in the low-dimensional space.

## Example

Suppose you have a dataset of customer demographics and purchase history, and you want to identify groups of customers that are similar based on their purchasing behavior. You could use t-SNE to reduce the high-dimensional feature space to two dimensions, and then plot the resulting data points on a scatter plot. By examining the plot, you might be able to identify clusters of customers with similar purchasing behavior, which could then inform your feature selection process. Here's a sample t-SNE for the MNIST dataset:

<img src="image1.jpg" style="width:3.7583in" />

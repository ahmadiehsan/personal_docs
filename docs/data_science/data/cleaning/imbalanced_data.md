# Imbalanced Data {SMOTE} {NearMiss}

## Description

In general, we can have three categories of methods to handle imbalanced datasets:

- **Undersampling**: To use fewer training records from the majority class.
- **Resampling**: Modifying the original dataset to create a balanced distribution. This can be achieved by either **oversampling** the minority class (creating more samples of the minority class) or undersampling the majority class (removing samples from the majority class).
- **Handling imbalanced datasets in machine learning models**: Such as modifying cost function, or modified batching in deep learning models.

Oversampling techniques include:

- Random oversampling
- Synthetic Minority Oversampling Technique (SMOTE)
- Adaptive Synthetic Sampling (ADASYN)

Undersampling techniques include:

- Random undersampling
- Tomek links
- Cluster centroids

## Techniques

### SMOTE (Oversampling)

SMOTE is a widely used algorithm for handling imbalanced datasets in machine learning.
It is a synthetic data generation technique that creates new, synthetic samples in the minority class by interpolating between existing samples.
SMOTE works by identifying the k-nearest neighbors of a minority class sample and then generating new samples along the line segments that connect these neighbors.

Here are the steps of the SMOTE algorithm:

1. Select a minority class sample, $x$.
2. Choose one of its k-nearest neighbors, $x'$.
3. Generate a synthetic sample by interpolating between $x$ and $x'$. To do this, choose a random number, r, between 0 and 1, and then calculate the synthetic sample, as follows:

  $\text{new sample} = x + r^{*}(x' - x)$

  This creates a new sample that is somewhere between $x$ and $x'$, but not the same as either one.

4. Repeat steps 1 to 3 until the desired number of synthetic samples has been generated.

Here are the advantages and disadvantages of SMOTE:

- It helps to address the problem of class imbalance by creating synthetic samples in the minority class.
- Can be combined with other techniques, such as random undersampling or Tomek links, to further improve the balance of the dataset.
- Can be applied to both categorical and numerical data.
- Can sometimes create synthetic samples that are unrealistic or noisy, leading to overfitting.
- Can sometimes cause the decision boundary to be too sensitive to the minority class, leading to poor performance of the majority class.
- Can be computationally expensive for large datasets.

### NearMiss (Undersampling)

The NearMiss algorithm is a technique for balancing class distribution by undersampling (removing) the records from the major class.
When two classes have records that are very close to each other, eliminating some of the records from the majority class increases the distance between the two classes, which helps the classification process.
To avoid information loss problems in the majority of undersampling methods, near-miss methods are widely used.

The working of nearest-neighbor methods is based on the following steps:

1. Find the distances between all records from the major class and minor class. Our goal is to undersample the records from the major class.
2. Choose $n$ records from the major class that are closest to the minor class.
3. If there are $k$ records in the minor class, the nearest method will return $k \times n$ records from the major class.

There are three variations of applying the NearMiss algorithm that we can use to find the n closest records in the major class:

- We can select the records of the major class for which the average distances to the k-closest records of the minor class are the smallest.
- We can select the records of the major class for which the average distances to the k-farthest records of the minor class are the smallest.
- We can implement two steps. In the first step, for each record from the minor class, their M nearest neighbors will be stored. Then, the records from the major class are selected such that the average distance to the N nearest neighbors is the largest.

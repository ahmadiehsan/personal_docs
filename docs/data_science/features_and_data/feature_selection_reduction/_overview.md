# Overview

## The Curse of Dimensionality

We care because the curse of dimensionality demands that we do. The curse of dimensionality refers to all the problems that arise when working with data in the higher dimensions that did not exist in the lower dimensions.

<img src="image1.jpg" style="width:3.31667in" />

As the number of features increases, the number of samples also increases proportionally. The more features we have, the more samples we will need to have all combinations of feature values well represented in our sample.

## Various Solutions

### Dimensionality Reduction

Dimensionality reduction is the process of transforming high-dimensional data into a lower-dimensional format while preserving its most important properties. This technique has applications in many industries including quantitative finance, healthcare, and drug discovery.

### Feature Selection

Simply speaking, feature selection is about selecting a subset of features out of the original features to reduce model complexity, enhance the computational efficiency of the models, and reduce generalization error introduced due to noise by irrelevant features.

Is the process of identifying and selecting relevant features for your sample.

- Heat maps that show the correlation between features are a good idea.
- So is just visualizing the relationship between the features and the target variable by plotting each feature against the target variable.

### Feature extraction

Is about extracting/deriving information from the original features set to create a new features subspace. The primary idea behind feature extraction is to compress the data to maintain most of the relevant information. As with feature selection techniques, these techniques are also used for reducing the number of features from the original features set to reduce model complexity, and model overfitting, enhance model computation efficiency, and reduce generalization error.

### Feature Selection vs Feature Extraction

The key difference between feature selection and feature extraction techniques used for dimensionality reduction is that while the original features are maintained in the case of feature selection algorithms, the feature extraction algorithms transform the data onto a new feature space.

Feature selection techniques can be used if the requirement is to maintain the original features, unlike the feature extraction techniques which derive useful information from data to construct a new feature subspace. Feature selection techniques are used when model explainability is a key requirement.

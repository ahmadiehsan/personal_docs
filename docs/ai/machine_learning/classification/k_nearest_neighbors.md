# K-Nearest Neighbors (KNN) [Sup]

## Description

Is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point.

<img src="image2.jpg" style="width:5.22689in" />

For example in the above image, the big red circle at first was unclassified and by using KNN it was classified by the nearest old classified data.

## The Best Number For K

- There is no physical or biological way to determine the best value for "K", so you may have to try out a few values before settling on one. Do this by pretending part of the training data is "unknown".
- Low values for K (like K=1 or K=2) can be noisy and subject to the effects of outliers.
- Large values for K smooth over things, but you don't want K to be so large that a category with only a few samples in it will always be outvoted by other categories.

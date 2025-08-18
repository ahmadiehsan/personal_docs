# Stratified K-Fold

## Description

In some cases, there may be a large imbalance in the response variables.
For example, in a dataset concerning the price of houses, there might be a large number of houses having high prices.
Or in case of classification, there might be several times more negative samples than positive samples.
For such problems, a slight variation in the K Fold cross validation technique is made, such that each fold contains approximately the same percentage of samples of each target class as the complete set, or in case of prediction problems, the mean response value is approximately equal in all the folds.
This variation is also known as Stratified K Fold.

<img src="image1.jpg" style="width:2.027in" />

# Gini [Binary Classification] [Tree]

## Description

A node's Gini value represents its Gini impurity, which measures how mixed the classes are within that node.
A node is considered pure (Gini = 0) when all the data points it contains belong to the same class.
For instance, if a node includes only samples from one category, its impurity is zero.
In contrast, nodes that contain samples from multiple categories are impure, having higher Gini values.

## Formula

$$
G_i = 1 - \sum_{k=1}^{n} p_{i,k}^2
$$

- $G_i$: Gini impurity of the $i$-th node
- $p_{i,k}$: Ratio of instances of class $k$ among the training samples in the $i$-th node
- $n$: Total number of classes

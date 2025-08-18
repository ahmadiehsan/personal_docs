# Support Vector Machine (SVM)

## Description

The support vector machine is a model used for both classification and regression problems though it is mostly used to solve classification problems.
The algorithm creates a hyperplane or line (decision boundary) which separates data into classes.
It uses the kernel trick to find the best line separator (decision boundary that has the same distance from the boundary point of both classes).

SVM tries to finds the maximal margin (distance between the line and the support vectors) that separates the classes and this reduces the risk of error on the data

<img src="image4.jpg" style="width:3in" />

- $H_1$ does not separate the classes.
- $H_2$ does, but only with a small margin.
- $H_3$ separates them with the maximal margin.

## Hyperplane

A hyperplane is a decision boundary that differentiates the two classes in SVM.
A data point falling on either side of the hyperplane can be attributed to different classes.
The dimension of the hyperplane depends on the number of input features in the dataset.

<img src="image9.png" style="width:2.53833in" />

In geometry, a hyperplane is a subspace whose dimension is one less than that of its ambient space.
For example, if a space is 3-dimensional then its hyperplanes are the 2-dimensional planes, while if the space is 2-dimensional, its hyperplanes are the 1-dimensional lines.

## Soft Margin

Soft margin SVM allows some misclassification to happen by relaxing the hard constraints of Support Vector Machine.

<img src="image3.jpg" style="width:3.54212in" />

<img src="image1.jpg" style="width:3.48459in" />

<img src="image11.jpg" style="width:3.4371in" />

## SVM Functionality For Weird Shaped Data

SVM by using a **kernel function** will move the data into a higher dimension to make the classification possible.

<img src="image10.jpg" style="width:3.54322in" />

<img src="image12.jpg" style="width:3.53186in" />

<img src="image8.jpg" style="width:3.59745in" />

## Kernel Function

<img src="image7.jpg" style="width:3.71837in" />

<img src="image6.jpg" style="width:3.75761in" />

<img src="image5.jpg" style="width:2.97164in" />

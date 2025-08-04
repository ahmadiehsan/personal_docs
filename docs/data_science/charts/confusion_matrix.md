# Confusion Matrix (Error Matrix) {Categorical}

## Description

A confusion matrix is a table that is used to define the performance of a classification algorithm.

<img src="image3.jpg" style="width:5.5in" />

- True positive: The real value is T and the predicted value is T
- False positive (type I error): The real value is F but the predicted value is T
- True negative: The real value is F and the predicted value is F
- False negative (type II error): The real value is F but the predicted value is T

A confusion matrix visualizes and summarizes the performance of a classification algorithm.

<img src="image2.jpg" style="width:4.5in" />

Is a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually called a matching matrix). Each row of the matrix represents the instances in an actual class while each column represents the instances in a predicted class, or vice versa – both variants are found in the literature. The name stems from the fact that it makes it easy to see whether the system is confusing two classes (i.e. commonly mislabeling one as another).

The size of the confusion matrix will be determined by the number of things we want to predict. For example, in the below table, we will have a 3*3 matrix (Troll 2, Gore Police, Cool As Ice).

<img src="image1.jpg" style="width:3.5in" />

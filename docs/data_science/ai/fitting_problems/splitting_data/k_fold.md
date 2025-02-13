# K-Fold

## Description

As there is never enough data to train your model, removing a part of it for validation poses a problem of underfitting. By reducing the training data, we risk losing important patterns/trends in the data set, which in turn increases error induced by bias. So, what we require is a method that provides ample data for training the model and also leaves ample data for validation. K Fold cross validation does exactly that.

In K Fold cross validation, the data is divided into k subsets. Now the **holdout method** is repeated k times, such that each time, one of the k subsets is used as the test-set/validation-set and the other k-1 subsets are put together to form a training set. The error estimation is averaged over all k trials to get total effectiveness of our model.

<img src="image1.png" style="width:5.26427in" />

As can be seen, every data point gets to be in a validation set exactly once, and gets to be in a training set k-1 times. This significantly reduces **bias** as we are using most of the data for fitting, and also significantly reduces **variance** as most of the data is also being used in validation sets. Interchanging the training and test sets also adds to the effectiveness of this method.

As a general rule and empirical evidence, **K=5** or **10** is generally preferred, but nothing's fixed and it can take any value.

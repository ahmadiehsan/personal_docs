# Leave-P-Out

## Description

This approach leaves p data points out of training data, i.e. if there are n data points in the original sample then, n-p samples are used to train the model and p points are used as the validation set.
This is repeated for all combinations in which the original sample can be separated this way, and then the error is averaged for all trials, to give overall effectiveness.

<img src="image1.png" style="width:4.52997in" />

This method is exhaustive in the sense that it needs to train and validate the model for all possible combinations, and for moderately large p, it can become computationally infeasible.

A particular case of this method is when p=1.
This is known as Leave one out cross validation.
This method is generally preferred over the previous one because it does not suffer from the intensive computation, as the number of possible combinations is equal to the number of data points in the original sample or n.

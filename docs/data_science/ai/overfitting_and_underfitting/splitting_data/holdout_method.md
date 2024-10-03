# Holdout Method (Train_Test Split)

## Description

Removing a part of the training data and using it to get predictions from the model trained on the rest of the data.

<img src="image1.jpg" style="width:3.0434in" />

This is a simple kind of cross validation technique, also known as the holdout method.

Although this method doesn’t take any overhead to compute and is better than traditional validation, it still suffers from issues of high variance. This is because it is not certain which data points will end up in the validation set and the result might be entirely different for different sets.

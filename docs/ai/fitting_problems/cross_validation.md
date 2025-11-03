# Cross-Validation {Holdout} {K-Fold}

## Description

Cross-Validation means dividing a dataset into parts for training and testing a model, helping to evaluate its performance and avoid overfitting.

## Varieties

=== "Holdout"

    Holdout (Train/Test Split) is removing a part of the training data and using it to get predictions from the model trained on the rest of the data.

    <img src="holdout_overview.jpg" style="width:3.5in" />

    This is a simple kind of cross validation technique, also known as the holdout method.

    Although this method doesn't take any overhead to compute and is better than traditional validation, it still suffers from issues of high variance.
    This is because it is not certain which data points will end up in the validation set and the result might be entirely different for different sets.

=== "K-Fold"

    As there is never enough data to train your model, removing a part of it for validation poses a problem of underfitting.
    By reducing the training data, we risk losing important patterns/trends in the data set, which in turn increases error induced by bias.
    So, what we require is a method that provides ample data for training the model and also leaves ample data for validation.
    K Fold cross validation does exactly that.

    In K Fold cross validation, the data is divided into k subsets.
    Now the **holdout method** is repeated k times, such that each time, one of the k subsets is used as the test-set/validation-set and the other k-1 subsets are put together to form a training set.
    The error estimation is averaged over all k trials to get total effectiveness of our model.

    <img src="k_fold_overview.png" style="width:5in" />

    As can be seen, every data point gets to be in a validation set exactly once, and gets to be in a training set k-1 times.
    This significantly reduces **bias** as we are using most of the data for fitting, and also significantly reduces **variance** as most of the data is also being used in validation sets.
    Interchanging the training and test sets also adds to the effectiveness of this method.

    As a general rule and empirical evidence, **K=5** or **10** is generally preferred, but nothing's fixed and it can take any value.

=== "Stratified K-Fold"

    In some cases, there may be a large imbalance in the response variables.
    For example, in a dataset concerning the price of houses, there might be a large number of houses having high prices.
    Or in case of classification, there might be several times more negative samples than positive samples.
    For such problems, a slight variation in the K Fold cross validation technique is made, such that each fold contains approximately the same percentage of samples of each target class as the complete set, or in case of prediction problems, the mean response value is approximately equal in all the folds.
    This variation is also known as Stratified K Fold.

    <img src="stratified_k_fold_overview.jpg" style="width:3in" />

=== "Leave-P-Out"

    This approach leaves p data points out of training data, i.e. if there are n data points in the original sample then, n-p samples are used to train the model and p points are used as the validation set.
    This is repeated for all combinations in which the original sample can be separated this way, and then the error is averaged for all trials, to give overall effectiveness.

    <img src="leave_p_out_overview.png" style="width:5.5in" />

    This method is exhaustive in the sense that it needs to train and validate the model for all possible combinations, and for moderately large p, it can become computationally infeasible.

    A particular case of this method is when p=1.
    This is known as Leave one out cross validation.
    This method is generally preferred over the previous one because it does not suffer from the intensive computation, as the number of possible combinations is equal to the number of data points in the original sample or n.

=== "Time Series Cross-Validation"

    Time series data requires special attention when splitting.
    In this case, we typically use a method called time series cross-validation, which preserves the temporal order of the data.
    In this method, the data is split into multiple segments, with each segment representing a fixed time interval.
    The model is then trained on the past data and tested on the future data.
    This helps to evaluate the performance of the model in real-world scenarios.

    <img src="time_series_cross_validation_overview.jpg" style="width:4in" />

    In all cases, it's important to ensure that the split is done randomly but with the same random seed each time to ensure the reproducibility of the results.
    It's also important to ensure that the split is representative of the underlying data – that is, the distribution of the target variable should be consistent across all sets.
    Once we have split the data into different subsets for training and testing our model, we can try to find the best set of hyperparameters for our model.

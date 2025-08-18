# Overview

## Description

This process of deciding whether the numerical results quantifying hypothesized relationships between variables are acceptable as descriptions of the data, is known as validation.

Generally, an error estimation for the model is made after training, better known as evaluation of residuals.
In this process, a numerical estimate of the difference in predicted and original responses is done, also called the training error.
However, this only gives us an idea about how well our model does on data used to train it.
Now it's possible that the model is underfitting or overfitting the data. So, the problem with this evaluation technique is that it does not give an indication of how well the learner will generalize to an independent/unseen data set. Getting this idea about our model is known as Cross Validation.

Choosing the right loss function is crucial for effectively optimizing your model for the task at hand!

Popular functions:

| Loss Function      | Typical Use Case                      | Notes                                                                 |
|--------------------|---------------------------------------|-----------------------------------------------------------------------|
| Squared Error Loss | Regression                            | Sensitive to outliers due to squaring                                 |
| Log Loss           | Binary Classification                 | Optimized for probabilistic models and binary outcomes                |
| Distortion         | Signal Processing/Compression Quality | Measures fidelity or degradation between inputs and outputs           |
| Cross-Entropy Loss | Multi-Class Classification            | Focuses on probability distributions (often used with softmax output) |

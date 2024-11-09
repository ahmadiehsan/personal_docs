# Training CV

## Description

Means using all possible hyperparameters in each try.

Creating and testing a CV will be done with the following steps:

1. **Define the hyperparameters and their search space**: Identify the hyperparameters you want to optimize and specify the range of possible values for each of them.
2. **Choose a search strategy**: Select a method to explore the hyperparameter search space, such as:

   1. Grid search: systematically evaluates all combinations of hyperparameter values.
   2. Random search: samples random combinations within the search space.
   3. Bayesian optimization: uses a probabilistic model to guide the search, balancing exploration and exploitation based on the model's predictions.

3. **Perform the search**: For each combination of hyperparameter values, train a model on the training data, and evaluate its performance.
4. **Select the best hyperparameters**: After the search is complete, select the hyperparameter combination that yields the best performance on the evaluation metric.

# Training CV

## Description

Training a CV involves testing all possible hyperparameters in each attempt. The process consists of the following steps:

1. **Define the hyperparameters and their search space**: Identify the hyperparameters to optimize and specify their possible value ranges.
2. **Choose a search strategy**: Select a method to explore the hyperparameter search space, such as:

   - **Grid search**: Systematically evaluates all possible hyperparameter combinations.
   - **Random search**: Samples random combinations within the search space.
   - **Bayesian optimization**: Uses a probabilistic model to guide the search, balancing exploration and exploitation.

3. **Perform the search**: Train a model using each combination of hyperparameter values and evaluate its performance.
4. **Select the best hyperparameters**: Choose the combination that achieves the best performance based on the evaluation metric.

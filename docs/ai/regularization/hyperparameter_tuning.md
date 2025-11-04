# Hyperparameter Tuning

## Description

Hyperparameter tuning is the process of finding the best settings for a model to achieve optimal performance.

## Varieties

=== "Training CV"

    Training a CV involves testing all possible hyperparameters in each attempt.
    The process consists of the following steps:

    1. **Define the hyperparameters and their search space**: Identify the hyperparameters to optimize and specify their possible value ranges.
    2. **Choose a search strategy**: Select a method to explore the hyperparameter search space, such as:

        - **Grid search**: Systematically evaluates all possible hyperparameter combinations.
        - **Random search**: Samples random combinations within the search space.
        - **Bayesian optimization**: Uses a probabilistic model to guide the search, balancing exploration and exploitation.

    3. **Perform the search**: Train a model using each combination of hyperparameter values and evaluate its performance.
    4. **Select the best hyperparameters**: Choose the combination that achieves the best performance based on the evaluation metric.

## Example

=== "Training CV (Grid)"

    ```python
    from sklearn.model_selection import GridSearchCV

    full_pipeline = Pipeline([
        ("preprocessing", preprocessing),
        ("random_forest", RandomForestRegressor(random_state=42)),
    ])
    param_grid = [
        {"preprocessing__geo__n_clusters": [5, 8, 10], "random_forest__max_features": [4, 6, 8]},
        {"preprocessing__geo__n_clusters": [10, 15], "random_forest__max_features": [6, 8, 10]},
    ]
    grid_search = GridSearchCV(full_pipeline, param_grid, cv=3, scoring="neg_root_mean_squared_error")
    grid_search.fit(housing, housing_labels)

    print(grid_search.best_params_)
    print(grid_search.cv_results_)
    ```

    !!! info

        The GridSearchCV process in this example:

        1. First dictionary: $3 \times 3 = 9$ combinations (3 values each for n_clusters and max_features)
        2. Second dictionary: $2 \times 3 = 6$ combinations (2 values for n_clusters, 3 for max_features)
        3. Total combinations: $9 + 6 = 15$ parameter sets
        4. With 3-fold cross-validation: $15 \times 3 = 45$ total training rounds

=== "Training CV (Randomized)"

    ```python
    from sklearn.model_selection import RandomizedSearchCV
    from scipy.stats import randint

    full_pipeline = Pipeline([
        ("preprocessing", preprocessing),
        ("random_forest", RandomForestRegressor(random_state=42)),
    ])
    param_distribs = {
        "preprocessing__geo__n_clusters": randint(low=3, high=50),
        "random_forest__max_features": randint(low=2, high=20)
    }
    rnd_search = RandomizedSearchCV(
        full_pipeline,
        param_distributions=param_distribs,
        n_iter=10,
        cv=3,
        scoring="neg_root_mean_squared_error",
        random_state=42
    )
    rnd_search.fit(housing, housing_labels)

    print(rnd_search.best_params_)
    print(rnd_search.cv_results_)
    ```

    !!! info

        RandomizedSearchCV is typically preferred over GridSearchCV for large hyperparameter spaces. Instead of exhaustively trying all combinations, it evaluates a fixed number of random combinations. This approach offers several advantages:

        - Better exploration of continuous parameters: Can test many more values per parameter
        - Efficiency with less important parameters: Adding an irrelevant parameter doesn't multiply training time
        - Flexible iteration control: Can specify any number of iterations, avoiding combinatorial explosion

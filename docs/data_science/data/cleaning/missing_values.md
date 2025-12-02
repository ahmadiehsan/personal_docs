# Missing Values

## Description

Missing data is a common problem that occurs in many machine-learning projects.
Dealing with missing data is important because ML models cannot handle missing data and will either produce errors or provide inaccurate results.

!!! warning

    Filling in values without understanding the pattern of missingness can introduce bias and weaken model performance. For example, using mean imputation on MNAR data may distort the true distribution and reduce predictive power.

## Types of Missing Data

<img src="types.png" style="width:400px" />

Understanding why data is missing is crucial before choosing a handling strategy.
Missing values typically fall into three categories:

- **Missing Completely At Random (MCAR)**: Missingness is unrelated to any data. Safe to drop if few.

    - *Example*: Random technical glitch causes missing values.

- **Missing At Random (MAR)**: Missingness depends on other observed variables, not the missing value itself.

    - *Example*: Students are more likely to have missing income data. Imputation based on related features is appropriate.

- **Missing Not At Random (MNAR)**: Missingness depends on the value itself.

    - *Example*: High incomes are more likely to be missing. Imputation is risky; consider using a missingness indicator or advanced models.

## Methods

=== "Deletion"

    - **Dropping rows (Listwise deletion)**: Remove rows with missing values. Use when missingness is random and affects a small portion of the data.
    - **Pairwise deletion**: Use available values for calculations (e.g., correlations) without dropping entire rows.
    - **Dropping columns**: Remove columns with many missing values, especially if they are not important for analysis. Perform correlation analysis before dropping important columns.

=== "Imputation"

    - **Mean/median/mode imputation**: Substitute missing values with the mean, median, or mode of the column. Suitable for numeric or categorical columns, depending on distribution. Easy to implement, but may introduce bias.
    - **Arbitrary value imputation**: Fill missing values with a constant (e.g., 0 or "Unknown") if contextually appropriate.
    - **Forward/backward fill**: For time series data, fill missing values using previous or next values to maintain temporal consistency.

=== "Advanced Imputation"

    - **Regression imputation**: Predict missing values using regression models based on other variables.
    - **Multiple imputation**: Generate multiple imputed datasets using statistical models and combine results for robust analysis.
    - **K-nearest neighbor (KNN) imputation**: Impute missing values using the mean or median of the k-nearest data points.
    - **Iterative imputer**: Build a model with other columns to estimate missing values iteratively.
    - **Interpolation**: For numeric sequences, estimate missing values based on trends in the data.

=== "Using Missingness as a Feature"

    - **Missingness indicator**: Add a binary column (e.g., `was_missing = 1`) to flag missing values if the fact that a value is missing may carry information.

=== "Oversampling/Undersampling"

    - **Resampling**: If missing data causes class imbalance, use oversampling or undersampling to maintain a fair target distribution.

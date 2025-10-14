# Outliers

## Description

Outliers are data points that markedly deviate from the rest of the observations in a dataset.
Their occurrence may stem from factors such as measurement errors, data corruption, or authentic extreme values.
The presence of outliers can wield a substantial influence on the outcomes of ML models, introducing distortion to the data and disrupting the relationships between variables.
Therefore, handling outliers is an important step in preprocessing data for ML.

## Methods

=== "Removing"

    One straightforward approach involves eliminating observations identified as outliers from the dataset.
    Nevertheless, exercising caution is paramount when adopting this method as excessive removal of observations may result in the loss of valuable information and potentially introduce bias to the analysis results.

=== "Transforming data"

    Applying mathematical functions such as logarithms or square roots to transform the data can mitigate the influence of outliers.
    For instance, taking the logarithm of a variable can alleviate the impact of extreme values, given the slower rate of increase in the logarithmic scale compared to the original values.

=== "Winsorizing"

    Winsorizing is a technique that entails substituting extreme values with the nearest highest or lowest value in the dataset.
    Employing this method aids in maintaining the sample size and overall distribution of the data.

=== "Imputing"

    Imputation involves replacing missing or extreme values with estimated values derived from the remaining observations in the dataset.
    For instance, substituting extreme values with the median or mean of the remaining observations is a common imputation technique.

=== "Using robust statistical methods"

    Robust statistical methods exhibit lower sensitivity to outliers, leading to more accurate results even in the presence of such extreme values.
    For instance, opting for the median instead of the mean can effectively diminish the influence of outliers on the final results.

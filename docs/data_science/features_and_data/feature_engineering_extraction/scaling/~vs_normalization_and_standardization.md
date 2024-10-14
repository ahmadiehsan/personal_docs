# Vs (Normalization & Standardization)

## Description

| Normalization                                                                             | Standardization                                                                                   |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum and maximum value of features are used for scaling                                | Mean and standard deviation is used for scaling.                                                  |
| It is used when features are of different scales.                                         | It is used when we want to ensure zero mean and unit standard deviation.                          |
| Scales values between [0, 1] or [-1, 1].                                                  | It is not bounded to a certain range.                                                             |
| It is really affected by outliers.                                                        | It is much less affected by outliers.                                                             |
| Scikit-Learn provides a transformer called `MinMaxScaler` for Normalization.              | Scikit-Learn provides a transformer called `StandardScaler` for standardization.                  |
| This transformation squishes the n-dimensional data into an n-dimensional unit hypercube. | It translates the data to the mean vector of original data to the origin and squishes or expands. |

- Min-max normalization guarantees all features will have the exact same scale but does not handle outliers well.
- Z-score normalization handles outliers, but does not produce normalized data with the exact same scale.

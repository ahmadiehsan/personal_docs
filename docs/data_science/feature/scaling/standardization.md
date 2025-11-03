# Standardization (Z-score) *

## Description

Standardization (Z-score) refers to the process of normalizing every value in a dataset such that the mean of All the values is 0 and the standard deviation is 1.

This technique transforms the feature values to have a mean of 0 and a standard deviation of 1.

!!! info

    - Standardization is less affected by outliers in the data than min-max scaling.
    - Unlike min-max scaling, standardization does not restrict values to a specific range.

## Formula

$$
Z = \frac{x - \mu}{\sigma}
$$

- $Z$ = standard score
- $x$ = observed value
- $\mu$ = mean of the sample
- $\sigma$ = standard deviation of the sample

## Example

=== "Code"

    ```python
    from sklearn.preprocessing import StandardScaler

    std_scaler = StandardScaler()
    housing_num_std_scaled = std_scaler.fit_transform(housing_num)
    ```

=== "Text"

    ![](standardization/image1.png)

    <span dir="rtl">مقدار $\sigma$ برابر است با انحراف از معیار (standard deviation)</span>

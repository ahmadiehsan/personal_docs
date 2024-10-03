# Log Transformation

## Specifications

- **Data Type:** Continuous numeric data
- **Good For:** Non-Gaussian to Gaussian

## Description

This technique is used when the **data is highly skewed** or **has a long tail**. By taking the logarithm of the feature values, the distribution can be made more normal or symmetric, which can improve the performance of some machine learning algorithms.

This function has a prerequisite that **the numeric values to be transformed must be positive** (similar to what power transform (Box-Cox) expects).

Log transforms are useful when applied to skewed distributions as they tend to expand the values that fall in the range of lower magnitudes and tend to compress or reduce the values that fall in the range of higher magnitudes. This tends to make the skewed distribution as normal as possible.

<img src="image1.jpg" style="width:3.79794in" />

It’s important to note that the logarithmic transformation is not appropriate for all types of data. For example, **if the data includes zero or negative values**, the logarithmic transformation cannot be applied directly. In these cases, a modified logarithmic transformation, such as adding a constant before taking the logarithm, may be used.

## Formula

<img src="image2.jpg" style="width:1.53333in" />

Here, x is the original feature value.

## Example

![](log_transformation/image3.jpg)

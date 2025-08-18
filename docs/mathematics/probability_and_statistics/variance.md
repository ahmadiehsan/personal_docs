# Variance

## Description

Variance is a statistical measure that quantifies the amount of variation or dispersion of a set of data points around its mean (average) value.
It essentially indicates how spread out the data is.

A higher variance suggests that the data points are more scattered, while a lower variance indicates that the data points are clustered closer to the mean.

<img src="image1.jpg" style="width:4.5in" />

!!! info

    High variance is better than low variance **because that feature carries more meaning**, as long as it’s meaningful and not just outliers.

## Formula

The variance is the average value of the squared difference between the random variable and its expectation

$$
\text{Var}(X) = E[(X - E[X])^2]
$$

Or in other shape:

Variance is the expectation of the squared deviation of a random variable from its population mean or sample mean.

$$
S^2 = \frac{\sum{(x_i - \bar{x})^2}}{n - 1}
$$

- $S^2$ = sample variance
- $x_i$ = the value of one observation
- $\bar{x}$ = the mean value of all observations
- $n$ = the number of observations

## Vs Mean

The mean is the average of a group of numbers, and the variance measures the average degree to which each number is different from the mean.

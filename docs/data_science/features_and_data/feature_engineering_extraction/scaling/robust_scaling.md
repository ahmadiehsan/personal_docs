# Robust Scaling

## Description

This technique is similar to standardization but uses the median and interquartile range (IQR) instead of the mean and standard deviation. Robust scaling is useful when the data contains outliers that would significantly affect the mean and standard deviation.

## Formula

<img src="image1.jpg" style="width:3.6375in" />

Here, x is the original feature value, median(x) is the median of the feature, Q1(x) is the first quartile of the feature, and Q3(x) is the third quartile of the feature.
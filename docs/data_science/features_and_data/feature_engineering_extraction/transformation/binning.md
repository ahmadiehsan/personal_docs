# Binning (Quantization)

## Specifications

- **Data Type:** Continuous numeric data

## Description

The problem of working with raw, continuous numeric features is that often the distribution of values in these features will be skewed. This signifies that some values will occur quite frequently while some will be quite rare. Besides this, there is also another problem of the varying range of values in any of these features. For instance view counts of specific music videos could be abnormally large (Despacito we’re looking at you!) and some could be really small. Directly using these features can cause a lot of issues and adversely affect the model. Hence there are strategies to deal with this, which include binning and transformations.

Binning, also known as quantization, is used for transforming continuous numeric features into discrete ones (categories). These discrete values or numbers can be thought of as categories or bins into which the raw, continuous numeric values are binned or grouped into. Each bin represents a specific degree of intensity and hence a specific range of continuous numeric values fall into it. Specific strategies of binning data include fixed-width and adaptive binning.

## Fixed-Width Binning

Description:

Just like the name indicates, in fixed-width binning, we have specific fixed widths for each of the bins which are usually pre-defined by the user analyzing the data. Each bin has a pre-fixed range of values which should be assigned to that bin on the basis of some domain knowledge, rules or constraints. Binning based on rounding is one of the ways, where you can use the rounding operation which we discussed earlier to bin raw values.

Example:

<img src="image1.jpg" style="width:1.28621in" />

<img src="image4.jpg" style="width:5.70689in" />

## Adaptive Binning

Description:

The drawback in using fixed-width binning is that due to us manually deciding the bin ranges, we can end up with irregular bins which are not uniform based on the number of data points or values which fall in each bin. Some of the bins might be densely populated and some of them might be sparsely populated or even empty! Adaptive binning is a safer strategy in these scenarios where we let the data speak for itself! That’s right, we use the data distribution itself to decide our bin ranges.

Quantile based binning is a good strategy to use for adaptive binning. Quantiles are specific values or cut-points which help in partitioning the continuous valued distribution of a specific numeric field into discrete contiguous bins or intervals. Thus, q-Quantiles help in partitioning a numeric attribute into q equal partitions. Popular examples of quantiles include the 2-Quantile known as the median which divides the data distribution into two equal bins, 4-Quantiles known as the quartiles which divide the data into 4 equal bins and 10-Quantiles also known as the deciles which create 10 equal width bins.

Example:

<img src="image3.jpg" style="width:5.36283in" />

The above distribution depicts a right skew in the income with lesser developers earning more money and vice versa.

<img src="image2.jpg" style="width:5.975in" />

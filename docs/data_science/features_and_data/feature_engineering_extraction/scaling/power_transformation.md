# Power Transformation [Box-Cox]

## Specifications

- **Data Type:** Continuous numeric data
- **Good For:** Non-Gaussian to Gaussian

## Description

This technique is similar to log transformation but allows for a broader range of transformations. The most common power transformation is the Box-Cox transformation, which raises the feature values to a power that is determined using maximum likelihood estimation.

## Formula

<img src="image3.jpg" style="width:1.52083in" />

Here, x is the original feature value, and ​λ​ is the power parameter that is estimated using maximum likelihood.

## Box-Cox

The Box-Cox transform is another popular function belonging to the power transform family of functions. **This function has a prerequisite that the numeric values to be transformed must be positive (similar to what log transform expects)**. In case they are negative, shifting using a constant value helps.

<img src="image1.png" style="width:1.96282in" />

The resulting transformed output y is a function of input x and the transformation parameter λ such that when λ = 0, the resultant transform is the natural log transform which we discussed earlier. The optimal value of λ is usually determined using a maximum likelihood or log-likelihood estimation.

<img src="image2.png" style="width:4.04952in" />

## Example

Let’s now apply the Box-Cox transform on our developer income feature. First we get the optimal lambda value from the data distribution by removing the non-null values as follows.

<img src="image4.jpg" style="width:4.03312in" />

Now that we have obtained the optimal λ value, let us use the Box-Cox transform for two values of λ such that λ = 0 and λ = λ(optimal) and transform the developer Income feature.

<img src="image5.jpg" style="width:5.23312in" />

The transformed features are depicted in the above data frame. Just like we expected, Income\_log and Income\_boxcox\_lamba\_0 have the same values.

The distribution looks more normal-like similar to what we obtained after the log transform.

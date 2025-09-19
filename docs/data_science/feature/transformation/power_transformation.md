# Power Transformation [Scaling] {Box-Cox}

## Specifications

- **Data Type**: Continuous numeric data
- **Good For**: Non-Gaussian to Gaussian

## Description

This technique is similar to log transformation but allows for a broader range of transformations.
The most common power transformation is the Box-Cox transformation, which raises the feature values to a power that is determined using maximum likelihood estimation.

## Formula

$$
x_{transformed} = \frac{x^{\lambda} - 1}{\lambda}
$$

Here, $x$ is the original feature value, and $\lambda$ is the power parameter that is estimated using maximum likelihood.

## Box-Cox

The Box-Cox transform is another popular function belonging to the power transform family of functions. **This function has a prerequisite that the numeric values to be transformed must be positive (similar to what log transform expects)**.
In case they are negative, shifting using a constant value helps.

$$
y_i^{(\lambda)} =
\begin{cases}
\frac{y_i^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0, \\
\ln y_i & \text{if } \lambda = 0,
\end{cases}
$$

The resulting transformed output y is a function of input x and the transformation parameter $\lambda$ such that when $\lambda$ = 0, the resultant transform is the natural log transform which we discussed earlier.
The optimal value of $\lambda$ is usually determined using a maximum likelihood or log-likelihood estimation.

<img src="image2.png" style="width:5in" />

## Example

Let's now apply the Box-Cox transform on our developer income feature. First we get the optimal lambda value from the data distribution by removing the non-null values as follows.

```python
income = np.array(fcc_survey_df["Income"])
income_clean = income[~np.isnan(income)]
l, opt_lambda = spstats.boxcox(income_clean)
print("Optimal lambda value:", opt_lambda)

# Output
# ------
# Optimal lambda value: 0.117991239456
```

Now that we have obtained the optimal $\lambda$ value, let us use the Box-Cox transform for two values of $\lambda$ such that $\lambda = 0$ and $\lambda = \lambda_{optimal}$ and transform the developer Income feature.

```python
fcc_survey_df["Income_boxcox_lambda_0"] = spstats.boxcox(
    (1 + fcc_survey_df["Income"]),
    lmbda=0
)

fcc_survey_df["Income_boxcox_lambda_opt"] = spstats.boxcox(
    fcc_survey_df["Income"],
    lmbda=opt_lambda
)
```

The transformed features are depicted in the above data frame.
Just like we expected, Income_log and Income_boxcox_lamba_0 have the same values.

The distribution looks more normal-like similar to what we obtained after the log transform.

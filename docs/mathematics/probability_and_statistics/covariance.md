# Covariance

## Description

We use this concept to understand relationships between features.

We can quantify the relationship between features and then use this learning to either select, add, or alter features for predictive modeling, insight generation, or even storytelling using data.

- Covariance can take any value between $-\infty$ and $+\infty$.
- **The change in scale of the features affects the value of covariance**. If we multiply all the values of the given feature by a constant and all the values of another feature by a similar or different constant, then **the value of covariance also changes**.
- **Covariance**, in and of itself, is not very interesting. What I mean by that is you will never calculate **covariance** and be done for the day. Instead **covariance** is a computational stepping stone to something that is interesting, like **correlation**.

## Formula

Covariance assumes the units from the product of the units of the two variables involved in its formula.

$$
cov_{x, y} = \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{N - 1}
$$

- $cov_{x,y}$ = covariance between variable $x$ and $y$
- $x_i$ = data value of $x$
- $y_i$ = data value of $y$
- $\bar{x}$ = mean of $x$
- $\bar{y}$ = mean of $y$
- $N$ = number of data values

## 3 Types of Covariance

<img src="image4.jpg" style="width:3.22517in" />

<img src="image1.jpg" style="width:3.26181in" />

<img src="image3.jpg" style="width:3.45235in" />

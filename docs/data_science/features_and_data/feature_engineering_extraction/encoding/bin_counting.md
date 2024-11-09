# Bin-Counting

## Specifications

- **Good for**: Large number of values

## Description

The encoding schemes like One-Hot Encoding Scheme, work quite well on categorical data in general, but they start causing problems when the number of distinct categories in any feature becomes very large. Essential for any categorical feature of m distinct labels, you get m separate features. This can easily increase the size of the feature set causing problems like storage issues, and model training problems concerning time, space, and memory. Besides this, we also have to deal with what is popularly known as the "curse of dimensionality" where basically with an enormous number of features and not enough representative samples, model performance starts getting affected often leading to overfitting.

Hence we need to look towards other categorical data feature engineering schemes for features having a large number of possible categories (like IP addresses). The bin-counting scheme is a useful scheme for dealing with categorical variables having many categories. **In this scheme, instead of using the actual label values for encoding, we use probability-based statistical information about the value and the actual target or response value which we aim to predict in our modeling efforts.**

## Example

A simple example would be based on past historical data for IP addresses and the ones that were used in DDOS attacks; we can build probability values for a DDOS attack being caused by any of the IP addresses. Using this information, we can encode an input feature that depicts that if the same IP address comes in the future, what is the probability value of a DDOS attack being caused? This scheme needs historical data as a prerequisite and is an elaborate one.

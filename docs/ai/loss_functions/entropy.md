# Entropy [Multi-Class Classification] [Tree]

## Description

The concept of entropy originated in thermodynamics as a measure of molecular disorder: entropy approaches zero when molecules are still and well ordered.
Entropy later spread to a wide variety of domains, including in Shannon's information theory, where it measures the average information content of a message.
Entropy is zero when all messages are identical.
In machine learning, entropy is frequently used as an impurity measure: a set's entropy is zero when it contains instances of only one class.

## Formula

$$
H_i = - \sum_{k=1}^{n} p_{i,k} \log_2(p_{i,k})
$$

- $H_i$: Entropy of the $i$-th node
- $p_{i,k}$: Ratio of instances of class $k$ among the training samples in the $i$-th node
- $n$: total number of classes
- The logarithm is base 2 (representing information measured in bits)

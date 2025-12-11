# Batch Normalization (BN)

## Description

Batch Normalization consists of adding an operation in the model just before or after the activation function of each hidden layer.
This operation simply zero-centers and normalizes each input, then scales and shifts the result using two new parameter vectors per layer: one for scaling, the other for shifting.
In other words, the operation lets the model learn the optimal scale and mean of each of the layer's inputs.

Batch normalization intentionally uses only the **mini-batch** to compute the mean and variance during training.
This makes training efficient—because computing statistics over the entire dataset for every update would be too slow—and it also introduces beneficial noise.
That noise acts as a regularizer, helping the model generalize better (similar to the effect of dropout).

During inference, however, batch normalization does **not** use mini-batches.
Instead, it relies on **running averages** of the mean and variance collected during training, which approximate the overall data distribution.
This ensures stable predictions and eliminates dependence on batch size.

!!! info

    In many
    cases, if you add a BN layer as the very first layer of your neural
    network, you do not need to standardize your training set (no
    need for `StandardScaler`); the BN layer will do it for you (well,
    approximately, since it only looks at one batch at a time, and it
    can also rescale and shift each input feature).

## Workflow

The algorithm consists of the following steps:

=== "1. Compute mini-batch mean"

    $$
    \mu_B = \frac{1}{m_B} \sum_{i=1}^{m_B} x^{(i)}
    $$

=== "2. Compute mini-batch variance"

    $$
    \sigma_B^{2} = \frac{1}{m_B} \sum_{i=1}^{m_B} \left(x^{(i)} - \mu_B\right)^2
    $$

=== "3. Normalize each input"

    $$
    \hat{x}^{(i)} = \frac{x^{(i)} - \mu_B}{\sqrt{\sigma_B^2 + \varepsilon}}
    $$

=== "4. Scale and shift"

    $$
    z^{(i)} = \gamma \otimes \hat{x}^{(i)} + \beta
    $$

Where:

- $\mu_B$: Vector of means over the mini-batch (one mean per input).
- $m_B$: Number of instances in the mini-batch.
- $x^{(i)}$: Input vector of instance *i* for the batch-norm layer.
- $\sigma_B$: Vector of standard deviations over the mini-batch.
- $\hat{x}^{(i)}$: Normalized input vector for instance *i*.
- $\varepsilon$: Small constant for numerical stability (e.g., $10^{-5}$).
- $\gamma$: Vector of scale parameters (one per input).
- $\beta$: Vector of shift parameters (one per input).
- $\otimes$: Element-wise multiplication.
- $z^{(i)}$: Output of the batch normalization operation.

!!! info

    The normalization part of Batch Normalization is basically the same as Z-score normalization.
    But BN is an extended version of it, because it also has learnable parameters ($\gamma$ and $\beta$) and it works on mini-batches, which makes it special for neural networks.

## Example

```python
import torch.nn as nn

model = nn.Sequential(
    nn.BatchNorm1d(784),  # Input normalization
    nn.Linear(784, 300), nn.ReLU(), nn.BatchNorm1d(300),
    nn.Linear(300, 100), nn.ReLU(), nn.BatchNorm1d(100),
    nn.Linear(100, 10)
)
```

!!! warning

    Since batch norm behaves differently during training and during evaluation, it's critical to switch to training mode during training (using `model.train()`), and switch to evaluation mode during evaluation (using `model.eval()`). Forgetting to do so is one of the most common mistakes.

# Layer Normalization (LN) *

## Description

Layer Normalization is similar to Batch Normalization, but it normalizes across the features of a **single sample** instead of across the batch.
It computes the mean and variance using all the hidden units in a specific layer for one specific input.

Like BN, it applies a learnable scale and shift ($\gamma$ and $\beta$) after normalization.
However, because it doesn't rely on other samples in the batch, Layer Normalization behaves exactly the same way during training and inference.
There are no running averages or global statistics to track.

This independence from the batch dimension makes it the go-to normalization technique for Recurrent Neural Networks (RNNs) and Transformers, where batch sizes can vary or be small, and sequence lengths differ.

!!! info

    Unlike Batch Norm, Layer Norm does **not** introduce noise related to batch statistics.
    This means it doesn't have the same implicit regularization effect as BN, but it is much more stable for sequence models.

## Workflow

The algorithm processes each sample $x^{(i)}$ independently:

=== "1. Compute layer mean"

    $$
    \mu^{(i)} = \frac{1}{H} \sum_{j=1}^{H} x_j^{(i)}
    $$

=== "2. Compute layer variance"

    $$
    \sigma^{(i)2} = \frac{1}{H} \sum_{j=1}^{H} \left(x_j^{(i)} - \mu^{(i)}\right)^2
    $$

=== "3. Normalize input"

    $$
    \hat{x}_j^{(i)} = \frac{x_j^{(i)} - \mu^{(i)}}{\sqrt{\sigma^{(i)2} + \varepsilon}}
    $$

=== "4. Scale and shift"

    $$
    z_j^{(i)} = \gamma_j \cdot \hat{x}_j^{(i)} + \beta_j
    $$

Where:

- $H$: Number of hidden units (features) in the layer.
- $x_j^{(i)}$: The $j$-th feature of the $i$-th sample input.
- $\mu^{(i)}$: Mean of the input features for sample $i$ (scalar).
- $\sigma^{(i)}$: Standard deviation of the input features for sample $i$ (scalar).
- $\varepsilon$: Small constant for numerical stability.
- $\gamma$: Learnable scale parameter.
- $\beta$: Learnable shift parameter.
- $z^{(i)}$: Output vector for sample $i$.

!!! info

    - Notice the indices.
    - Batch Norm sums over the batch dimension $m$.
    - Layer Norm sums over the feature dimension $H$.

## Example

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 300), nn.ReLU(), nn.LayerNorm(300),
    nn.Linear(300, 100), nn.ReLU(), nn.LayerNorm(100),
    nn.Linear(100, 10)
)
```

!!! info

    Layer Normalization behaves consistently in training and evaluation modes, unlike Batch Normalization.

# AdamW Algorithm [Adam]

## Description

AdamW is an optimization algorithm that **builds upon the Adam** technique by **decoupling weight decay from the gradient update**.

While Adam combines momentum and adaptive learning rates to efficiently move towards the minimum, AdamW improves generalization by applying weight decay directly to the parameters, rather than through the gradients.
This adjustment helps prevent overfitting and leads to better performance in training deep neural networks.

## Example

```python
from torch.optim import AdamW

optimizer = AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
```

!!! info

    The `weight_decay` parameter controls the strength of L2 regularization (Ridge).

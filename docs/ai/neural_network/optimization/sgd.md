# SGD

## Description

Stochastic Gradient Descent (SGD) updates model parameters by subtracting the loss gradient, calculated from random data samples.

## Formula

On iteration $t$: Compute $dW$, $db$ using current example.

$W := W - \alpha \, dW$

$b := b - \alpha \, db$

## Example

```python
from torch.optim import SGD

optimizer = SGD(model.parameters(), lr=1e-3)
```

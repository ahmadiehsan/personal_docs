# Stochastic Weight Averaging (SWA)

## Description

SWA is a technique that improves neural network generalization by averaging weights from multiple points along the optimization trajectory, effectively finding flatter, more robust minima that perform better on unseen data than the typically sharp minima found by conventional optimization methods.

SWA involves averaging multiple points along the trajectory of Stochastic gradient descent (SGD) with a modified learning rate schedule.

## Example

```python
from torch.optim.swa_utils import AveragedModel, SWALR

swa_model = AveragedModel(model)
swa_scheduler = SWALR(optimizer, swa_lr=0.05)

for epoch in range(100):
    # Train the model here ...

    if epoch > 75:  # Start SWA after epoch 75
        swa_model.update_parameters(model)
        swa_scheduler.step()
```

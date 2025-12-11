# Sharpness-Aware Minimization (SAM)

## Description

Sharpness-Aware Minimization (SAM) seeks parameters that lie in neighborhoods with uniformly low loss values, leading to better generalization.

Its key features are the following:

- Looks for "flat" minima instead of sharp ones
- Improves robustness against input perturbations
- Generally provides better generalization than standard SGD

## Example

```python
import torch

class SAM(torch.optim.Optimizer):
    def __init__(self, params, base_optimizer, rho=0.05):
        self.rho = rho
        self.base_optimizer = base_optimizer(self.param_groups)

    def step(self):
        # First forward-backward pass
        grad_norm = self._grad_norm()
        scale = self.rho / (grad_norm + 1e-12)

        # Perturb weights
        for group in self.param_groups:
            for p in group["params"]:
                e_w = p.grad * scale
                p.add_(e_w)

        # Second forward-backward pass
        self.base_optimizer.step()
```

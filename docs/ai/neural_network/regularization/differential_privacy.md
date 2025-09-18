# Differential Privacy (DP)

## Description

Differential privacy (DP) is a technique that adds carefully calibrated noise to data or computations to protect individual privacy while still allowing useful insights, ensuring that the inclusion or exclusion of any single data point does not significantly affect model performance.

Is a technique used to enhance model privacy by adding noise to the model’s training process, which protects individual data points from being exposed in model outputs or learned representations.
By introducing controlled randomness, DP-based regularization limits the model’s reliance on any specific data sample, thereby reducing the risk of overfitting and making the model less sensitive to variations in individual data points.

!!! info

    This method is particularly valuable in privacy-sensitive applications, as it ensures that models can learn generalizable patterns without revealing specific information about the training data, making it useful in healthcare, finance, and other areas requiring data confidentiality.

## Example

```python
import torch

class DPOptimizer(torch.optim.Optimizer):
    def __init__(self, params, noise_multiplier=1.0, max_grad_norm=1.0):
        super().__init__(params, {})  # initialize base Optimizer
        self.noise_multiplier = noise_multiplier
        self.max_grad_norm = max_grad_norm

    def step(self, closure=None):
        # Clip gradients
        torch.nn.utils.clip_grad_norm_(self.param_groups[0]["params"], self.max_grad_norm)

        # Add noise
        for p in self.param_groups[0]["params"]:
            noise = torch.randn_like(p.grad) * self.noise_multiplier
            p.grad.add_(noise)
```

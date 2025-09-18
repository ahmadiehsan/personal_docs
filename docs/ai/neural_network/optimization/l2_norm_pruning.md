# L2-Norm Pruning [Pruning] [Structured]

## Description

L2-norm pruning is a **popular structured pruning** technique that removes entire neurons or filters from a network.

The main idea is to assess the overall importance of a whole neuron by calculating the L2-norm (Euclidean norm) of its associated weights.
Neurons with the smallest L2-norm are considered the least influential and are removed completely.

!!! info

    This method creates a genuinely smaller and more regular model architecture, which often leads to direct speed improvements without needing special hardware or software.

## Example

```python
import torch
import torch.nn.utils.prune as prune

model = ...  # Assume model is an instance of a pre-trained NN

# Step 1) Prune 30% of weights (will remove entire neurons) in all Linear layers (Masking step)
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        prune.ln_structured(module, name="weight", amount=0.3, n=2, dim=0)

# Optional) Fine-tune the model here

# Step 2) Remove the pruning reparameterization (Permanently removing step)
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        prune.remove(module, "weight")
```

# Magnitude-Based Pruning [Pruning] [Unstructured]

## Description

Magnitude-based pruning is **one of the simplest and most widely used** pruning techniques.
The idea behind this method is to remove weights in the neural network that contribute least to the model’s overall function, typically, these are weights with the smallest magnitude (absolute value).
By pruning such weights, the model becomes more compact and faster, with minimal impact on accuracy.

!!! info

    Magnitude-based pruning is particularly effective for models with many small weights that contribute little to overall performance, but it may not be sufficient when applied alone for large-scale pruning.

## Example

```python
import torch
import torch.nn.utils.prune as prune

model = ...  # Assume model is an instance of a pre-trained NN

# Step 1) Prune 30% of weights in all Linear layers (Masking weights)
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        prune.l1_unstructured(module, name="weight", amount=0.3)

# Optional) Fine-tune the model here

# Step 2) Remove the pruning reparameterization (Permanently replacing masked weights with 0)
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        prune.remove(module, "weight")
```

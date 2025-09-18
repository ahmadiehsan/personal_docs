# Magnitude-Based Pruning [Pruning]

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

model = ... # Assume model is an instance of a pre-trained NN

# Step 1) Prune 30% of the lowest magnitude weights in all Linear layers
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        prune.l1_unstructured(module, name='weight', amount=0.3)

# Step 2) Remove the pruning reparameterization
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        prune.remove(module, 'weight')
```

!!! info

    The first step applies a temporary mask (Optionally, after this step we can fine-tune the model to help the remaining weights adjust and recover accuracy).

    The second step permanently sets the weak connections to zero and throws away the temporary mask, making the model's new, smaller structure final.

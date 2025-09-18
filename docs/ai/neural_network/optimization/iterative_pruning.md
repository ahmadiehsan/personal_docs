# Iterative Pruning [Pruning] [Structured & Unstructured]

## Description

Iterative pruning allows you to prune a small fraction of weights at a time over multiple training steps.
This method reduces the risk of drastic performance drops and provides more opportunities for the model to recover and adjust to the pruning.

The iterative approach also allows for fine-tuning after each pruning step, enabling the model to "heal" from the weight reduction.

!!! info

    The gradual removal of weights ensures that the model has enough time to adjust between each pruning step.

## Example

Iteratively prune 10% of the model after every 10 epochs:

```python
for epoch in range(1, num_epochs+1):
    # Regular training step here

    if epoch % 10 == 0:
        for name, module in model.named_modules():
            if isinstance(module, torch.nn.Linear):
                # prune.l1_unstructured(module, name="weight", amount=0.1)  # Unstructured
                prune.ln_structured(module, name="weight", amount=0.1, n=2, dim=0)  # Structured
                prune.remove(module, "weight")  # Remove pruning mask after each step

    # Regular validation step here
```

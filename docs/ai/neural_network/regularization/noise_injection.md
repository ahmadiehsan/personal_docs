# Noise Injection [Noise]

## Description

Noise injection is a regularization technique commonly used to improve the generalization of machine learning models.
By adding a small amount of noise to the input data, weights, or activation functions.

Noise injection helps prevent overfitting, the technique forces the model to be less reliant on specific patterns in the training data, encouraging it to learn more robust, general features that apply across different datasets.

This approach is particularly useful in neural networks, where noise such as the following can be injected at various stages:

- **Input noise**: Adds noise directly to the input data, helping the model become more robust to variations in the input
- **Weight noise**: Perturbs the weights during training, encouraging the model to generalize better
- **Activation noise**: Adds noise to the activation functions, leading to smoother decision boundaries and reducing overfitting

## Example

```python
import torch
from torch.nn.utils import clip_grad_norm_
from torch.optim import AdamW

def train(model, dataloader, grad_clip=1.0, noise_factor=0.01, lr=5e-5, epochs=3):
    optimizer = AdamW(model.parameters(), lr=lr)

    for e in range(epochs):
        model.train()
        total_loss = 0

        for batch in dataloader:
            optimizer.zero_grad()

            input_ids = batch["input_ids"]
            noise = torch.randn_like(input_ids, dtype=torch.float) * noise_factor
            noisy_inputs = noisy_inputs = input_ids.float() + noise
            noisy_inputs = noisy_inputs.long().clamp(min=0, max=model.config.vocab_size - 1)

            outputs = model(input_ids=noisy_inputs, labels=input_ids)
            loss = outputs.loss
            loss.backward()

            clip_grad_norm_(model.parameters(), grad_clip);
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {e+1}, Loss: {total_loss/len(dataloader):.4f}")
```

!!! info

    **What does `clip_grad_norm_` do?**

    It limits (clips) the size of gradients during backpropagation.
    This prevents *exploding gradients* (when gradients become too large), helping the model train more stably and avoiding NaN losses.

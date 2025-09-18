# Adaptive Dropout [Dropout]

## Description

When fine-tuning pre-trained NNs, it's important to carefully adjust regularization to avoid blocking task-specific adaptation while still preventing overfitting.

It starts with a higher dropout rate and gradually decreases it over the course of fine-tuning.
This allows the model to adapt to the new task while still maintaining some regularization to prevent overfitting.

!!! info

    This approach prevents overfitting more efficiently than standard dropout, as it maintains the network's capacity to learn complex patterns through important neurons while aggressively regularizing redundant or noise-sensitive parts, resulting in models that generalize better with less performance sacrifice on critical features.

## Example

```python
import torch.nn as nn
from torch.optim import AdamW
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def fine_tune(model_id, dataloader, initial_dropout=0.1, epochs=3):
    model = GPT2LMHeadModel.from_pretrained(model_id)
    tokenizer = GPT2Tokenizer.from_pretrained(model_id)
    optimizer = AdamW(model.parameters(), lr=5e-5, weight_decay=0.01)

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        current_dropout = initial_dropout * (1 - epoch / epochs)

        # Update dropout rates
        for module in model.modules():
            if isinstance(module, nn.Dropout):
                module.p = current_dropout

        # Training loop
        for batch in dataloader:
            optimizer.zero_grad()
            outputs = model(**batch)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(
            f"Epoch {epoch + 1}, "
            f"Loss: {total_loss / len(dataloader):.4f}, "
            f"Dropout: {current_dropout:.4f}"
        )
```

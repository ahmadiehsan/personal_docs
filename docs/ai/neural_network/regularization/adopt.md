# ADOPT [Adam]

## Description

ADOPT offers a better alternative for optimizing Deep Learning models and LLMs.
The key issue with Adam was the lack of convergence guarantee during weight updates, which is addressed by ADOPT.
This isn't just theoretical—ADOPT has been shown to outperform Adam in most tasks, including GPT-2 pretraining.

The core idea and solution to ensure convergence are:

1. Removing the current gradient from the second momentum estimate.
2. Normalizing the gradient before updating the momentum.

## Example

```python
from adopt import ADOPT

#optimizer = Adam(model.parameters(), lr=1e-3)  # We don't need Adam anymore!
optimizer = ADOPT(model.parameters(), lr=1e-3)
```

# Layer-Wise Adaptive Regularization

## Description

Layer-wise adaptive regularization involves **applying different regularization strengths to different layers** of the model.

This can be particularly effective for LLMs, where lower layers may benefit from less regularization to capture fundamental patterns, while higher layers might need stronger regularization to prevent overfitting.

## Example

```python
import torch.nn as nn

class LayerwiseAdaptiveRegularization(nn.Module):
    def __init__(self, base_model, base_dropout=0.1, dropout_step=0.02):
        super().__init__()
        self.base_model = base_model
        for i, layer in enumerate(base_model.transformer.h):
            dropout = base_dropout + i * dropout_step
            layer.attn.dropout.p = dropout
            layer.mlp.dropout.p = dropout

    def forward(self, *args, **kwargs):
        return self.base_model(*args, **kwargs)

base_model = create_lm_model()
model = LayerwiseAdaptiveRegularization(base_model)
```

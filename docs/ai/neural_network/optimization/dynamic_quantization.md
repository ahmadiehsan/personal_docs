# Dynamic Quantization [Quantization]

## Description

Dynamic quantization calculates quantization parameters on the fly during inference based on the actual input values.
This adapts better to varying data distributions but introduces some computational overhead compared to static approaches.

## Example

```python
import torch
import torch.quantization as quant

model = ...  # Pre-trained model
quantized_model = quant.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
```

!!! info

    We use `torch.quantization.quantize_dynamic` to dynamically quantize the linear layers of a pre-trained model

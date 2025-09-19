# Quantization

## Description

The weights of an LLM are numeric values with a given precision, which can be expressed by the number of bits like float64 or float32.
If we lower the amount of bits to represent a value, we get a less accurate result.
However, if we lower the number of bits we also lower the memory requirements of that model.

![](quantization/overview.png)

!!! info

    Notice the lowered accuracy when we halve the number of bits.

## Varieties

There are two main quantization approaches based on when quantization is applied:

- **Post-training quantization (PTQ)**: Applies quantization after the model has been fully trained, with minimal or no additional training. Can be implemented as either static (with calibration) or dynamic.
- **Quantization-aware training (QAT)**: Simulates quantization effects during training by adding fake quantization operations in the forward pass while keeping gradients in full precision. Typically results in static quantization for deployment.

## Example

```python
import torch
import torch.quantization as quant

model = ...  # Pre-trained model
quantized_model = quant.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
```

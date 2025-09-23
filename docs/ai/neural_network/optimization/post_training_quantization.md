# Post-Training Quantization (PTQ) [Quantization]

## Description

PTQ is the **most straightforward** form of quantization and is **applied after a model has been fully trained**.
It doesn't require model retraining and works by converting the high-precision weights and activations into lower-precision formats, typically INT8.

PTQ is ideal for models where retraining is expensive or impractical, and it works best for tasks that are not overly sensitive to precision loss.

!!! info

    Some PTQ methods often require a calibration step on a representative dataset to determine optimal quantization parameters such as scaling factors and zero points, capture activation distributions during inference, and minimize the error between original and quantized model outputs.

    This calibration process helps the quantization algorithm understand the numerical range and distribution of weights and activations across the network, allowing more accurate mapping from higher precision formats (such as FP32) to lower precision formats (such as INT8 or INT4), ultimately preserving model accuracy while reducing memory footprint and computational requirements for deployment.

## Example

```python
import torch
import torch.quantization as quant

model = ...  # Load pre-trained model

# Convert model to quantization-ready state
model.eval()
model.qconfig = quant.default_qconfig

# Prepare for static quantization
model_prepared = quant.prepare(model)

# Calibration step: run representative data through the model
# (This example uses random data; replace with real samples)
for _ in range(100):
    sample_input = torch.randn(1, 784)
    model_prepared(sample_input)

# Apply quantization
model_quantized = quant.convert(model_prepared)
```

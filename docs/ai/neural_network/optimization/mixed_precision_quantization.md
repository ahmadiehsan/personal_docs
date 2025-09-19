# Mixed-Precision Quantization [Quantization]

## Description

Mixed-precision quantization is a more flexible approach that leverages multiple levels of numerical precision within a single model.
For instance, less critical layers of the model can use INT8, while more sensitive layers remain in FP16 or FP32.
This allows greater control over the trade-off between performance and precision.

## Example

```python
from torch.cuda.amp import autocast

model = ...  # Load a normal pre-trained FP32 model

with autocast():  # Use FP16 where possible, fall back to FP32 for sensitive computations
    output = model(input_data)
```

!!! info

    The `autocast` context manager is designed to convert standard float32 (full-precision) models to mixed precision.

    If the model is already saved in half-precision (float16), there's nothing for `autocast` to do.

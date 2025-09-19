# Quantization-Aware Training (QAT) [Quantization]

## Description

QAT goes beyond simple PTQ by incorporating the effects of **quantization into the training process** itself.
This allows the model to learn how to compensate for the quantization-induced noise.

During QAT, both weights and activations are **simulated at lower precision during training** but are kept at **higher precision for gradient calculations**.
This method is particularly useful when the application requires high performance with aggressive quantization.

!!! info

    QAT typically results in better model accuracy compared to PTQ, particularly for more complex or critical applications.

## Example

```python
import torch.quantization as quant

model = ...  # Load pre-trained model

# Set up QAT
model.train()
model.qconfig = quant.get_default_qat_qconfig("fbgemm")

# Prepare for QAT
model_prepared = quant.prepare_qat(model)

# Training loop (for simplicity, only showing initialization)
for epoch in range(num_epochs):
    train_one_epoch(model_prepared, train_loader, optimizer)
    validate(model_prepared, val_loader)

# Convert to quantized version
model_quantized = quant.convert(model_prepared.eval())
```

# Quantization {QAT} {PTQ} {Mixed-Precision} {Dynamic}

## Description

The weights of an LLM are numeric values with a given precision, which can be expressed by the number of bits like float64 or float32.
If we lower the amount of bits to represent a value, we get a less accurate result.
However, if we lower the number of bits we also lower the memory requirements of that model.

<img src="overview.png" style="width:4.5in" />

!!! info

    Notice the lowered accuracy when we halve the number of bits.

## Varieties

=== "PTQ"

    **Post-Training Quantization (PTQ)** is the **most straightforward** form of quantization and is **applied after a model has been fully trained**.
    It doesn't require model retraining and works by converting the high-precision weights and activations into lower-precision formats, typically INT8.

    PTQ is ideal for models where retraining is expensive or impractical, and it works best for tasks that are not overly sensitive to precision loss.

    !!! info

        Some PTQ methods often require a calibration step on a representative dataset to determine optimal quantization parameters such as scaling factors and zero points, capture activation distributions during inference, and minimize the error between original and quantized model outputs.

        This calibration process helps the quantization algorithm understand the numerical range and distribution of weights and activations across the network, allowing more accurate mapping from higher precision formats (such as FP32) to lower precision formats (such as INT8 or INT4), ultimately preserving model accuracy while reducing memory footprint and computational requirements for deployment.

=== "QAT"

    **Quantization-Aware Training (QAT)** goes beyond simple PTQ by incorporating the effects of **quantization into the training process** itself.
    This allows the model to learn how to compensate for the quantization-induced noise.

    During QAT, both weights and activations are **simulated at lower precision during training** but are kept at **higher precision for gradient calculations**.
    This method is particularly useful when the application requires high performance with aggressive quantization.

    !!! info

        QAT typically results in better model accuracy compared to PTQ, particularly for more complex or critical applications.

=== "Dynamic"

    **Dynamic quantization** calculates quantization parameters on the fly during inference based on the actual input values.
    This adapts better to varying data distributions but introduces some computational overhead compared to static approaches.

=== "Mixed-Precision"

    **Mixed-precision quantization** is a more flexible approach that leverages multiple levels of numerical precision within a single model.
    For instance, less critical layers of the model can use INT8, while more sensitive layers remain in FP16 or FP32.
    This allows greater control over the trade-off between performance and precision.

## Example

=== "PTQ"

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

=== "QAT"

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

=== "Dynamic"

    ```python
    import torch
    import torch.quantization as quant

    model = ...  # Pre-trained model
    quantized_model = quant.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
    ```

    !!! info

        We use `torch.quantization.quantize_dynamic` to dynamically quantize the linear layers of a pre-trained model

=== "Mixed-Precision"

    ```python
    from torch.cuda.amp import autocast

    model = ...  # Load a normal pre-trained FP32 model

    with autocast():  # Use FP16 where possible, fall back to FP32 for sensitive computations
        output = model(input_data)
    ```

    !!! info

        The `autocast` context manager is designed to convert standard float32 (full-precision) models to mixed precision.

        If the model is already saved in half-precision (float16), there's nothing for `autocast` to do.

## Vs

| Strategy        | Accuracy                                         | Complexity                         | Performance                             | Resources                      |
| --------------- | ------------------------------------------------ | ---------------------------------- | --------------------------------------- | ------------------------------ |
| PTQ             | Good for simple models; declines with complexity | Low; minimal setup                 | 75% storage reduction; 2-4x speedup     | Low; minimal compute needed    |
| QAT             | Highest; best for sub-8-bit                      | High; requires extended training   | High compression with the best accuracy | High; intensive training needs |
| Dynamic         | Good for RNNs; weak for CNNs                     | Medium; runtime overhead           | Good memory savings; slower compute     | Medium; runtime processing     |
| Mixed-Precision | High; flexible precision options                 | Medium-high; layer-specific tuning | Hardware-dependent speedup              | Medium-high during setup       |

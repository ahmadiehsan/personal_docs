# Pruning {Magnitude-Based} {L2-Norm} {Iterative}

## Description

Pruning is a model optimization technique used to reduce the size and computational complexity of a trained model while maintaining accuracy.
This is achieved by **identifying and removing redundant or less important parameters (weights)** or **structures (neurons, channels, or layers)**.

When pruning LLMs, you can either prune weights individually (unstructured pruning) or remove entire structures, such as filters, channels, or attention heads (structured pruning):

- **Unstructured pruning**: This involves removing individual weights based on magnitude or other criteria. It provides more granularity but can result in sparse matrices, **which are harder to optimize on standard hardware**.
- **Structured pruning**: Entire sections of the model, such as neurons, channels, or layers, are pruned. This approach is **easier to implement on modern hardware** and often leads to **better speedups** in inference time, even though it may **have a larger immediate effect on model performance**.

## Varieties

=== "Magnitude-Based"

    **Magnitude-based pruning** is **one of the simplest** and most widely used **unstructured** pruning techniques.
    The idea behind this method is to remove weights in the neural network that contribute least to the model's overall function, typically, these are weights with the smallest magnitude (absolute value).
    By pruning such weights, the model becomes more compact and faster, with minimal impact on accuracy.

    !!! info

        Magnitude-based pruning is particularly effective for models with many small weights that contribute little to overall performance, but it may not be sufficient when applied alone for large-scale pruning.

=== "L2-Norm"

    **L2-norm pruning** is a popular **structured** pruning technique that removes entire neurons or filters from a network.

    The main idea is to assess the overall importance of a whole neuron by calculating the L2-norm (Euclidean norm) of its associated weights.
    Neurons with the smallest L2-norm are considered the least influential and are removed completely.

    !!! info

        This method creates a genuinely smaller and more regular model architecture, which often leads to direct speed improvements without needing special hardware or software.

=== "Iterative"

    **Iterative pruning** is a **structured and unstructured** pruning technique that allows you to prune a small fraction of weights at a time over multiple training steps.
    This method reduces the risk of drastic performance drops and provides more opportunities for the model to recover and adjust to the pruning.

    The iterative approach also allows for fine-tuning after each pruning step, enabling the model to "heal" from the weight reduction.

    !!! info

        The gradual removal of weights ensures that the model has enough time to adjust between each pruning step.

## Example

=== "Magnitude-Based"

    ```python
    import torch
    import torch.nn.utils.prune as prune

    model = ...  # Assume model is an instance of a pre-trained NN

    # Step 1) Prune 30% of weights in all Linear layers (Masking weights)
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            prune.l1_unstructured(module, name="weight", amount=0.3)

    # Optional) Fine-tune the model here

    # Step 2) Remove the pruning reparameterization (Permanently replacing masked weights with 0)
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            prune.remove(module, "weight")
    ```

=== "L2-Norm"

    ```python
    import torch
    import torch.nn.utils.prune as prune

    model = ...  # Assume model is an instance of a pre-trained NN

    # Step 1) Prune 30% of weights (will remove entire neurons) in all Linear layers (Masking weights)
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            prune.ln_structured(module, name="weight", amount=0.3, n=2, dim=0)

    # Optional) Fine-tune the model here

    # Step 2) Remove the pruning reparameterization (Permanently replacing masked weights with 0)
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            prune.remove(module, "weight")
    ```

=== "Iterative"

    Iteratively prune 10% of the model after every 10 epochs:

    ```python
    for epoch in range(1, num_epochs+1):
        # Regular training step here

        if epoch % 10 == 0:
            for name, module in model.named_modules():
                if isinstance(module, torch.nn.Linear):
                    # prune.l1_unstructured(module, name="weight", amount=0.1)  # Unstructured
                    prune.ln_structured(module, name="weight", amount=0.1, n=2, dim=0)  # Structured
                    prune.remove(module, "weight")  # Remove pruning mask after each step

        # Regular validation step here
    ```

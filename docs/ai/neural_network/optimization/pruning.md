# Pruning

## Description

Pruning is a model optimization technique used to reduce the size and computational complexity of a trained model while maintaining accuracy.
This is achieved by **identifying and removing redundant or less important parameters (weights)** or **structures (neurons, channels, or layers)**.

When pruning LLMs, you can either prune weights individually (unstructured pruning) or remove entire structures, such as filters, channels, or attention heads (structured pruning):

- **Unstructured pruning**: This involves removing individual weights based on magnitude or other criteria. It provides more granularity but can result in sparse matrices, **which are harder to optimize on standard hardware**.
- **Structured pruning**: Entire sections of the model, such as neurons, channels, or layers, are pruned. This approach is **easier to implement on modern hardware** and often leads to **better speedups** in inference time, even though it may **have a larger immediate effect on model performance**.

# Gradient Checkpointing

## Description

Gradient Checkpointing reduces memory usage by selectively storing only a subset of intermediate activations during the forward pass.
During backpropagation, the missing activations are recomputed as needed, trading compute for memory.

This technique is particularly useful when training large transformer models, where memory consumption due to storing full activation histories becomes prohibitive.
Popular libraries such as PyTorch's torch. utils.checkpoint or TensorFlow's recomputation wrappers make it possible to apply this technique without having to rewrite model architectures.

## Example

```python
from transformers import GPT2LMHeadModel

def enable_gradient_checkpointing(model):
    if hasattr(model, "gradient_checkpointing_enable"):
        model.gradient_checkpointing_enable()
    else:
        model.base_model.gradient_checkpointing_enable()

    return model

base_model = GPT2LMHeadModel.from_pretrained("gpt2-large")
base_model = enable_gradient_checkpointing(base_model)
```

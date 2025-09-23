# Integrated Gradients [NLP] [Attribution]

## Description

Integrated gradients is an attribution method used to explain the predictions of neural networks by quantifying the contribution of each input feature to the model's output.
It computes feature attributions by integrating the gradients of the model's output with respect to the input, along a straight path from a baseline to the actual input.

!!! warning

    Keep in mind that gradient-based methods in LLMs can be noisy due to sensitivity to input perturbations, mini-batch variance, and gradient saturation, affecting both training stability and interpretability.
    In optimization, noise can cause oscillations or suboptimal convergence, while in interpretability, methods such as integrated gradients can produce inconsistent attributions across runs.
    This instability reduces trust in model insights, especially for similar inputs.
    Techniques such as gradient smoothing, averaging, and second-order optimization help mitigate noise but add computational overhead, creating a trade-off between efficiency and precision in LLM development.

## Example

```python
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np
import matplotlib.pyplot as plt

def integrated_gradients(model, tokenizer, text, target_class, steps=50):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    baseline_ids = torch.zeros_like(input_ids)
    alphas = torch.linspace(0, 1, steps)
    delta = input_ids - baseline_ids
    accumulated_grads = 0

    for alpha in alphas:
        interpolated_ids = baseline_ids + alpha * delta
        interpolated_ids.requires_grad_()

        outputs = model(interpolated_ids)
        pred = outputs.logits[:, target_class]

        model.zero_grad()
        pred.backward()

        accumulated_grads += interpolated_ids.grad

    attributions = (input_ids - baseline_ids) * accumulated_grads / steps
    return attributions.squeeze().detach().numpy()

model_name = "bert-base-uncased"
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

text = "This movie was fantastic!"
target_class = 1  # Assuming 1 is the positive sentiment class

attributions = integrated_gradients(model, tokenizer, text, target_class)

# Visualize attributions
tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(text))
plt.figure(figsize=(10, 5))
plt.bar(range(len(tokens)), attributions)
plt.xticks(range(len(tokens)), tokens, rotation=45)
plt.title("Integrated Gradients Attribution")
plt.show()
```

!!! info

    After defining the model and tokenizer, the code runs the attribution method on an example text and displays the results as a bar plot, where each bar corresponds to a token and its importance for the target prediction.

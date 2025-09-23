# Attention Visualization [NLP]

## Description

Attention mechanisms are a key component of transformer-based LLMs.
Visualizing attention patterns can provide insights into how the model processes and attends to different parts of the input.

!!! warning

    Keep in mind that attention maps do not always correlate with model reasoning in LLMs. While they show where the model focuses, they don't necessarily explain why a decision is made.
    Attention can be diffused, inconsistent, or misleading, sometimes highlighting irrelevant tokens while still producing correct outputs. Since LLMs encode information in distributed representations, reasoning often occurs beyond direct attention, involving deep latent transformations across layers.

## Example

```python
import torch
from transformers import BertTokenizer, BertModel
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_attention(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(inputs, output_attentions=True)

    attention = outputs.attentions[-1].squeeze().detach().numpy()
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    plt.figure(figsize=(10, 8))
    sns.heatmap(attention, xticklabels=tokens, yticklabels=tokens, cmap="YlGnBu")
    plt.title("Attention Visualization")
    plt.show()

model_name = "bert-base-uncased"
model = BertModel.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

text = "The cat sat on the mat."
visualize_attention(model, tokenizer, text)
```

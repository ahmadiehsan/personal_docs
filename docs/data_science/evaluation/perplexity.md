# Perplexity [NLP] [LLM]

## Description

Perplexity is a measurement of how well a probabilistic model (often a language model) predicts a sample.
Lower perplexity indicates better predictive performance.

It is commonly used in natural language processing to evaluate language models, such as n-gram models or neural language models.

- Perplexity can be interpreted as the average branching factor: the lower the perplexity, the less "confused" the model is when making predictions.
- A model that assigns higher probabilities to the correct sequence will have lower perplexity.

## Example

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

text = "The quick brown fox jumps over the lazy dog."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs, labels=inputs["input_ids"])
    perplexity = torch.exp(outputs.loss).item()

print(f"Perplexity: {perplexity:.2f}")
```

# Probing [NLP]

## Descrption

Probing involves training simple models on the internal representations of an LLM to assess what linguistic properties are captured at different layers.

Different layers in a transformer specialize in different linguistic properties.
Lower layers capture syntax and token identity; middle layers handle grammar and sentence structure; and higher layers focus on semantics, reasoning, and factual recall.
This hierarchy emerges naturally during training, with lower layers excelling in syntactic tasks and higher layers in semantic reasoning.
Probing studies confirm this specialization, aiding interpretability, fine-tuning, and model compression for task-specific optimizations.

## Example

```python
import torch
from transformers import BertTokenizer, BertModel
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def probe_bert_layers(model, tokenizer, texts, labels, layer_nums):
    def get_embeddings(text):  # Get BERT embeddings for each layer
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(inputs, output_hidden_states=True)
        return outputs.hidden_states

    results = {}
    for layer_num in layer_nums:
        embeddings = [get_embeddings(text)[layer_num].squeeze().mean(dim=0).numpy() for text in texts]
        X_train, X_test, y_train, y_test = train_test_split(embeddings, labels, test_size=0.2, random_state=42)

        # Train and evaluate probe
        probe = LogisticRegression(random_state=42)
        probe.fit(X_train, y_train)
        y_pred = probe.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[f"layer_{layer_num}"] = accuracy

    return results

model_name = "bert-base-uncased"
model = BertModel.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

texts = ["The cat sat on the mat.", "The dog chased the ball.", ...]
labels = [0, 1, ...]  # Corresponding labels (e.g., 0 for simple, 1 for complex sentences)

layer_nums = [1, 6, 12]  # Layers to probe
probe_results = probe_bert_layers(model, tokenizer, texts, labels, layer_nums)

for layer, accuracy in probe_results.items():
    print(f"{layer} accuracy: {accuracy:.2f}")
```

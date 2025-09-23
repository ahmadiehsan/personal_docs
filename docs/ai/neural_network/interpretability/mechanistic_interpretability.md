# Mechanistic Interpretability (MI) [NLP]

## Description

Mechanistic interpretability (MI) is an emerging field that aims to understand how neural networks process information at a detailed, component level—similar to how we might reverse-engineer a mechanical device.
Rather than just observing inputs and outputs, MI seeks to trace how information flows through the network, identify specific computational patterns, and understand how different parts of the network (such as individual neurons or attention heads) contribute to the model's behavior.

!!! info

    MI is important because it goes beyond surface-level explanations to uncover the internal mechanisms of how neural networks, particularly complex models like LLMs, actually work. By analyzing how specific components—like neurons, layers, or attention heads—process and transform information

## Example

```python
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

class InterpretableTransformer(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_layers):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model, nhead, batch_first=True)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)
        self.fc = nn.Linear(d_model, vocab_size)

    def get_attention_patterns(self, x):
        """Extract attention weights from each layer"""
        x = self.embedding(x)
        attention_patterns = []

        for layer in self.transformer.layers:
            # Register a hook to capture attention weights
            attention_weights = None

            def hook(module, input, output):
                nonlocal attention_weights
                attention_weights = output[1]  # attention weights

            handle = layer.self_attn.register_forward_hook(hook)
            x = layer(x)
            attention_patterns.append(attention_weights)
            handle.remove()

        return attention_patterns

    def analyze_neuron_activations(self, x, layer_idx):
        """Analyze individual neuron activations in a specific layer"""
        activations = []

        def hook(module, input, output):
            activations.append(output.detach())

        # Register hook on specific layer
        handle = list(self.transformer.layers)[layer_idx].register_forward_hook(hook)

        # Forward pass
        with torch.no_grad():
            self(x)

        handle.remove()
        layer_activations = activations[0]

        # Find most active neurons
        mean_activation = layer_activations.mean(dim=(0, 1))  # Average across batch and sequence
        top_neurons = torch.topk(mean_activation, k=10)

        return top_neurons.indices, top_neurons.values

    def intervention_study(self, x, layer_idx, neuron_idx):
        """Study how zeroing out specific neurons affects the output"""
        original_output = None
        modified_output = None

        def hook_original(module, input, output):
            nonlocal original_output
            original_output = output.detach()

        def hook_modified(module, input, output):
            nonlocal modified_output
            modified = output.clone()
            modified[:, :, neuron_idx] = 0  # Zero out specific neuron
            modified_output = modified
            return modified

        layer = list(self.transformer.layers)[layer_idx]

        # Get original output
        handle = layer.register_forward_hook(hook_original)
        self(x)
        handle.remove()

        # Get modified output
        handle = layer.register_forward_hook(hook_modified)
        self(x)
        handle.remove()

        return original_output, modified_output

def visualize_attention(attention_weights, tokens=None):
    """Visualize attention patterns"""
    plt.figure(figsize=(10, 8))
    plt.imshow(attention_weights[0].cpu(), cmap="viridis")

    if tokens is not None:
        plt.xticks(range(len(tokens)), tokens, rotation=45)
        plt.yticks(range(len(tokens)), tokens)

    plt.colorbar()
    plt.title("Attention Pattern")
    plt.show()


# Initialize model
model = InterpretableTransformer(vocab_size=1000, d_model=256, nhead=8, num_layers=4)

# Sample input
input_ids = torch.randint(0, 1000, (1, 20))  # Batch size 1, sequence length 20

# Get attention patterns
attention_patterns = model.get_attention_patterns(input_ids)

# Analyze neuron activations
top_neurons, activation_values = model.analyze_neuron_activations(input_ids, layer_idx=0)

# Perform intervention study
original, modified = model.intervention_study(input_ids, layer_idx=0, neuron_idx=42)

# Visualize attention
visualize_attention(attention_patterns[0])  # Visualize first layer's attention
```

!!! info

    Each component helps us understand different aspects of the model:

    - Attention patterns show how the model relates different tokens to each other
    - The neuron activation analysis reveals which neurons are most important for processing specific inputs
    - Causal intervention helps us understand the role of specific neurons by observing how the output changes when we modify them
    - Visualization tools help us interpret these patterns more intuitively

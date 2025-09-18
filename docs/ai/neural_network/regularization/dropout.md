# Dropout

## Description

Dropout is a powerful regularization technique that randomly "drops out" a portion of neurons during training.

<img src="image1.png" style="width:2in" />

It helps combat overfitting by randomly deactivating a fraction of neurons during each training iteration, **forcing the network to develop redundant pathways for information flow**.
This technique **prevents neurons from becoming overly dependent** on each other by creating a form of ensemble learning within a single network, where different subnetworks handle similar tasks.
The result is a more robust model that relies on distributed representations rather than memorizing specific patterns, ultimately improving generalization to unseen data when all neurons are active during inference.

## Example

```python
import torch
import torch.nn as nn

class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_layers, dropout=0.1, max_len=1000):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_embedding = nn.Embedding(max_len, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model, nhead, 4*d_model, dropout)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)
        self.fc_out = nn.Linear(d_model, vocab_size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        seq_len = x.size(1)
        pos = torch.arange(seq_len, device=x.device)
        x = self.embedding(x) + self.pos_embedding(pos)
        x = self.dropout(x)
        x = self.transformer(x.transpose(0, 1)).transpose(0, 1)
        return self.fc_out(x)
```

!!! info

    In this implementation, dropout is applied after the embedding layer and within each transformer layer.

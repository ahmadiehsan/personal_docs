# Supervised Fine-Tuning (SFT)

## Description

Supervised Fine-Tuning (SFT) is the standard approach for adapting large pretrained models to specific downstream tasks.
In SFT, all or most of the model's parameters are updated using labeled data, typically via standard supervised learning objectives (e.g., cross-entropy loss for classification or language modeling). This method is straightforward and often yields strong performance, but it can be computationally expensive and requires significant resources, especially for large models.

!!! info

    SFT is the most direct way to adapt a pretrained model to a new task.

## Workflow

1. **Prepare Labeled Data**: Collect and preprocess a dataset with input-output pairs for the target task.
2. **Initialize Model**: Start with a pretrained model (e.g., a language model or vision transformer).
3. **Fine-Tune Parameters**: Train the model on the labeled data, updating all (or most) of its parameters.
4. **Evaluate**: Assess the model's performance on a validation or test set.

!!! warning

    SFT can require significant GPU memory and storage, especially for very large models, since all weights are updated and stored.

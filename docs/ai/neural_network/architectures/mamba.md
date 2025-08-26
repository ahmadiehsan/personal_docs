# Mamba [NLP]

## Description

Mamba is a next-generation sequence model that combines efficiency and state-of-the-art performance without relying on attention or MLP blocks.
Designed to overcome the computational inefficiency of Transformers on long sequences, Mamba uses **Selective Structured State Space Models (SSMs)** with input-dependent parameters, enabling content-based reasoning and selective information propagation for discrete modalities like language.

- **Fast and Scalable**: Achieves **5x higher inference throughput** than Transformers with **linear memory and computational scaling** for sequences up to a million tokens.
- **Simplified Design**: Optimized with a hardware-aware parallel algorithm in recurrent mode, eliminating attention mechanisms entirely.
- **Top-Tier Performance**: Delivers state-of-the-art results across diverse modalities such as language, audio, and genomics. In language modeling, the Mamba-3B model outperforms same-size Transformers and matches Transformers twice its size.

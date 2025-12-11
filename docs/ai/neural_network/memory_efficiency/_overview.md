# Overview

## Description

Memory efficiency techniques in neural networks aim to reduce the amount of GPU/TPU memory required during training or inference.

This allows models to run on smaller devices, train with larger batch sizes, or scale to deeper architectures without exceeding hardware limits.

!!! info

    These methods often work by reducing intermediate activations, recomputing values when needed, or structuring computation more efficiently. While they save memory, they may introduce trade-offs such as additional compute or slower training.

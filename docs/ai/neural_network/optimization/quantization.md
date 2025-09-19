# Quantization

## Description

The weights of an LLM are numeric values with a given precision, which can be expressed by the number of bits like float64 or float32.
If we lower the amount of bits to represent a value, we get a less accurate result.
However, if we lower the number of bits we also lower the memory requirements of that model.

![](quantization/overview.png)

!!! info

    Notice the lowered accuracy when we halve the number of bits.

## Varieties

| Strategy        | Accuracy                                         | Complexity                         | Performance                             | Resources                      |
| --------------- | ------------------------------------------------ | ---------------------------------- | --------------------------------------- | ------------------------------ |
| PTQ             | Good for simple models; declines with complexity | Low; minimal setup                 | 75% storage reduction; 2-4x speedup     | Low; minimal compute needed    |
| QAT             | Highest; best for sub-8-bit                      | High; requires extended training   | High compression with the best accuracy | High; intensive training needs |
| Dynamic         | Good for RNNs; weak for CNNs                     | Medium; runtime overhead           | Good memory savings; slower compute     | Medium; runtime processing     |
| Mixed-Precision | High; flexible precision options                 | Medium-high; layer-specific tuning | Hardware-dependent speedup              | Medium-high during setup       |

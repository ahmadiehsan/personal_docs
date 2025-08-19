# Quantization

## Description

The weights of an LLM are numeric values with a given precision, which can be expressed by the number of bits like float64 or float32.
If we lower the amount of bits to represent a value, we get a less accurate result.
However, if we lower the number of bits we also lower the memory requirements of that model.

![](quantization/overview.png)

!!! info

    Notice the lowered accuracy when we halve the number of bits.

# AI

## NN Memory

- Memory: **3.6 bytes** per parameter
- Double Descent: At first, the model tries to just memorize the data, so it gradually improves. But once its memory fills up, it has to slowly start discarding what it memorized and actually learn the underlying logic of the subject. As a result, the model keeps getting better over time, then suddenly its quality drops, and after that, it begins improving again.

## Transformer Layers

Different layers in a transformer specialize in different linguistic properties:

- **Lower layers**: Capture syntax and token identity.
- **Middle layers**: Handle grammar and sentence structure.
- **Deeper layers**: Focus on semantics, reasoning, and factual recall.

## H100 Varieties

| Feature               | H100 PCIe                                                                          | H100 SXM                                                                          | H100 NVL                                                        |
| --------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Connection**        | Standard PCIe slot                                                                 | Custom socket on DGX/HGX boards                                                   | PCIe slot (two cards bridged)                                   |
| **RAM to VRAM Speed** | Slower (limited by PCIe bus)                                                       | Fastest                                                                           | Slower (limited by PCIe bus)                                    |
| **GPU to GPU Speed**  | Slower                                                                             | Fastest (via NVLink on the board)                                                 | Very Fast (via dedicated NVLink Bridge)                         |
| **VRAM Type**         | HBM2e                                                                              | HBM3                                                                              | HBM3                                                            |
| **VRAM Size**         | 80 GB                                                                              | 80 GB                                                                             | 192 GB total (2x 96 GB)                                         |
| **Best For**          | General compatibility, single-card setups where PCIe bandwidth isn't a bottleneck. | Demanding single-GPU or multi-GPU tasks needing the highest RAM-to-GPU bandwidth. | Dual-GPU tasks with massive data transfer between the two GPUs. |
| **Key Downside**      | Slower data transfer to and from system RAM.                                       | Requires specific, expensive motherboards (DGX/HGX).                              | Acts as a pair; not ideal for scaling beyond two bridged GPUs.  |

## Singularity

- Researcher: Ray Kurzweil
- Reference: Based on Moore's law

## Godfathers

=== "AI"

    <img src="godfather_1.jpg" style="width:3.02139in" />

=== "Convolutional NN"

    <img src="godfather_2.jpg" style="width:2.99608in" />

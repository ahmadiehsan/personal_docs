# Weight Initialization

## Description

Weight initialization is a crucial technique for training deep neural networks effectively.
Proper initialization helps prevent problems like exploding or vanishing gradients, enabling faster convergence and better model performance.

Different activation functions require different initialization strategies to maintain stable gradient flow through the network.

## Formula

=== "RELU"

    $$
    \sqrt{\frac{2}{size^{[l-1]}}}
    $$

    ```python
    W = np.random.randn(size_l, size_l-1) * np.sqrt(2/size_l-1)
    ```

=== "TanH"

    $$
    \sqrt{\frac{1}{size^{[l-1]}}}
    $$

    ```python
    W = np.random.randn(size_l, size_l-1) * np.sqrt(1/size_l-1)
    ```

=== "Heuristic"

    $$
    \sqrt{\frac{2}{size^{[l-1]} + size^{[l]}}}
    $$

    ```python
    W = np.random.randn(size_l, size_l-1) * np.sqrt(2 / (size_l-1 + size_l))
    ```

## Example

=== "RELU"

    ```python
    import torch.nn as nn

    def use_he_init(module):
        if isinstance(module, nn.Linear):
            nn.init.kaiming_uniform_(module.weight)
            nn.init.zeros_(module.bias)

    model = nn.Sequential(
        nn.Linear(50, 40), nn.ReLU(),
        nn.Linear(40, 1), nn.ReLU()
    )
    model.apply(use_he_init)
    ```

# Fast Gradient Sign Method (FGSM) [Noise]

## Description

Fast Gradient Sign Method (FGSM) is a technique for creating adversarial examples by adding a small, targeted perturbation to input data, pushing the model to misclassify.

It works by calculating the gradient of the loss function with respect to the input and applying a slight adjustment in the direction that maximizes the model's error.
The input data is slightly changed by a small amount, controlled by a factor called $\epsilon$, to create an "adversarial example" that can fool a machine learning model.

!!! info

    FGSM is commonly used to test model robustness and for adversarial training, where models are trained on adversarial examples to enhance security. However, FGSM’s one-step nature makes it fast but less effective against strong defenses, unlike iterative methods that achieve higher attack success.

## Example

```python
import torch

def fgsm_attack(image, epsilon, data_grad):
    sign_data_grad = data_grad.sign()
    perturbed_image = image + epsilon * sign_data_grad
    perturbed_image = torch.clamp(perturbed_image, 0, 1)
    return perturbed_image
```

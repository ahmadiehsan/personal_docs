# Fast Gradient Sign Method (FGSM) [Noise]

## Description

Fast Gradient Sign Method (FGSM) is a technique for creating adversarial examples by adding a small, targeted perturbation to input data, pushing the model to misclassify.

It works by calculating the gradient of the loss function with respect to the input and applying a slight adjustment in the direction that maximizes the model's error.
The input data is slightly changed by a small amount, controlled by a factor called $\epsilon$, to create an "adversarial example" that can fool a machine learning model.

!!! info

    FGSM is commonly used to test model robustness and for adversarial training, where models are trained on adversarial examples to enhance security. However, FGSM's one-step nature makes it fast but less effective against strong defenses, unlike iterative methods that achieve higher attack success.

## Example

```python
import torch

def adversarial_train_step(model, inputs, labels, epsilon=0.1):
    embeds = model.get_input_embeddings()(inputs["input_ids"])
    embeds.requires_grad = True
    outputs = model(inputs, inputs_embeds=embeds)
    loss = torch.nn.functional.cross_entropy(outputs.logits, labels)
    loss.backward()

    perturb = epsilon * embeds.grad.detach().sign()
    adv_embeds = embeds + perturb
    adv_outputs = model(inputs_embeds=adv_embeds)
    adv_loss = torch.nn.functional.cross_entropy(adv_outputs.logits, labels)

    return 0.5 * (loss + adv_loss)

def adversarial_train(model, train_dataloader, optimizer, num_epochs=3):
    for epoch in range(num_epochs):
        for batch in train_dataloader:
            inputs, labels = batch
            loss = adversarial_train_step(model, inputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    return model
```

# Noise Injection {FGSM} {DP}

## Description

Noise injection is a regularization technique commonly used to improve the generalization of machine learning models.
By adding a small amount of noise to the input data, weights, or activation functions.

Noise injection helps prevent overfitting, the technique forces the model to be less reliant on specific patterns in the training data, encouraging it to learn more robust, general features that apply across different datasets.

This approach is particularly useful in neural networks, where noise such as the following can be injected at various stages:

- **Input noise**: Adds noise directly to the input data, helping the model become more robust to variations in the input
- **Weight noise**: Perturbs the weights during training, encouraging the model to generalize better
- **Activation noise**: Adds noise to the activation functions, leading to smoother decision boundaries and reducing overfitting

## Varieties

=== "Standard"

    Standard Noise Injection involves adding random noise directly to the input data during training. This helps the model become less sensitive to small changes and improves its ability to generalize to unseen data.

=== "FGSM"

    Fast Gradient Sign Method (FGSM) is a technique for creating adversarial examples by adding a small, targeted perturbation to input data, pushing the model to misclassify.

    It works by calculating the gradient of the loss function with respect to the input and applying a slight adjustment in the direction that maximizes the model's error.
    The input data is slightly changed by a small amount, controlled by a factor called $\epsilon$, to create an "adversarial example" that can fool a machine learning model.

    !!! info

        FGSM is commonly used to test model robustness and for adversarial training, where models are trained on adversarial examples to enhance security. However, FGSM's one-step nature makes it fast but less effective against strong defenses, unlike iterative methods that achieve higher attack success.

=== "DP"

    Differential privacy (DP) is a technique that adds carefully calibrated noise to data or computations to protect individual privacy while still allowing useful insights, ensuring that the inclusion or exclusion of any single data point does not significantly affect model performance.

    Is a technique used to enhance model privacy by adding noise to the model's training process, which protects individual data points from being exposed in model outputs or learned representations.
    By introducing controlled randomness, DP-based regularization limits the model's reliance on any specific data sample, thereby reducing the risk of overfitting and making the model less sensitive to variations in individual data points.

    !!! info

        This method is particularly valuable in privacy-sensitive applications, as it ensures that models can learn generalizable patterns without revealing specific information about the training data, making it useful in healthcare, finance, and other areas requiring data confidentiality.

## Example

=== "Standard"

    ```python
    import torch
    from torch.nn.utils import clip_grad_norm_
    from torch.optim import AdamW

    def train(model, dataloader, grad_clip=1.0, noise_factor=0.01, lr=5e-5, epochs=3):
        optimizer = AdamW(model.parameters(), lr=lr)

        for e in range(epochs):
            model.train()
            total_loss = 0

            for batch in dataloader:
                optimizer.zero_grad()

                input_ids = batch["input_ids"]
                noise = torch.randn_like(input_ids, dtype=torch.float) * noise_factor
                noisy_inputs = noisy_inputs = input_ids.float() + noise
                noisy_inputs = noisy_inputs.long().clamp(min=0, max=model.config.vocab_size - 1)

                outputs = model(input_ids=noisy_inputs, labels=input_ids)
                loss = outputs.loss
                loss.backward()

                clip_grad_norm_(model.parameters(), grad_clip);
                optimizer.step()
                total_loss += loss.item()

            print(f"Epoch {e+1}, Loss: {total_loss/len(dataloader):.4f}")
    ```

    !!! info

        **What does `clip_grad_norm_` do?**

        It limits (clips) the size of gradients during backpropagation.
        This prevents *exploding gradients* (when gradients become too large), helping the model train more stably and avoiding NaN losses.

=== "FGSM"

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

=== "DP"

    ```python
    import torch

    class DPOptimizer(torch.optim.Optimizer):
        def __init__(self, params, noise_multiplier=1.0, max_grad_norm=1.0):
            super().__init__(params, {})  # initialize base Optimizer
            self.noise_multiplier = noise_multiplier
            self.max_grad_norm = max_grad_norm

        def step(self, closure=None):
            # Clip gradients
            torch.nn.utils.clip_grad_norm_(self.param_groups[0]["params"], self.max_grad_norm)

            # Add noise
            for p in self.param_groups[0]["params"]:
                noise = torch.randn_like(p.grad) * self.noise_multiplier
                p.grad.add_(noise)
    ```

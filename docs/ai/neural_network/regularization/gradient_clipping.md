# Gradient Clipping

## Description

Gradient Clipping mitigates the exploding gradients problem by clipping the gradients during backpropagation so that they never exceed some threshold.

!!! info

    This technique is generally used in recurrent neural networks, where using batch norm is tricky.

## Example

=== "clip_grad_norm_"

    ```python
    import torch.nn as nn

    for epoch in range(n_epochs):
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)

            optimizer.zero_grad()
            y_pred = model(X_batch)
            loss = loss_fn(y_pred, y_batch)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
    ```

    !!! info

        If the original gradient vector is `[0.9, 100.0]`, it points mostly in the direction of the second dimension; but once you clip it by norm, you get `[0.00899964, 0.9999595]`, which would preserve the vector's orientation, but almost eliminate the first component.

=== "clip_grad_value_"

    ```python
    import torch.nn as nn

    for epoch in range(n_epochs):
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)

            optimizer.zero_grad()
            y_pred = model(X_batch)
            loss = loss_fn(y_pred, y_batch)
            loss.backward()
            nn.utils.clip_grad_value_(model.parameters(), max_norm=1.0)
            optimizer.step()
    ```

    !!! info

        If the original gradient vector is `[0.9, 100.0]`, it points mostly in the direction of the second dimension; but once you clip it by value, you get `[0.9, 1.0]`, which points roughly at the diagonal between the two axes.

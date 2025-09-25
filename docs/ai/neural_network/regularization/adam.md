# Adam {AdamW} {ADOPT}

## Description

=== "Adam"

    <img src="image2.jpg" style="width:5in" />

    <span dir="rtl">طبق یه الگوریتمی تشخیص میده اگر حرکت به سمت نقطه minimum داره صورت میگیره سرعت حرکت رو با افزایش مقدار α بیشتر میکنه در غیر این صورت سرعت رو با کاهش مقدار α کمتر میکنه.</span>

=== "AdamW"

    **AdamW** is an optimization algorithm that **builds upon the Adam** technique by **decoupling weight decay from the gradient update**.

    While Adam combines momentum and adaptive learning rates to efficiently move towards the minimum, AdamW improves generalization by applying weight decay directly to the parameters, rather than through the gradients.
    This adjustment helps prevent overfitting and leads to better performance in training deep neural networks.

=== "ADOPT"

    **ADOPT** offers a better alternative for optimizing Deep Learning models and LLMs.
    The key issue with Adam was the lack of convergence guarantee during weight updates, which is addressed by ADOPT.
    This isn't just theoretical—ADOPT has been shown to outperform Adam in most tasks, including GPT-2 pretraining.

    The core idea and solution to ensure convergence are:

    1. Removing the current gradient from the second momentum estimate.
    2. Normalizing the gradient before updating the momentum.

## Formula

=== "Adam"

    Initialize: $V_{dw} = 0$, $S_{dw} = 0$, $V_{db} = 0$, $S_{db} = 0$

    On iteration $t$: Compute $dW$, $db$ using the current mini-batch.

    $V_{dw} = \beta_1 V_{dw} + (1 - \beta_1) dW$, $V_{db} = \beta_1 V_{db} + (1 - \beta_1) db$ <-- "momentum" $\beta_1$

    $S_{dw} = \beta_2 S_{dw} + (1 - \beta_2) dW^2$, $S_{db} = \beta_2 S_{db} + (1 - \beta_2) db^2$ <-- "RMSprop" $\beta_2$

    $V_{dw}^{\text{corrected}} = V_{dw} / (1 - \beta_1^t)$, $V_{db}^{\text{corrected}} = V_{db} / (1 - \beta_1^t)$

    $S_{dw}^{\text{corrected}} = S_{dw} / (1 - \beta_2^t)$, $S_{db}^{\text{corrected}} = S_{db} / (1 - \beta_2^t)$

    $W := W - \alpha \frac{V_{dw}^{\text{corrected}}}{\sqrt{S_{dw}^{\text{corrected}}} + \epsilon}$, $b := b - \alpha \frac{V_{db}^{\text{corrected}}}{\sqrt{S_{db}^{\text{corrected}}} + \epsilon}$

    !!! info

        <span dir="rtl">در اصل این تکنیک ترکیبی از تکنیک های Gradient Descent With Momentum و RMS-prop هستش.</span>

=== "AdamW"

=== "ADOPT"

## Example

=== "Adam"

    ```python
    from torch.optim import Adam

    optimizer = Adam(model.parameters(), lr=1e-3)
    ```

=== "AdamW"

    ```python
    from torch.optim import AdamW

    optimizer = AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
    ```

    !!! info

        The `weight_decay` parameter controls the strength of L2 regularization (Ridge).

=== "ADOPT"

    ```python
    from adopt import ADOPT

    #optimizer = Adam(model.parameters(), lr=1e-3)  # We don't need Adam anymore!
    optimizer = ADOPT(model.parameters(), lr=1e-3)
    ```

# ReLU [$0$ to $+\infty$] {Leaky} {Swish}

## Description

- Its complete name is "Rectified Linear Unit"
- In other words, the activation is simply the input if the input is positive; otherwise, it's zero.
- It doesn't activate all the neurons at the same time, meaning that the neurons will only be deactivated if the output of the linear transformation is less than 0. This makes the network sparse and efficient. However, ReLU units can be fragile during training and can "die" (they stop learning completely) if a large gradient flows through them.
- The ReLU function has become very popular in recent years.

!!! info

    <span dir="rtl">زمانی که میخوایم خروجی شبکه عصبی ۰ یا بیشتر باشه از این فانکشن در لایه آخر استفاده می کنیم</span>

## Varieties

=== "Standard"

    Standard ReLU returns the input if it is positive; otherwise, it outputs zero.

=== "Leaky *"

    Leaky ReLU is a variant of ReLU that addresses the "dying ReLU" problem.
    Instead of defining the function as 0 for negative x.

    This allows the function to "leak" some information when the input is negative and helps to mitigate the dying ReLU problem.

=== "ELU"

    Exponential Linear Unit (ELU) is also a variant of ReLU that modifies the function to be a non-zero value for negative x.

=== "Softplus"

    Softplus is a smoothed version of ReLU, both ReLU and Softplus are similar, except near 0 where the softplus is smooth and differentiable.

=== "GELU"

    Gaussian Error Linear Unit (GELU) uses the cumulative distribution function of a Gaussian distribution.
    GELU is smooth and provides better performance in transformer models.

=== "Swish *"

    Swish is a self-gated activation function that combines smoothness with non-monotonicity.
    It has shown better performance than ReLU in many deep networks.

=== "SwiGLU"

    A gated linear unit variant using Swish activation, commonly used in transformer architectures.
    It provides better expressiveness through element-wise gating mechanisms.

=== "Mish"

    Mish is a smooth, non-monotonic activation function combining tanh and softplus.
    It provides good regularization properties and smooth gradients throughout the domain.

=== "ReLU$^2$"

    Squared ReLU is the square of the standard ReLU output. It amplifies positive activations while maintaining sparsity.

## Formula

=== "Standard"

    <img src="relu_diagram.jpg" style="width:688px" />

=== "Leaky"

    <img src="leaky_diagram.png" style="width:688px" />

=== "ELU"

    <img src="elu_diagram.jpg" style="width:688px" />

    Here alpha (α) is a constant that defines function smoothness when inputs are negative.
    ELU tends to converge cost to zero faster and produce more accurate results.
    However, it can be slower to compute because of the use of the exponential operation.

=== "Softplus"

    $$
    f(x) = \ln(1 + e^x)
    $$

    <img src="softplus_diagram.png" style="width:688px" />

=== "GELU"

    $$f(x) = x \cdot \Phi(x)$$

    where $\Phi(x)$ is the cumulative distribution function of the standard Gaussian.

    <img src="gelu_diagram.png" style="width:688px" />

=== "Swish"

    $$f(x) = x \cdot \sigma(\beta x)$$

    where $\sigma$ is the sigmoid function and $\beta$ is a learnable parameter.

    <img src="swish_diagram.png" style="width:688px" />

=== "SwiGLU"

    $$f(x) = (x \cdot \sigma(\beta x)) \otimes W$$

    where $\otimes$ is element-wise multiplication with learned gate weights.

=== "Mish"

    $$f(x) = x \cdot \tanh(\ln(1 + e^x))$$

    A smooth, self-regularizing activation combining tanh and softplus.

    <img src="mish_diagram.png" style="width:688px" />

=== "ReLU$^2$"

    $$f(x) = \max(0, x)^2$$

    Squares the ReLU output, amplifying positive activations while maintaining sparsity.

    <img src="relu_2_diagram.png" style="width:688px" />

## VS

| Function       | Vibe & Pros                                                             | The Catch                                                                     | Best For                                                               |
| :------------- | :---------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **ReLU**       | **The Standard.** Fast, simple, induces sparsity.                       | **Dead Neurons.** Gradients kill parts of the network if inputs are negative. | Default for CNNs and simple MLPs. Start here.                          |
| **Leaky ReLU** | **The Fixer.** Like ReLU but allows small gradients when $x < 0$.       | $\alpha$ is another hyperparam to worry about.                                | GANs, or deep networks where neurons are dying.                        |
| **ELU**        | **The Stabilizer.** Pushes mean activation to zero, faster convergence. | **Slow.** Computing $e^x$ is expensive.                                       | Noisy data or when Batch Norm isn't an option.                         |
| **Softplus**   | **The Smooth ReLU.** Differentiable everywhere.                         | Can saturate; computation is heavy.                                           | Output layers enforcing positivity (e.g., standard deviation in VAEs). |
| **GELU**       | **The Transformer Standard.** Smooth, probabilistic interpretation.     | Slightly more compute than ReLU.                                              | **NLP / LLMs.** (BERT, GPT series).                                    |
| **Swish**      | **Google's Baby.** Smooth, non-monotonic. Often beats ReLU.             | Slower to train than ReLU.                                                    | Modern CNNs (EfficientNet), some Transformers.                         |
| **Mish**       | **The Optimizer.** Deeply smooth, self-regularizing.                    | Very expensive ops ($\tanh, \ln, \exp$).                                      | Computer Vision (YOLOv4) where every 1% accuracy counts.               |
| **SwiGLU**     | **The Modern King.** Actually a Gated Linear Unit using Swish.          | **Parameter Hungry.** Requires two sets of weights (gate + value).            | **SOTA LLMs** (LLaMA, PaLM, Mistral).                                  |
| **ReLU$^2$**   | **The Primer.** Super-linear growth.                                    | Gradient explosion risk; aggressive.                                          | Physics-informed NNs, some efficient Transformers (Primer paper).      |

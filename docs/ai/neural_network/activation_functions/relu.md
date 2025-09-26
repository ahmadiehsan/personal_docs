# ReLU [$0$ to $+\infty$] {Leaky} {ELU} {Softplus}

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

=== "Leaky"

    Leaky ReLU is a variant of ReLU that addresses the "dying ReLU" problem.
    Instead of defining the function as 0 for negative x.

    This allows the function to "leak" some information when the input is negative and helps to mitigate the dying ReLU problem.

=== "ELU"

    Exponential Linear Unit (ELU) is also a variant of ReLU that modifies the function to be a non-zero value for negative x.

=== "Softplus"

    Softplus is a smoothed version of ReLU, both ReLU and Softplus are similar, except near 0 where the softplus is smooth and differentiable.

## Formula

=== "Standard"

    <img src="relu_diagram.jpg" style="width:4in" />

=== "Leaky"

    <img src="leaky_diagram.png" style="width:3in" />

=== "ELU"

    <img src="elu_diagram.jpg" style="width:4in" />

    Here alpha (α) is a constant that defines function smoothness when inputs are negative.
    ELU tends to converge cost to zero faster and produce more accurate results.
    However, it can be slower to compute because of the use of the exponential operation.

=== "Softplus"

    $$
    f(x) = \ln(1 + e^x)
    $$

    <img src="softplus_diagram.png" style="width:3in" />

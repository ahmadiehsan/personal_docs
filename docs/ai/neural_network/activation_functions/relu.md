# ReLU {$0$ to $+\infty$}

## Description

- Its complete name is "Rectified Linear Unit"
- In other words, the activation is simply the input if the input is positive; otherwise, it's zero.
- It doesn't activate all the neurons at the same time, meaning that the neurons will only be deactivated if the output of the linear transformation is less than 0. This makes the network sparse and efficient. However, ReLU units can be fragile during training and can "die" (they stop learning completely) if a large gradient flows through them.
- The ReLU function has become very popular in recent years.

!!! info

    <span dir="rtl">زمانی که میخوایم خروجی شبکه عصبی ۰ یا بیشتر باشه از این فانکشن در لایه آخر استفاده می کنیم</span>

## Formula

<img src="image3.jpg" style="width:3.92476in" />

## Varieties

### Leaky Relu

Leaky ReLU is a variant of ReLU that addresses the "dying ReLU" problem. Instead of defining the function as 0 for negative x.

<img src="image1.png" style="width:2.43955in" />

This allows the function to "leak" some information when the input is negative and helps to mitigate the dying ReLU problem.

### Exponential Linear Unit (ELU)

ELU is also a variant of ReLU that modifies the function to be a non-zero value for negative x.

<img src="image2.jpg" style="width:4.09113in" />

Here alpha (α) is a constant that defines function smoothness when inputs are negative.
ELU tends to converge cost to zero faster and produce more accurate results.
However, it can be slower to compute because of the use of the exponential operation.

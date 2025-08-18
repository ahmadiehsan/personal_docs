# TanH {-1 to 1}

## Description

The tanh function also takes a real-valued input and squashes it to range between -1 and 1.
Unlike the sigmoid function, its output is zero-centered because its range is symmetric around the origin.

However, it has one major drawbacks:

- the vanishing gradients problem (gradients are very small for large positive or negative inputs, which can slow down learning during backpropagation)

!!! info

    <span dir="rtl">معمولا تو لایه های مخفی (hidden layers) از این فانکشن به عنوان پیش فرض استفاده میشه مگر این که کاربری دیگه ای رو بخوایم</span>

## Formula

$$
\tanh(\Sigma) = \frac{e^{\Sigma} - e^{-\Sigma}}{e^{\Sigma} + e^{-\Sigma}}
$$

<img src="image1.png" style="width:2.73813in" />

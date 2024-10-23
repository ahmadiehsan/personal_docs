# Sigmoid [0 to 1]

## Description

This is where we're essentially classifying the input as either 0 or 1. The sigmoid function takes a real-valued input and squashes it to range between 0 and 1. It's often used in the output layer of a binary classification network.

However, it has two major drawbacks:

- the vanishing gradients problem (gradients are very small for large positive or negative inputs, which can slow down learning during backpropagation)
- the outputs are not zero-centered

!!! info

    <span dir="rtl">این مدل در اصل یک حالت خاص (دو دسته ای) از مدل Softmax هستش</span>

## Formula

<img src="image1.jpg" style="width:3.82609in" />

# Sigmoid [0 to 1]

## Description

This is where we’re essentially classifying the input as either 0 or 1. The sigmoid function takes a real-valued input and squashes it to range between 0 and 1. It’s often used in the output layer of a binary classification network.

<img src="image1.jpg" style="width:3.82609in" />

However, it has two major drawbacks:

- the vanishing gradients problem (gradients are very small for large positive or negative inputs, which can slow down learning during backpropagation)
- the outputs are not zero-centered

<span dir="rtl">نکات:</span>

- <span dir="rtl">این مدل در اصل یک حالت خاص (دو دسته ای) از مدل</span> <span dir="ltr">Softmax</span> <span dir="rtl">هستش</span>

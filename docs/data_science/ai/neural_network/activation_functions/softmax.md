# Softmax [0 to 1]

## Description

The softmax function is often used in the output layer of a classifier where we’re trying to assign the input to one of several classes. It gives the probability that any given input belongs to each of the possible classes

The denominator normalizes the probabilities, so they all sum up to 1 across all classes. The softmax function is also used in multinomial logistical regression.

Is a mathematical function that converts a vector of numbers into a vector of probabilities, where the probabilities of each value are proportional to the relative scale of each value in the vector.

<img src="image1.jpg" style="width:3.55568in" />

<span dir="rtl">نکات:</span>

- <span dir="rtl">به شکل کلی برای دسته بندی اطلاعات استفاده میشه (Multiclass Classification)</span>

## Formula

<img src="image3.png" style="width:1.72471in" />

<img src="image4.jpg" style="width:2.07097in" />

- <span dir="rtl">تو این فرمول N به معنی تعداد دسته ها و j به معنی خود دسته ها هستن</span>
- <span dir="rtl">هر a به معنی احتمال بودن در اون دسته خاص هستش و مجموع تمامی a ها باید ۱ بشه</span>
- <span dir="rtl">نمونه فرمول باز شده و ساده شده تو تصویر زیر اومده:</span>

<img src="image2.png" style="width:2.48392in" />

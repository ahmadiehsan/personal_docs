# Normalization (Min-Max) [Scaling]

## Description

Also known as normalization, this technique scales the values of the feature to be between a specified range, typically between 0 and 1 (for regular machine learning models, and sometimes -1 and 1 for deep learning models).

## Formula

Normal version:

$$
x' = \frac{x - \min(x)}{\max(x) - \min(x)}
$$

where $x$ is an original value, $x'$ is the normalized value.

Generalized version (Restrict the range of values in the dataset between any arbitrary points a and b):

$$
X' = a + \frac{(X - X_{min})(b - a)}{X_{max} - X_{min}}
$$

## Example

<img src="image3.png" style="width:5in" />

<span dir="rtl">برای اینپوت هایی (فیچر هایی) که خیلی دامنه متفاوتی با هم دارن از این تکنیک استفاده میکنیم.</span>

<img src="image4.jpg" style="width:5in" />

<span dir="rtl">تو تصویر بالا با استفاده از این تکنیک فیچر ها تو رنج های مشابه هم در اومدن که تو تصویر با اسم Normalized مشخص شده، تو این حالت سیستم خیلی سریع تر آموزش میبینه.</span>

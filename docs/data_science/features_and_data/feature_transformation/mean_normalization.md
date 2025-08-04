# Mean Normalization {Scaling}

## Formula

$$
x' = \frac{x - \bar{x}}{\max(x) - \min(x)}
$$

where $x$ is an original value, $x'$ is the normalized value, $\bar{x} = \text{average}(x)$

## Example

<img src="image3.png" style="width:5in" />

<span dir="rtl">مقدار $\mu$ برابر است با میانگین اعداد در آن اینپوت (فیچر) خاص</span>

<img src="image4.jpg" style="width:6in" />

<img src="image2.jpg" style="width:4.5in" />

<span dir="rtl">تو دو تصویر بالا نمونه از این تکنیک در الگوریتم Collaborative Filtering میبینیم با اضافه کردن $\mu$ به فرمول محاسبه باعث میشه کسایی که به یه فیلم امتیاز ندادن هم یه عدد اولیه براشون در نظر گرفته بشه.</span>

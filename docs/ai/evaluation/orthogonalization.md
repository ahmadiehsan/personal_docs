# Orthogonalization

## Description

<span dir="rtl">برای بهبود عملکرد سیستم بسته به مشکل راه های مختلفی وجود داره که فقط رو یه جنبه از الگوریتم تاثیر میذاره و با جنبه های دیگه کاری نداره، اول لازمه طبق تصویر زیر مشکل سیستم رو تشخیص بدین:</span>

<img src="image1.jpg" style="width:3.5in" />

<span dir="rtl">در زیر تمامی حالات زیاد بودن error بین دو موقعیت رو با راه حلش میبینیم:</span>

- <span dir="rtl">بین human و training: یعنی سیستم high bias هست</span>
- <span dir="rtl">بین training و training-dev: یعنی سیستم high variance هست</span>
- <span dir="rtl">بین training-dev و dev: یعنی سیستم مشکل data mismatch داره</span>
- <span dir="rtl">بین dev و test: یعنی دیتای dev و test از یک فضای یکسان نیست</span>

<span dir="rtl">حالا بسته به تشخیص بالا تو دو تصویر زیر مشخص شده که برای هر مشکل سراغ چه راهی بریم:</span>

<img src="image3.jpg" style="width:5in" />

<img src="image2.jpg" style="width:4.5in" />

- <span dir="rtl">برای فیت شدن بهتر training set از bigger network و Adam استفاده میکنیم</span>
- <span dir="rtl">برای فیت شدن بهتر dev set از Regularization و bigger treating set استفاده میکنیم</span>
- <span dir="rtl">برای فیت شدن بهتر test set از bigger dev set استفاده میکنیم</span>
- <span dir="rtl">برای اجرای خوب روی دیتا های واقعی از change dev set یا change cost function استفاده میکنیم</span>

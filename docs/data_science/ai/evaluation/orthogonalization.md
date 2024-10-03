# Orthogonalization

## Description

<span dir="rtl">برای بهبود عملکرد سیستم بسته به مشکل راه های مختلفی وجود داره که فقط رو یه جنبه از الگوریتم تاثیر میذاره و با جنبه های دیگه کاری نداره، اول لازمه طبق تصویر زیر مشکل سیستم رو تشخیص بدین:</span>

<img src="image1.jpg" style="width:2.99433in" />

<span dir="rtl">در زیر تمامی حالات زیاد بودن</span> <span dir="ltr">error</span> <span dir="rtl">بین دو موقعیت رو با راه حلش میبینیم:</span>

- <span dir="rtl">بین</span> <span dir="ltr">human</span> <span dir="rtl">و</span> <span dir="ltr">training</span><span dir="rtl">: یعنی سیستم</span> <span dir="ltr">high bias</span> <span dir="rtl">هست</span>
- <span dir="rtl">بین</span> <span dir="ltr">training</span> <span dir="rtl">و</span> <span dir="ltr">training-dev</span><span dir="rtl">: یعنی سیستم</span> <span dir="ltr">high variance</span> <span dir="rtl">هست</span>
- <span dir="rtl">بین</span> <span dir="ltr">training-dev</span> <span dir="rtl">و</span> <span dir="ltr">dev</span><span dir="rtl">: یعنی سیستم مشکل</span> <span dir="ltr">data mismatch</span> <span dir="rtl">داره</span>
- <span dir="rtl">بین</span> <span dir="ltr">dev</span> <span dir="rtl">و</span> <span dir="ltr">test</span><span dir="rtl">: یعنی دیتای</span> <span dir="ltr">dev</span> <span dir="rtl">و</span> <span dir="ltr">test</span> <span dir="rtl">از یک فضای یکسان نیست</span>

<span dir="ltr"></span>

<span dir="rtl">حالا بسته به تشخیص بالا تو دو تصویر زیر مشخص شده که برای هر مشکل سراغ چه راهی بریم:</span>

<img src="image3.jpg" style="width:4.24161in" />

<img src="image2.jpg" style="width:3.74768in" />

- <span dir="rtl">برای فیت شدن بهتر</span> <span dir="ltr">training set</span> <span dir="rtl">از</span> <span dir="ltr">bigger network</span> <span dir="rtl">و</span> <span dir="ltr">Adam</span> <span dir="rtl">استفاده میکنیم</span>
- <span dir="rtl">برای فیت شدن بهتر</span> <span dir="ltr">dev set</span> <span dir="rtl">از</span> <span dir="ltr">Regularization</span> <span dir="rtl">و</span> <span dir="ltr">bigger treating set</span> <span dir="rtl">استفاده میکنیم</span>
- <span dir="rtl">برای فیت شدن بهتر</span> <span dir="ltr">test set</span> <span dir="rtl">از</span> <span dir="ltr">bigger dev set</span> <span dir="rtl">استفاده میکنیم</span>
- <span dir="rtl">برای اجرای خوب روی دیتا های واقعی از</span> <span dir="ltr">change dev set</span> <span dir="rtl">یا</span> <span dir="ltr">change cost function</span> <span dir="rtl">استفاده میکنیم</span>

# Collaborative Filtering [Unsup]

## Description

<img src="image3.jpg" style="width:4.60985in" />

- <span dir="rtl">این الگوریتم دقیقا مشابه با</span> <span dir="ltr">Simple Recommendation</span> <span dir="rtl">هستش با این تفاوت که اینجا مقادیر</span> <span dir="ltr">x</span> <span dir="rtl">رو نداریم.</span>
- <span dir="rtl">این الگوریتم اصلی هستش و الگوریتم</span> <span dir="ltr">Simple Recommendation</span> <span dir="rtl">فقط برای فهم بهتر این الگوریتم مطرح شده</span>
- <span dir="rtl">از اونجایی که اساس این الگوریتم بر فعالیت کاربر تو سامانه هستش، همون ابتدا که کاربر هنوز هیچ فعالیت خاصی نداشته نمیتونه پیشنهادی هم بهش بده</span>
- <span dir="rtl">به طریق مشابه نکته قبل، اگر هنوز هیچ کاربری به یه محصول خاص واکنشی نشون نداده باشه، اون محصول قابلیت ارزیابی برای این الگوریتم نداره</span>

## Formula

<span dir="rtl">کاملا مشابه با</span> <span dir="ltr">Simple Recommendation</span> <span dir="rtl">هستش</span>

## Specific Cost Function (Squared Error Loss)

Formula:

<img src="image4.jpg" style="width:4.47538in" />

<img src="image6.jpg" style="width:5.08069in" />

Gradient Descent:

<img src="image2.jpg" style="width:3.40765in" />

<span dir="rtl">همونطور که تو عکس پیداس، مشابه با</span> <span dir="ltr">Linear Regression</span> <span dir="rtl">هستش با این تفاوت که چون</span> <span dir="ltr">x</span> <span dir="rtl">هم اینجا جزو مجهولاته سه تا فانکشن داریم جای دوتا.</span>

## Binary Classification

<img src="image5.jpg" style="width:2.58944in" />

<img src="image1.jpg" style="width:4.37791in" />

<span dir="rtl">با استفاده از این شیوه خروجی این الگوریتم رو از حالت یک عدد، به حالت</span> <span dir="ltr">boolean</span> <span dir="rtl">تغییر میدیم (در اصل از حالت</span> <span dir="ltr">Linear regression</span> <span dir="rtl">به حالت</span> <span dir="ltr">Logistic regression</span> <span dir="rtl">تغییر میدیمش)</span>

## Finding Related Items

<img src="image7.jpg" style="width:3.8063in" />

<span dir="rtl">بعد از این که مقادیر</span> <span dir="ltr">x</span> <span dir="rtl">برای هر محصول با استفاده از تکنیک های قبلی بدست اومد، به راحتی با چک کردن این</span> <span dir="ltr">x</span> <span dir="rtl">ها و پیدا کردن اون هایی که به هم نزدیک هستن (به وسیله فرمول تو تصویر) میتونیم یه سیستم ریکامندر داشته باشیم که مشابهت سنجی میکنه و پیشنهاد میده</span>

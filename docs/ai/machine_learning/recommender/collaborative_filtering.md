# Collaborative Filtering [Unsup]

## Description

![](collaborative_filtering/image3.jpg)

- <span dir="rtl">این الگوریتم دقیقا مشابه با Simple Recommendation هستش با این تفاوت که اینجا مقادیر x رو نداریم.</span>
- <span dir="rtl">این الگوریتم اصلی هستش و الگوریتم Simple Recommendation فقط برای فهم بهتر این الگوریتم مطرح شده</span>
- <span dir="rtl">از اونجایی که اساس این الگوریتم بر فعالیت کاربر تو سامانه هستش، همون ابتدا که کاربر هنوز هیچ فعالیت خاصی نداشته نمیتونه پیشنهادی هم بهش بده</span>
- <span dir="rtl">به طریق مشابه نکته قبل، اگر هنوز هیچ کاربری به یه محصول خاص واکنشی نشون نداده باشه، اون محصول قابلیت ارزیابی برای این الگوریتم نداره</span>

## Formula

<span dir="rtl">کاملا مشابه با Simple Recommendation هستش</span>

## Specific Cost Function (Squared Error Loss)

Formula:

![](collaborative_filtering/image4.jpg)

![](collaborative_filtering/image6.jpg)

Gradient Descent:

![](collaborative_filtering/image2.jpg)

<span dir="rtl">همونطور که تو عکس پیداس، مشابه با Linear Regression هستش با این تفاوت که چون x هم اینجا جزو مجهولاته سه تا فانکشن داریم جای دوتا.</span>

## Binary Classification

![](collaborative_filtering/image5.jpg)

![](collaborative_filtering/image1.jpg)

<span dir="rtl">با استفاده از این شیوه خروجی این الگوریتم رو از حالت یک عدد، به حالت boolean تغییر میدیم (در اصل از حالت Linear regression به حالت Logistic regression تغییر میدیمش)</span>

## Finding Related Items

![](collaborative_filtering/image7.jpg)

<span dir="rtl">بعد از این که مقادیر x برای هر محصول با استفاده از تکنیک های قبلی بدست اومد، به راحتی با چک کردن این x ها و پیدا کردن اون هایی که به هم نزدیک هستن (به وسیله فرمول تو تصویر) میتونیم یه سیستم ریکامندر داشته باشیم که مشابهت سنجی میکنه و پیشنهاد میده</span>

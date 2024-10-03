# K-Means [Unsup]

## Description

k-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster.

<span dir="rtl">نحوه عملکرد کلیش این مدلیه که دو یا چند</span> <span dir="ltr">centroid</span> <span dir="rtl">اولیه (</span><span dir="ltr">k</span> <span dir="rtl">عدد) رو تو نمودار انتخاب میکنه، فاصله تمامی نقاط موجود رو با تک تک این</span> <span dir="ltr">centroid</span> <span dir="rtl">ها اندازه میگیره و به هر کدوم که نزدیک تر بود به اون اختصاصش میده، حالا میانگین همه اونایی که به یه</span> <span dir="ltr">centroid</span> <span dir="rtl">اختصاص پیدا کردن رو میگیره و اون</span> <span dir="ltr">centroid</span> <span dir="rtl">رو به اون نقطه میانگین جا به جا میکنه، این کارو برای همه</span> <span dir="ltr">centroid</span> <span dir="rtl">ها تکرار میکنه، بعدش با توجه به موقعیت جدید</span> <span dir="ltr">centroid</span> <span dir="rtl">ها، دوباره نقاط رو اختصاص میده و الی آخر، انقدر این کارو تکرار میکنه تا دیگه</span> <span dir="ltr">centroid</span> <span dir="rtl">ها جا به جا نشن.</span>

## Formula

![](k_means/image2.jpg)

- <span dir="rtl">تو تصویر بالا میتونیم الگو ریاضیاتیشو ببینیم</span>
- <span dir="rtl">علامت</span> <span dir="ltr">m</span> <span dir="rtl">هم نشون میده چنتا نقطه داریم</span>
- <span dir="rtl">علامت</span> <span dir="ltr">k</span> <span dir="rtl">نشون دهنده تعداد</span> <span dir="ltr">centroid</span> <span dir="rtl">ها و کلاستر هاست</span>
- <span dir="rtl">علامت</span> <span dir="ltr">n</span> <span dir="rtl">نشون میده هر نقطه چه تعداد فیچر تو خودش داره، مثلا تو تصویر بالا چون نمودار دو بعدیه پس هر نقطه دوتا فیچر داره (</span><span dir="ltr">n</span><span dir="rtl">=2)</span>
- <span dir="rtl">علامت</span> <span dir="ltr">µ</span> <span dir="rtl">مشخصات موقعیت</span> <span dir="ltr">centroid</span> <span dir="rtl">ها هستن</span>
- <span dir="rtl">چون ممکنه این سیستم تو لوکال مینیموم هاش گیر کنه، یعنی یه حالت دسته بندی ای پیش بیاد که تعداد زیادی از نقاط به یه</span> <span dir="ltr">centroid</span> <span dir="rtl">وصلن اما یه تعداد کمی فقط به یه</span> <span dir="ltr">centroid</span> <span dir="rtl">دیگه رسیده، لازمه این الگوریتم رو بین 50 تا 1000 بار اجرا کنیم و آخر سر اونی که</span> <span dir="ltr">cost function</span> <span dir="rtl">با عدد کمتری داشت رو انتخاب کنیم</span>

## Best Number For The K

How should I know which number is the best for the K (number of clusters)?

We will select multiple numbers for it and each time we will check how the variation within each cluster changes.

<img src="image1.jpg" style="width:3.4651in" />

Then by creating the below diagram we can easily find the best point (the best number for K).

<img src="image3.jpg" style="width:3.33326in" />

Importantly, every time we increase the number of K, the variation in each cluster decreases, but it does not mean that we should continue this approach, each time we should check whether the reduction of variation was reasonable or just decreased a little.

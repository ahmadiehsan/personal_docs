# Strategy (Flexible algorithm selection) [Behavioral]

## Description

![](strategy/image1.jpg)

Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

![](strategy/image2.jpg)

!!! info

    - <span dir="rtl">حرف اصلی این پترن استفاده از کامپوزیشن بجای ارث بری هستش</span>
    - <span dir="rtl">به طور مثال بجای ارث برای تولید انواع اردک، بیایم کلاس های مختلفی از رفتار های اردک رو درست کنیم (مثلا نوع صدا، این که پرواز میکنه یا نه، قیافه اردک و …) و کامبینیشن های مختلف از این رفتارهارو کنار هم بذاریم و اردک های مختلف درست کنیم</span>
    - <span dir="rtl">حتی فراتر از این، اگر قبلا برای هر مدل ادک یه کلاس جدا داشتیم، با این روش میتونیم کلا اون کلاس هارو پاک کنیم و فقط یه کلاس داشته باشیم که این کابینیشن های مختلف رو قبول میکنه</span>

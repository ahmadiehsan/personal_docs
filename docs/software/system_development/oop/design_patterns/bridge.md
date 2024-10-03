# Bridge (Decoupled abstraction) [Structural]

## Description

![](bridge/image2.jpg)

Decouple an abstraction from its implementation so that the two can vary independently.

![](bridge/image1.jpg)

<span dir="rtl">حاشیه ها:</span>

- <span dir="rtl">خیلی شبیه به دیزاین پترن استراتژی هستش، با این تفاوت که استراتژی جزو بیهیورال</span><span dir="ltr"></span> <span dir="rtl">پترن هاست اما بریدج</span><span dir="ltr"></span> <span dir="rtl">جزو استراکچرال پترن هاست، به بیان دیگه</span><span dir="ltr"></span> <span dir="rtl">از این پترن برای کم کردن تعداد کلاس های سیستم استفاده میشه.</span>
- <span dir="rtl">مثلا اگر در یک پروژه، یو آی صفحات به صورت زیر هستند</span>

   - <span dir="rtl">آیتم طولانی کتاب و آیتم کوتاه کتاب</span>
   - <span dir="rtl">آیتم طولانی مجله و آیتم کوتاه مجله</span>
   - <span dir="rtl">آیتم طولانی نویسنده و آیتم کوتاه نویسنده</span>
   - <span dir="rtl">آیتم طولانی خواننده و آیتم کوتاه خواننده</span>

- <span dir="rtl">می توانیم آنها را به دو دسته زیر تقسیم کنم:</span>

   - <span dir="rtl">آیتم: طولانی و کوتاه</span>
   - <span dir="rtl">منابع: کتاب، مجله، نویسنده، خواننده</span>

- <span dir="rtl">با این کار تعداد کلاس های پروژه از ۸ به ۶ کاهش پیدا میکنه (در تعداد بالاتر بیشتر خودشو نشون میده) و به راحتی در زمان ران تایم کامبینیشن های مختلف از این کلاس هارو میتونیم ترکیب کنیم و صفحات دلخواهمون رو تشکیل بدیم.</span>

# Data Distribution

## Description

<span dir="rtl">بعضی اوقات، دیتایی اولیه ای که داریم تماما دیتای واقعی نیست، مثلا توی سیستم تشخیص گربه برای آموزش شبکه عصبی کل تصویر با کیفیت تو فضای نت هست اما سیستم ما بناس روی عکس های بی کیفیتی که کاربرها با گوشیشون میگیرن درست کار کنه.</span>

<span dir="rtl">توی این شرایط اگر از دیتای فضای واقعی 10000 نمونه وجود داشته باشه و از دیتای فضای غیر واقعی 500000 نمونه، لازمه به شکل منطقی ای این اعداد بین سه دسته</span> <span dir="ltr">training</span> <span dir="rtl">و</span> <span dir="ltr">dev</span> <span dir="rtl">و</span> <span dir="ltr">test</span> <span dir="rtl">تقسیم بشن، که در زیر میبینیم چطور باید این کارو بکنیم:</span>

- <span dir="rtl">از اونجایی که قراره سیستم ما روی دیتای فضای واقعی کار کنه پس کل دسته</span> <span dir="ltr">dev</span> <span dir="rtl">و</span> <span dir="ltr">test</span> <span dir="rtl">رو از 10000 نمونه بر میداریم</span>
- <span dir="rtl">از اونجایی هم که بالاخره شبکه عصبی ما از دسته</span> <span dir="ltr">training</span> <span dir="rtl">آموزش میبینه لازمه این دسته رو از ترکیب 10000 و 500000 نمونه تشکیل بدیم</span>
- <span dir="rtl">حالا که نحوه تقسیم بندی رو متوجه شدیم، دقیق میتونیم بگیم که هر دسته شامل چند نمونه باشه</span>

   - <span dir="rtl">دسته</span> <span dir="ltr">training</span><span dir="rtl">: شامل 505000 نمونه که ترکیب دیتای فضای واقعی و غیرواقعی هست</span>
   - <span dir="rtl">دسته</span> <span dir="ltr">dev</span><span dir="rtl">: شامل 2500 نمونه از دیتای فضای واقعی</span>
   - <span dir="rtl">دسته</span> <span dir="ltr">test</span><span dir="rtl">: شامل 2500 نمونه از دیتای فضای واقعی</span>

<span dir="rtl">حالا با اعمال شرایط بالا ممکنه یک مشکل جدیدی پیش بیاد، تا قبل از این که دیتا های ما از یک فضا بودن اگر</span> <span dir="ltr">error</span> <span dir="rtl">بین</span> <span dir="ltr">trading</span> <span dir="rtl">و</span> <span dir="ltr">dev</span> <span dir="rtl">زیاد میشد میگفتیم</span> <span dir="ltr">Regularization</span> <span dir="rtl">و</span> <span dir="ltr">bigger treating set</span> <span dir="rtl">رو استفاده کن، ولی حالا با اطمینان نمیشه همچین چیزی گفت، چون ممکنه این تفاوت</span> <span dir="ltr">error</span> <span dir="rtl">بخاطر متفاوت بودن فضا های دیتا باشه (واقعی و غیر واقعی)، پس تو این شرایط لازمه یه دسته دیتای جدیدی رو معرفی کنیم به اسم</span> <span dir="ltr">treating-dev set</span> <span dir="rtl">نحوه عملکردشم این مدلیه که یه بخش کوچیکی از</span> <span dir="ltr">treating set</span> <span dir="rtl">رو جدا میکنیم و اسمشو میذاریم</span> <span dir="ltr">treating-dev set</span> <span dir="rtl">و از این دسته برای آموزش شبکه عصبی استفاده نمیکنیم، بعدی میایم</span> <span dir="ltr">error</span> <span dir="rtl">هارو اندازه میگیریم و بسته به</span> <span dir="ltr">error</span> <span dir="rtl">ها طبق تکنیک</span> <span dir="ltr">Orthogonalization</span> <span dir="rtl">برای حل مشکل عمل میکنیم.</span>

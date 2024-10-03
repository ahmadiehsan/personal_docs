# 一Share (Information Gain Technique) [Tree]

## Description

![](share/image1.png)

- <span dir="rtl">از این فرمول برای انتخاب ترتیب شکستن شاخه ها استفاده میشه</span>
- <span dir="rtl">هر چقدر یک ویژگی (</span><span dir="ltr">feature</span> <span dir="rtl">یا</span> <span dir="ltr">input</span><span dir="rtl">) به ما</span> <span dir="ltr">entropy</span> <span dir="rtl">بهتری بده (نزدیکتر به ۰) به این معنیه که اول بر اساس اون ویژگی بشکنیم بعدش بریم سراغ ویژگی های بعدی</span>

![](share/image4.png)

<span dir="rtl">تو تصویر بالا جایی که هیچکدوم از حیوون ها گربه نیستن فرمول به ما ۰ داده و همینطور جایی که همه شون گربه هستن هم ۰ داده (فرقی نداره که همه باشن یا هیچکدوم نباشن، همین که</span> <span dir="ltr">purity</span> <span dir="rtl">رعایت بشه کافیه)</span>

![](share/image2.png)

<span dir="rtl">حالا وقتی میخوایم از فرمول</span> <span dir="ltr">entropy</span> <span dir="rtl">برای</span> <span dir="ltr">decision trees</span> <span dir="rtl">استفاده کنیم، باید</span> <span dir="ltr">entropy</span> <span dir="rtl">هر طرف رو حساب کنیم، میانگینش رو بدست بیاریم (میانگین بر اساس تعداد دیتاهای هر سمت) و آخرسر نتیجه رو از</span> <span dir="ltr">entropy</span> <span dir="rtl">اولیه دیتا ست کم کنیم، به این فرمول میگن فرمول</span> <span dir="ltr">information gain</span> <span dir="rtl">که هرچقدر حاصل فرمول</span> <span dir="ltr">information gain</span> <span dir="rtl">بیشتر باشه یعنی گزینه بهتریه. (تو تصویر چون</span> <span dir="ltr">information gain</span> <span dir="rtl">سمت چپی بیشتره پس بر اساس اون دیتا مون رو میشکنیم)</span>

<span dir="rtl">برای فیچر هایی که یک مقدار ثابت ندارن (مثلا وزن) با استفاده از تکنیک تصویر زیر اون هارو به حالت</span> <span dir="ltr">True</span> <span dir="rtl">و</span> <span dir="ltr">False</span> <span dir="rtl">ای تغییر میدیم:</span>

![](share/image5.png)

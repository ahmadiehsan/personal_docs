# Reinforcement Learning [Unsup]

## Description

<img src="image6.jpg" style="width:4.36728in" />

<span dir="rtl">تو این مدل از یادگیری چیزی تحت عنوان دیتای اولیه نداریم، در اصل یک سری شرایط تعریف میکنیم به اضافه فانکشن تصمیم گیری برای</span> <span dir="ltr">reward</span> <span dir="rtl">و بسته به حرکت به اون حرکت نمره میدیم.</span>

- <span dir="rtl">تعریف</span> <span dir="ltr">state</span><span dir="rtl">: تمامی حالت هایی که ممکنه رخ بده</span>
- <span dir="rtl">تعریف</span> <span dir="ltr">action</span><span dir="rtl">: تمامی تصمیماتی که میشه گرفت</span>
- <span dir="rtl">تعریف</span> <span dir="ltr">rewards</span><span dir="rtl">: تمامی امتیازاتی که به یه حرکت میتونه تعلق بگیره</span>
- <span dir="rtl">تعریف</span> <span dir="ltr">discount factory</span><span dir="rtl">: ضریبی که حتما کمتر از 1 هستش (البته نه خیلی زیاد، در حد یک دهم یا یک صدم)، این ضریب با قرار گرفتن کنار</span> <span dir="ltr">reward</span> <span dir="rtl">یه جورایی نقش زمان رو بازی میکنه، چون کمتر از یک هستش باعث میشه</span> <span dir="ltr">reward</span> <span dir="rtl">اون</span> <span dir="ltr">action</span> <span dir="rtl">کمتر بشه، یعنی هر چقدر دیرتر اون</span> <span dir="ltr">action</span> <span dir="rtl">خوب انجام بشه، از اونجایی که مرتب این عدد به توان میرسه، هی بیشتر و بیشتر</span> <span dir="ltr">reward</span> <span dir="rtl">اون</span> <span dir="ltr">action</span> <span dir="rtl">خوب رو کم میکنه</span>
- <span dir="rtl">تعریف</span> <span dir="ltr">return</span><span dir="rtl">: فرمول محاسبه امتیاز</span> <span dir="ltr">action</span><span dir="rtl">، در اصل</span> <span dir="ltr">discount factory</span> <span dir="rtl">تو این فرمول یکی یکی توانش زیاد میشه</span>
- <span dir="rtl">تعریف</span> <span dir="ltr">policy</span><span dir="rtl">: ترجیح ما بر ارجحیت دادن کدام</span> <span dir="ltr">action</span>

## Formula (Bellman Equation)

<img src="image4.jpg" style="width:4.74433in" />

<img src="image2.jpg" style="width:3.49009in" />

- <span dir="rtl">با استفاده از این معادله</span> <span dir="ltr">reward</span> <span dir="rtl">حاصل از حرکت از یک</span> <span dir="ltr">state</span> <span dir="rtl">به یک</span> <span dir="ltr">state</span> <span dir="rtl">دیگه با استفاده از</span> <span dir="ltr">action</span> <span dir="rtl">خاص رو میشه محاسبه کرد.</span>
- <span dir="rtl">به بیان دیگه</span> <span dir="ltr">reward</span> <span dir="rtl">بر اساس این معادله به هر</span> <span dir="ltr">action</span> <span dir="rtl">اختصاص پیدا میکنه.</span>
- <span dir="rtl">چون تو این معادله، محاسبه</span> <span dir="ltr">reward</span> <span dir="rtl">هر</span> <span dir="ltr">action</span> <span dir="rtl">نیازمند داشتن</span> <span dir="ltr">reward</span> <span dir="rtl">حرکت های بعدیه، یه جورایی میشه بهش به شکل فانکشن</span> <span dir="ltr">recursive</span> <span dir="rtl">نگاه کرد.</span>

<img src="image3.jpg" style="width:3.65424in" />

## Random (Stochastic) Environment

<img src="image5.jpg" style="width:3.53724in" />

<span dir="rtl">بعضی اوقات سیستم اون مدلی که ما میخوایم عمل نمیکنه و ممکنه به هر علتی ربات تصمیم گرفته بره سمت چپ ولی پاش سر میخوره و میره سمت راست، حالا اتفاقای که میفته ممکنه کلا عوض بشه، مثلا ممکنه میخواسته به سمت 100 بره ولی کلا مسیر عوض بشه بره سمت 40 یا نه همون سمت 100 بره ولی با چند مرحله بیشتر از حالت عادی، تو این حالت برای محاسبه مقدار</span> <span dir="ltr">return</span> <span dir="rtl">از یک حالت استفاده نمیکینم، بلکه میانگین تمامی حالاتش رو حساب میکینم.</span>

<img src="image1.jpg" style="width:3.8631in" />

<span dir="rtl">تو تصویر بالا حالت بروز شده فرمول</span> <span dir="ltr">Bellman Equation</span> <span dir="rtl">رو با در نظر گرفتن حالت میانگین میبینیم.</span>

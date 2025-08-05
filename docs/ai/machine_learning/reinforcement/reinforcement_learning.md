# Reinforcement Learning {Unsup}

## Description

<img src="image6.jpg" style="width:4.36728in" />

<span dir="rtl">تو این مدل از یادگیری چیزی تحت عنوان دیتای اولیه نداریم، در اصل یک سری شرایط تعریف میکنیم به اضافه فانکشن تصمیم گیری برای reward و بسته به حرکت به اون حرکت نمره میدیم.</span>

- <span dir="rtl">تعریف state: تمامی حالت هایی که ممکنه رخ بده</span>
- <span dir="rtl">تعریف action: تمامی تصمیماتی که میشه گرفت</span>
- <span dir="rtl">تعریف rewards: تمامی امتیازاتی که به یه حرکت میتونه تعلق بگیره</span>
- <span dir="rtl">تعریف discount factory: ضریبی که حتما کمتر از 1 هستش (البته نه خیلی زیاد، در حد یک دهم یا یک صدم)، این ضریب با قرار گرفتن کنار reward یه جورایی نقش زمان رو بازی میکنه، چون کمتر از یک هستش باعث میشه reward اون action کمتر بشه، یعنی هر چقدر دیرتر اون action خوب انجام بشه، از اونجایی که مرتب این عدد به توان میرسه، هی بیشتر و بیشتر reward اون action خوب رو کم میکنه</span>
- <span dir="rtl">تعریف return: فرمول محاسبه امتیاز action، در اصل discount factory تو این فرمول یکی یکی توانش زیاد میشه</span>
- <span dir="rtl">تعریف policy: ترجیح ما بر ارجحیت دادن کدام action</span>

## Formula (Bellman Equation)

<img src="image4.jpg" style="width:4.74433in" />

<img src="image2.jpg" style="width:3.49009in" />

- <span dir="rtl">با استفاده از این معادله reward حاصل از حرکت از یک state به یک state دیگه با استفاده از action خاص رو میشه محاسبه کرد.</span>
- <span dir="rtl">به بیان دیگه reward بر اساس این معادله به هر action اختصاص پیدا میکنه.</span>
- <span dir="rtl">چون تو این معادله، محاسبه reward هر action نیازمند داشتن reward حرکت های بعدیه، یه جورایی میشه بهش به شکل فانکشن recursive نگاه کرد.</span>

<img src="image3.jpg" style="width:3.65424in" />

## Random (Stochastic) Environment

<img src="image5.jpg" style="width:3.53724in" />

<span dir="rtl">بعضی اوقات سیستم اون مدلی که ما میخوایم عمل نمیکنه و ممکنه به هر علتی ربات تصمیم گرفته بره سمت چپ ولی پاش سر میخوره و میره سمت راست، حالا اتفاقای که میفته ممکنه کلا عوض بشه، مثلا ممکنه میخواسته به سمت 100 بره ولی کلا مسیر عوض بشه بره سمت 40 یا نه همون سمت 100 بره ولی با چند مرحله بیشتر از حالت عادی، تو این حالت برای محاسبه مقدار return از یک حالت استفاده نمیکینم، بلکه میانگین تمامی حالاتش رو حساب میکینم.</span>

<img src="image1.jpg" style="width:3.8631in" />

<span dir="rtl">تو تصویر بالا حالت بروز شده فرمول Bellman Equation رو با در نظر گرفتن حالت میانگین میبینیم.</span>

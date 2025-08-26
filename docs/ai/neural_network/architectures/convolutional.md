# Convolutional (CNN) [Image]

## Description

A convolutional neural network (CNN) is a regularized type of feed-forward neural network that learns feature engineering by itself via filter (or kernel) optimization.

![](convolutional/image12.jpg)

- <span dir="rtl">به شبکه عصبی ای که لایه هاش با تمام دیتای مرحله قبلی کاری نداشته باشن و فقط با یک بخشی ازش کار کنن گفته میشه</span>
- <span dir="rtl">تو این الگو لایه ها اصطلاحا fully-connected نیستن، یعنی هر unite به تمامی unite های لایه بعدی متصل نیست</span>

A CNN is particularly well-suited to tasks involving spatial data, such as images.
Its architecture includes three main types of layers: convolutional layers, pooling layers, and fully connected layers.
The convolutional layers apply a series of filters to the input, which allows the network to automatically and adaptively learn spatial hierarchies of features.

Pooling layers decrease the spatial size of the representation, thereby reducing parameters and computation in the network to control overfitting and decrease the computation cost in the following layers.
Fully connected layers get the output of the pooling layer and conduct high-level reasoning on the output.

<img src="image3.png" style="width:5.30072in" />

## Description in Details

<span dir="rtl">تو این مدل شبکه عصبی با computer vision کار داریم و بناس با ماتریس های مربوط به تصاویر رنگی و سیاه سفید کار کنیم.</span>

<span dir="rtl">از اونجایی که تصاویر خیلی دیتا دارن و عملا امکان پذیر نیست همه unite ها به تمامی دیتای عکس دسترسی داشته باشن، از CNN برای train کردن استفاده میشه، مثلا تو تصویر زیر عددی که دایره سبز دورش هست فقط و فقط به وسیله اعداد داخل مربع سبز رنگ مشخص شده و هیچ کار دیگه ای با باقی پیکسل ها نداشته، همینطور عدد مشخص شده با دایره قرمز</span>

<img src="image1.jpg" style="width:5.45492in" />

<span dir="rtl">برای کار با عکس، شبکه عصبی باید حداقل شامل مراحل زیر باشه:</span>

<img src="image11.jpg" style="width:1.31136in" />

- <span dir="rtl">مرحله Convolution: تصویر اولیه به عنوان یه ماتریس به شبکه عصبی داده میشه با اعمال یک یا ده ها فیلتر یه ماتریس output ساخته میشه</span>
- <span dir="rtl">مرحله Polling: این مرحله هم مثل مرحله قبله ولی با این تفاوت که عملکرد فیلتر هاش متفاوته</span>
- <span dir="rtl">مرحله Fully connected: تو این مرحله سیستم از حالت Convolutional خارج میشه و لایه ها با هم fully connected میشن</span>

![](convolutional/image6.jpg)

## Convolution Step

<img src="image8.jpg" style="width:4.91526in" />

<span dir="rtl">توی تصویر بالا یه عکس 6 در 6 پیکسلی به دو فیلتر 3 در 3 داده شده و بعد از اعمال activation function روی پاسخ این تصویر 6 پیکسلی ما به تصویر 4 پیکسلی تغییر اندازه داده.</span>

<span dir="rtl">فرمول محاسبه اندازه نهایی تصویر بر اساس سایز اولیه تصویر و سایز فیلتر ها و … به شکل زیره:</span>

<img src="image4.jpg" style="width:3.25909in" />

<span dir="rtl">تمامی پارامترهایی که یک لایه شبکه عصبی CNN ممکنه باهاش سروکار داشته باشه تو تصویر زیر اومده:</span>

![](convolutional/image2.jpg)

- <span dir="rtl">پارامتر f: اندازه فیلتر رو مشخص میکنه، فیلتر ها همیشه اعداد مفرد هستن و معمولا هم 3 در 3 هستن</span>
- <span dir="rtl">پارامتر p: برای این که توی فرایند اعمال فیلترها روی تصویر، تصویر ما کوچیکتر نشه میتونیم قبل از دادن تصویر به فیلتر با استفاده از padding به اطراف تصویر فضا اضافه کنیم</span>
- <span dir="rtl">پارامتر s: گام های حرکت فیلتر روی تصویر رو مشخص میکنه، هرچقدر گام ها بلند تر، تصویر خروجی کوچیکتر</span>
- <span dir="rtl">پارامتر nc: تعداد فیلترهایی که میخوایم روی یک تصویر اعمال کنیم رو مشخص میکنه</span>

## Polling Step

<span dir="rtl">تو این مرحله، نتایج حاصل از مرحله Convolution را به یه فیلتر دیگر میدیم تا از هر چند پیکسل فقط یه پیکسل رو انتخاب کنه.</span>

<img src="image9.jpg" style="width:2.07541in" />

- <span dir="rtl">پارامترهای این فیلتر f و s هستن که بالاتر بهش اشاره شد.</span>
- <span dir="rtl">توی شبکه عصبی CNN برای پارامتر های s و f تو این لایه اعداد ثابتی در نظر میگیرن و توی فرایند train این اعداد عوض نمیشن</span>

Max polling:

<img src="image7.jpg" style="width:3.49604in" />

<span dir="rtl">محبوب ترین شیوه polling همین شیوه هستش که با حرکت بر اساس f و s تو هر رسید مربع بزرگترین پیکسل رو انتخاب میکنه</span>

<img src="image5.jpg" style="width:3.98601in" />

<span dir="rtl">این فیلتر میتونه چند بعدی هم باشه</span>

Average polling:

<img src="image10.jpg" style="width:3.55729in" />

<span dir="rtl">این شیوه هم دقیقا مثل max polling هستش با این تفاوت که میانگین پیکسل ها در نظر گرفته میشه و مثل max polling هم کاربردی نیست.</span>

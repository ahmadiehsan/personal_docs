# Batch & Mini-batch

## Description

<span dir="rtl">زمانی که تعداد دیتا هامون (</span><span dir="ltr">m</span><span dir="rtl">) خیلی زیاده بجای این که هر بار برای محاسبه</span> <span dir="ltr">j</span> <span dir="rtl">از کل دیتا های استفاده کنیم، میایم دیتا هارو به بخش های کوچکتر (</span><span dir="ltr">mini-batch</span><span dir="rtl">) تقسیم میکنیم و هر بار</span> <span dir="ltr">j</span> <span dir="rtl">رو بر اساس یکی از این بخش های کوچیک حساب میکنیم.</span>

<img src="image1.jpg" style="width:5.13819in" />

<span dir="rtl">همینطور تو تصویر بالا میتونیم تاثیر این تغییر در نمودار</span> <span dir="ltr">j</span> <span dir="rtl">رو ببینیم، از اونجایی که تصمیم درباره مقدار بعدی</span> <span dir="ltr">w</span> <span dir="rtl">و</span> <span dir="ltr">b</span> <span dir="rtl">رو هر بار بر اساس یک تکه ای از دیتا (یعنی یک</span> <span dir="ltr">mini-batch</span><span dir="rtl">) میگیریم، ممکنه در بعضی از مواقع نمودار</span> <span dir="ltr">j</span> <span dir="rtl">همواره نزولی نباشد، اما در کل نزولی خواهد بود.</span>

<img src="image5.jpg" style="width:4.86642in" />

<span dir="rtl">تو تصویر بالا</span> <span dir="ltr">X</span> <span dir="rtl">که ماتریکسی از تمامی دیتاهای (</span><span dir="ltr">m</span><span dir="rtl">) ما هست رو به ماتریس های کوچکتر 1000 تایی شکستیم و هر کدوم از این</span> <span dir="ltr">mini-batch</span> <span dir="rtl">های 1000 تایی رو با نماد {</span><span dir="ltr">i</span><span dir="rtl">} نشون میدیم.</span>

<img src="image2.jpg" style="width:5.98803in" />

<span dir="rtl">تو تصویر بالا:</span>

- <span dir="rtl">رنگ آبی به این اشاره داره که ما سایز های</span> <span dir="ltr">mini-batch</span> <span dir="rtl">هامون رو هم اندازه</span> <span dir="ltr">m</span> <span dir="rtl">بگیریم که در این صورت یک</span> <span dir="ltr">mini-batch</span> <span dir="rtl">بیشتر نخواهیم داشت که بهش در اصل</span> <span dir="ltr">Batch</span> <span dir="rtl">میگیم و خیلی سریعتر و دقیق تر به گلوبال مینیمم میرسه ولی یادمون نره که کلا هدف از استفاده ی</span> <span dir="ltr">mini-batch</span> <span dir="rtl">برای دیتا های خیلی زیاد هستش که عملا تو رم کامپیوتر جا نمیشن یا محاسباتشون خیلی طولانی میشه.</span>
- <span dir="rtl">رنگ بنفش به این اشاره داره که ما سایز های</span> <span dir="ltr">mini-batch</span> <span dir="rtl">هامون رو هم اندازه 1 بگیریم که در این صورت هر دونه از دیتا های ما در اصل یه</span> <span dir="ltr">mini-batch</span> <span dir="rtl">خواهد شد که در اصل بهش</span> <span dir="ltr">Stochastic</span> <span dir="rtl">و اصلا بهینه نیستش و عملا هیچوقت به گلوبال مینیمم نمیرسه، یه نکته دیگه که اینجا مهمه اینه که با این ویژگی جون به ازای هر دونه از دیتا هامون داریم</span> <span dir="ltr">j</span> <span dir="rtl">رو حساب میکنیم عملا نمیتونیم از خاصیت وکتوریزیشن استفاده کنیم و باید حلقه دستی بنویسیم.</span>
- <span dir="rtl">رنگ سبز به این اشاره داره که ما سایز های</span> <span dir="ltr">mini-batch</span> <span dir="rtl">هامون رو یه چیزی بین 1 و</span> <span dir="ltr">m</span> <span dir="rtl">بگیریم که در این صورت به هدفمون خواهیم رسید.</span>

<img src="image3.jpg" style="width:4.24463in" />

<span dir="rtl">تو تصویر بالا هم میبینیم که:</span>

- <span dir="rtl">برای دیتا های زیر 2000 تا اصلا نیازی به استفاده از</span> <span dir="ltr">mini-batch</span> <span dir="rtl">نیست و خیلی راحت با همون تکنیک</span> <span dir="ltr">batch</span> <span dir="rtl">سریع و دقیق به هدفمون میرسیم.</span>
- <span dir="rtl">معمولا تعداد دیتا های داخل هر</span> <span dir="ltr">mini-batch</span> <span dir="rtl">رو مضربی از 2 قرار میدن</span>
- <span dir="rtl">برای انتخاب تعداد دیتا های داخل هر</span> <span dir="ltr">mini-batch</span> <span dir="rtl">حتما باید به منابع کامپیوتر توجه کنیم.</span>

The batch size can significantly impact the learning process. Larger batch sizes result in faster progress in training but don’t always converge as fast. Smaller batch sizes update the model frequently but the progress in training is slower.

Moreover, smaller batch sizes have a regularizing effect and can help the model generalize better, leading to better performance on unseen data. However, using a batch size that is too small can lead to unstable training, less accurate estimates of the gradient, and, ultimately, a model with worse performance.

## Stochastic Gradient Descent (SGD)

Uses a single example at each iteration of the optimizer. Therefore, the batch size for SGD is 1

<img src="image4.jpg" style="width:5.84521in" />

<span dir="rtl">تو تصویر بالا دو مفهوم</span> <span dir="ltr">Batch</span> <span dir="rtl">و</span> <span dir="ltr">Stochastic</span> <span dir="rtl">رو که تو عناوین قبلی اشاره شد میبینیم.</span>

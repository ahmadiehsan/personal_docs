# Oauth [Authentication]

<script>
document.querySelector('.md-content').setAttribute('dir', 'rtl');
document.querySelector('.md-sidebar--secondary').setAttribute('dir', 'rtl');
</script>

## عملکرد

<img src="oauth2.jpg" style="width:688px" />

## لینک های مهم

فیلم یوتیوب برای فهم مفاهیم و دوری از تعاریف غلط (پیشنهاد میشود حتما دیده شود): [مشاهده فیلم](https://www.youtube.com/watch?v=996OiexHze0) فیلم های یوتیوب آموزشی به صورت گرافیکی:  [مشاهده فیلم اول](https://www.youtube.com/watch?v=CPbvxxslDTU) و [مشاهده فیلم دوم](https://www.youtube.com/watch?v=LyqeHAkxVyk)

## جریان و اصطلاحات اصلی Oauth 2.0

(OAuth 2.0 flow and terminology)

کیج کنندگی و ابهامات زیادی درباره oauth وجود دارد که علت آن توضیحات اشتباه و تعاریف نادرست در مورد اصطلاحات و کلمات این حوزه است

<img src="slide_1.jpg" style="width:688px" >

شناسایی و هویت موارد استفاده oauth:

قبل از سال 2007 (که oauth وجود نداشت) single login با استفاده از فرم ها و کوکی ها و single sign-on یا همان sso به وسیله تکنولوژی SAML که بر مبنای xml هست انجام می شد (در این زمان موبایل های هوشمند وجود نداشتند و ..‌)

<img src="slide_2.jpg" style="width:688px" >

حال به سوال زیر دقت کنید:

دسترسی دادن به یک سرویس یا ... برای استفاده از بخشی از اطلاعات ما در یک سرویس دیگر به جز از راه دادن پسورد خودمان به سرویس ثالث ممکن نبود.

<img src="slide_3.jpg" style="width:688px" >

مانند شکل زیر که یک سایت هم ایمیل و هم پسورد ایمیل شما را می گرفت تا بتواند شما را با دیگر دوستانی از خودتان که از همین سرویس استفاده می کنند را پیدا کند و با شما مرتبط سازد ( که این بدترین راه ممکن بود چرا که اصلی ترین قسمت امنیت شما را که پسوردتان هست از شما می گرفت )

مثال 1(سایت یلپ)  :

<img src="slide_4.jpg" style="width:688px" >

مثال 2  (سایت فیسبوک) :

<img src="slide_5.jpg" style="width:688px" >

تفویض مجوز با oauth 2 :

یعنی من هم به gmail اعتماد دارم و هم در مورد دادن دسترسی به سرویس yelp برای contact های داخل gmail ام.

<img src="slide_6.jpg" style="width:688px" >

تفویض مجوز (دسترسی کنترل شده دادن به یک سرویس ثالث) با استفاده از oauth 2.0 به صورت زیر اتفاق می افتد:

(با مثال توضیح می دهیم)

<img src="slide_7.jpg" style="width:688px" >

اصطلاحات مهم استفاده شده در Oauth 2.0 :

<img src="slide_8.jpg" style="width:688px" >

resource owner: به مالک یکسری اطلاعات روی یک سرور (منظور کاربر است) می گویند.

resource server: به سرور مالک اطلاعاتی که سرویس ثالث به اطلاعات آن در مورد کاربر نیاز دارد می گویند.

client: به سرویسی ثالثی ای (نه صرفا همیشه ثالث) که درخواست دسترسی به اطلاعات کاربر را دارد می گویند.

authorization server: به سروری که به احراز هویت کاربر می پردازد و برای استفاده سرویس ثالث، یک token مرتبط با همین کاربر تولید می کند می گویند

authorization grant: به نوع درخواستی که سرویس ثالث برای ساخت مدل دسترسی (توکن یا ای دی یا ...) به سرور اطلاعات دارد می گویند.

access token: به توکن صادر شده توسط authorization server برای resource owner جهت استفاده سرویس client می گویند.

- در اینجا یک مفهوم دیگری وجود دارد که بدین معنی است که شما باید در درخواستی که جهت گرفتن دسترسی به اطلاعات کاربر به authorization server می زنید یک parameter  به نام redirect url در کنار دیگر اطلاعات ارسال کنید تا این url با url ای که قبلا خودتان برای این کلاینت در سرویس authorization server ثبت کردید چک شود و اگر یکی بودن آنگاه به آن ادرس بعد گرفتن response ریدایرکت انجام شود.
- ما قبل از شروع ایجاد درخواست برای فرایند oauth باید اطلاعات کلاینت خودمان را در authorization server ثبت کرده باشیم و یک client id و client secet دریافت کرده باشیم.

در شکل زیر به طور کامل می بینید که یک فرایند oauth به چه صورت انجام می شود:

<img src="slide_9.jpg" style="width:688px" >

2 اصطلاح مهم دیگر داخل Oauth 2.0 :

<img src="slide_10.jpg" style="width:688px" >

scope : برای تعیین سطح و نوع دسترسی به اطلاعات استفاده می شود.

مثلا دسترسی خواندن ایمیل ها == >>  scope = read emails

گاهی مشاهده شده که بدیم صورت نیز استفاده می شود == >>  scope = emalis.read

consent : به سازنده صفحه نشان داده شده به کاربر برای تایید دسترسی های خواسته شده توسط سرویس ثالث گفته می شود.

<img src="slide_11.jpg" style="width:688px" >

2 مفهوم بسیار مهم در oauth وجود دارد:

<img src="slide_12.jpg" style="width:688px" >

این مفهوم ها از امنیت شبکه ها وارد oauth شده است

back channel : به ارتباط بین ۲ سرور (سرورهای  backend) بدون دخالت یا حضور هیچ کلاینت در میانشان ارتباط back-channel می گویند.

front channel : به ارتباطی که یک طرف آن یعنی درخواست دهنده یا پاسخ دهنده کلاینت (منظور browser هست) باشد، ارتباط  front-channel می گویند.

**نکات مهم** :

- امنیت back channel بسیار بالاتر از front channel هست.
- در front channel چون یک طرف ارتباط browser ها هستند و امنیت کمتری نسبت به سرور ها دارند.(چون که ما در مورد کد browser ها اطلاعات زیادی نداریم و خودمان آنها را نساختیم و کلی روزنه داخلشان وجود دارد که میتواند منجر به فاش شدن اطلاعات شود. همچنین با یک inspect element و باز کردن تب console یا network می توان اطلاعات مهمی از browser بیرون کشید)
- در back channel چون سازنده کد خودمان هستیم و تنها راه وارد شدن به سرور دست خودمان هست این موضوع باعث بالا رفتن امنیت ارتباط می شود.( فقط خودمان از secret code با خبر هستیم)

<img src="slide_13.jpg" style="width:688px" >

در مثال بالا تمام ارتباطات با فلش های ممتد در front-channel اتفاق افتاده و تمام ارتباطات با فلش های مقطع در back-channel اتفاق افتاده است.

در مثال زیر یک نمونه ریکوئست را می بینید:

<img src="slide_14.jpg" style="width:688px" >

همانطور که ملاحظه کردید تقریبا تمام اطلاعات برای گرفتن access token به صورت parameter در داخل ریکوئست ارسال می شود.

اگر کاربر اجازه دسترسی ندهد response با یک error و اگر اجازه دسترسی بدهد response با یک access token برمی گردد:

<img src="slide_15.jpg" style="width:688px" >

یک فرایند و ارتباطی بین سرور ها انجام خواهد شد به نام exchange code for access token :

**نکته مهم** : علت این موضوع که authorization server در ابتدا یک authorization_code به سمت کلاینت (browser) بر می گرداند و بعد کلاینت(browser)  آن را به سرور بکند خود می فرستد و سپس سرور بکند آن کلاینت، برای گرفتن access token یک ارتباط دیگر با backend authorization server برقرار می کند تا با ارسال authorization_code به authorization server گفته شده access token مورد نیاز خود را بگیرد این هست که؛ ارتباط اول که در آن authorization_code ساخته و ارسال شد میان کلاینت سرور ثالث و سرور احراز هویت برقرار شد (که در front-channel بود) و ارتباط دوم که در آن access token ساخته و ارسال شد میان سرور بکند آن کلاینت و سرور احراز هویت برقرار شد (که در back-channel بود) توجه داشته باشید که عمر authorization_code ساخته و ارسال شده در front-channel بسیار کوتاه است و در حد 3 الی 5 دقیقه قابل استفاده برای گرفتن access token توسط سرور بکند کلاینت ثالث هست.

عکس های زیر فرایند exchange برای دادن authorization_code و گرفتن access token را نمایش می دهد:

<img src="slide_16.jpg" style="width:688px" >

<img src="slide_17.jpg" style="width:688px" >

حال پس از گرفتن access token ارتباط بدین گونه میان client و resource server برقرار می شود: توجه داشته باشید که access token و کلا اطلاعات authorization برای این ارتباط در header ست می شود.

<img src="slide_18.jpg" style="width:688px" >

بجز مدل authorization code مدل های دیگری نیز برای جریان oauth 2.0 وجود دارد.

کل مدل های موجود عبارتند از:

<img src="slide_19.jpg" style="width:688px" >

فرایند یا جریان implicit به صورت زیر رخ می دهد:

<img src="slide_20.jpg" style="width:688px" >

همانطور که مشاهده کردید در implicit تمام ارتباط ها در داخل front-channel رخ میدهد و از امنیت پایین تری نسبت به authorization code دارد. این نوع ارتباط (implicit) مناسب single page application ها هستند که فقط صرفا یک نرم افزار یک صفحه ای نوشته شده با جاوا اسکریپت هستند و سرور بکند جدا از خود ندارند.

در سال 2012 از oauth 2.0 در use case ها (یا موارد استفاده) نا مناسبی استفاده می شد. همانطور که این موارد به صورت قرمز در عکس پایین مشخص شده اند:

<img src="slide_21.jpg" style="width:688px" >

علت این موضوع این بود که oauth 2.0 برای دادن سطح دسترسی به یک سرویس ثالث جهت داشتن دسترسی به اطلاعات یک کاربر به وجود آمده بود ولی جز این موضوع مردم از oauth 2.0 برای authentication نیز استفاده می کردند (البته با یکسری تغییرات) که این موضوع اشتباه بود.

علل اشتباه بودن استفاده از oauth 2.0 برای authentication :

<img src="slide_22.jpg" style="width:688px" >

برای حل این مشکل چیزی به نام open id ساخته شد تا روی پروتکل oauth سوار شود و این مشکل را حل کند:

<img src="slide_23.jpg" style="width:688px" >

مزایای اضافه شدن open id به oauth 2.0:

<img src="slide_24.jpg" style="width:688px" >

فرایند open id authentication به صورت زیر اتفاق می افتد:

<img src="slide_25.jpg" style="width:688px" >

اکثر اطلاعات رد و بدل شده شبیه oauth 2.0 می باشد بجز:

1. scope در اینجا برابر openid profile می باشد
2. در ارتباط exchange جهت گرفتن access token علاوه بر access token d یک ID token نیز از طرف سرور احراز هویت برای سرور کلاینت ثالث ارسال می شود که علت آن، وجود یکسری اطلاعات پایه از کاربر هست تا از آن برای ساخت اکانت کاربر یا ... استفاده کنند و علت ارسال access token نیز این هست که اگر اطلاعات موجود در ID token کافی نبود از access token برای گرفتن اطلاعات دیگر استفاده کند.

جریان open id به صورت ریزتر به شکل زیر اجرا می شود:

<img src="slide_26.jpg" style="width:688px" >

در اینجا ارتباط برای گرفتن ID token و access token برقرار می شود:

<img src="slide_27.jpg" style="width:688px" >

ID token و access token در response به سرور ثالث ارسال می شود:

<img src="slide_28.jpg" style="width:688px" >

ID token می تواند یک jwt token باشد که شامل ۳ جزء می باشد:

<img src="slide_29.jpg" style="width:688px" >

در ادامه درباره jwt token ها توضیح داده می شود.

مهم ترین قسمت ID token جزء دوم یعنی payload آن می باشده که شامل اطلاعات کاربر و ... می باشد:

<img src="slide_30.jpg" style="width:688px" >

اگر اطلاعات موجود در ID token ناکافی بود، می توان مانند زیر یک ریکوئست برای گرفتن اطلاعات بیشتر به user info endpoint زد:

<img src="slide_31.jpg" style="width:688px" >

با وجود آمدن open id مسئله استفاده از oauth 2.0 برای authentication حل شد:

<img src="slide_32.jpg" style="width:688px" >

موارد استفاده از Open ID درمقابل موارد استفاده از OAuth 2.0 :

<img src="slide_33.jpg" style="width:688px" >

در چه مواردی باید از چه grant type ای استفاده کنیم:

<img src="slide_34.jpg" style="width:688px" >

نمونه نحوه استفاده یک web application ای که دارای backend server هست از Open ID Connect :

<img src="slide_35.jpg" style="width:688px" >

نمونه نحوه استفاده یک native mobile app از Open ID Connect :

<img src="slide_36.jpg" style="width:688px" >

نمونه نحوه استفاده یک single page application از Open ID Connect :

<img src="slide_37.jpg" style="width:688px" >

نمونه نحوه استفاده از Open ID Connect در یک SSO یا Single Sign-On :

<img src="slide_38.jpg" style="width:688px" >

راه های راستی آزمایی توکن ها:

(در ادامه به طور کامل توضیح داده خواهد شد)

<img src="slide_39.jpg" style="width:688px" >

راه های ابطال توکن ها:

(در ادامه به طور کامل توضیح داده خواهد شد)

<img src="slide_40.jpg" style="width:688px" >

<img src="slide_41.jpg" style="width:688px" >

## سرور اطلاعاتی

([The Resource Server](https://www.oauth.com/oauth2-servers/the-resource-server/))

resource server در OAuth 2.0 یکی از ملزومات است و به handle کردن درخواست های تایید هویت شده (access token دار) می پردازد.

در پروژه هایی با اسکیل های بزرگ که ما چندیدن سرور اطلاعاتی (resource server) داریم نیاز هست که سرور authentication ما در یک سرور جدا باشد (و توکن ها در آن سرور ساخته شوند) و بقیه ی resource server ها باید برای احراز کردن توکن ها از آن سرور استفاده کنند که این ارتباط از طریق api رخ میدهد اما در پروژه هایی با اسکیل کوچکتر ما فقط یک resource server داریم و کد های authentication در کنار دیگر کدها به عنوان بخشی از این سرور (resource server) هستند و ارتباطشان به صورت داخلی خواهد بود.

### راستی آزمایی توکن های دسترسی

(Verifying Access Tokens)

resource server به دنبال دریافت ریکوئست هایی است به همراه HTTP Authorization header که شامل acces token هست می باشد. resource server نیازمند راستی آزمایی کردن access token هست تا در صورت صحیح بودن اطلاعات و سطح دسترسی تعریف شده در آن دیتای مورد نیاز کاربر یا سرویس را برگرداند.

### راستی آزمایی اسکوپ ها

(Verifying Scope)

resource server نیاز دارد تا از لیست scope های مرتبط با access token مطلع باشد چراکه resource server مسئول ممنوع یا قفل کردن ریکوئست هایی است که scope های موجود در توکن ارسالی توسط آن ریکوئست حاوی scope لازم (دسترسی لازم) برای انجام action خواسته شده توسط همین ریکوئست نباشد. oauth 2.0 هیچ مختصات خاصی برای scope ها تعریف نمیکند و scope های خاص از پیش تعریف شده مرکزی ای وجود ندارد و این خود شمایید ( developer ) که بر اساس نیاز خود و پروژه اتان درباره scope ها تصمیم گیری می کنید.

## چند روش ساخت و راستی آزمایی توکن های دسترسی

(multiple method for create and verify the access token)

1. token introspection
2. self encoded access token
3. database query for access token

یادداشت: هسته OAuth 2.0 هیچ راه بخصوصی را برای چگونگی راستی آزمایی token در داخل resource server تعریف نمی کند و فقط اعلام می کند که یکسری مختصات یا مشخصات بین resource server و authentication server نیاز می باشد همچنین در مواقعی که 2تا endpoint ما یعنی resource server و authentication server مان در یک سرور قرارداشته باشند انتقال اطلاعات از قبیل توکن و ... به صورت داخلی صورت می گیره اما هنگامی که این دو endpoint روی نقطه های یا سرور های مجزایی باشند نیاز هست که انتقال اطلاعات میانشان بر اساس پروتکل های غیر استاندارد صورت گیرد.

### درباره Token Introspection

([token introspection](https://www.oauth.com/oauth2-servers/token-introspection-endpoint/))

- OAuth 2.0 token introspection + تعریف کننده پروتکلی است که برگرداننده اطلاعات یک ، access token در نظر گرفته شده برای استفاده resource server یا دیگر internal server هاست.
- token introspection نیازمنده این هست که بتواند اطلاعات مربوط به یک توکن را برگرداند و برای رسیدن به این هدف راه های محتمل زیادی وجود دارد مثلا شاید بخواهید token introspection را در جایی بسازید که دیگر endpoint ها در آنجا قرار دارند. باید به خاطر داشت که برای برقراری ارتباط میان 2 تا endpoint ما یا نیاز به اشتراک گذاری یک دیتابیس و یا یک secret هست.
- در حقیقت روش token introspection یک نوع استاندارد و بهینه سازی بیشتر هست که در داخلش میتوان از یکی از 2 روش self encoded access token و یا database query for access token استفاده کرد.

#### ریکوئست با اطلاعات توکن

(token information request)

این یک post request هست که شامل یک پارامتر به نام token می باشد و همچنین انتظار می رود که endpoint این request به صورت عمومی قابل دستیابی نباشد و end-user نیز نباید امکان دسترسی به این endpoint را از هیچ طریقی برای service یا شخص دیگری فراهم کند، بنابراین endpoint ما یا باید در یک سرور داخلی قرار گیرد یا باید به وسیله http basic auth محافظت شود.

```http
POST /token_info HTTP/1.1
Host: authorization-server.com
Authorization: Basic Y4NmE4MzFhZGFkNzU2YWRhN

token=c1MGYwNDJiYmYxNDFkZjVkOGI0MSAgLQ
```

#### پاسخ سرور به اطلاعات توکن ارسالی ریکوئست

(token iformation response)

token introspection endpoint باید response را به همراه یک json object را با پراپرتی های زیر برگرداند که فقط پراپرتی `active` اجباری هست. (در مثال زیر بعضی از پراپرتی ها مخصوص jwt می باشد) همچنین میتوانید پراپرتی های بیشتر مورد نیاز خودتان را اضافه کنید.

- **active** : یک boolean هست که:

    - زمانی `true` ارسال می شود که 3  شرط زیر برقرار باشد:

        1. token توسط authorization sever صادر شده باشد.
        2. token توسط کاربر باطل نشده باشد.
        3. token منقضی نشده باشد.

    - زمانی `false` ارسال می شود که هر خطایی بجز authetication error رخ دهد.

- **scope** : یک json string ای می باشد که حاوی لیستی از scope های مرتبط با token است.
- **client_id** : شناسه کلاینت یا client identifier شناسه ای است که token برای آن صادر شده است.
- **user_name** : یک شناسه خوانا برای مشخص کردن شخصی که این توکنبا احراز او ساخته شده است.
- **exp** : یک unix timestamp یا مدت زمان تعریف شده برای منقضی شدن توکن (تعداد ثانیه های مانده تا انقضا)

response example :

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "active": true,
  "scope": "read write email",
  "client_id": "J8NFmU4tJVgDxKaJFmXTWvaHO",
  "username": "aaronpk",
  "exp": 1437275311
}
```

error response :

هنگامی که introspection به صورت عمومی قابل دسترسی باشد، ابتدا باید احراز هویت را راستی آزمایی کند که اگر در این راستی آزمایی به مشکل برخورد کند باید http 401 error برگرداند.

- 401 = invalid_client

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json; charset=utf-8

{
  "error": "invalid_client",
  "error_description": "The client authentication was invalid"
}
```

حال اگر هر خطای دیگر (به جر خطای احراز هویت) رخ دهد response همراه با یک ‍‍`'active': false` برمی گردد.(همراه هر یک از دلایل زیر این پارامتر باید ارسال شود)

- هنگامی که token وجود نداشته باشه یا غلط باشه.
- هنگامی که token منقضی شده باشد.
- هنگامی که token برای یک کلاینت دیگر صادر شده باشد.

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "active": false
}
```

#### ملاحظات امنیتی

(security consideration)

- استفاده از token introspection به این معناست که ، هر resource server ای برای تعیین این که access token ای که ارسال کرده است active هست یا نه میتواند به این endpoint اتکا کند. (مثلا گوگل کلی resource server متفاوت که برخی از آنها در عکس زیر آمده است دارد که برای همه آنها به از endpoint برای راستی آزمایی access token استفاده می کنند)

  <img src="google-apis.png" style="width:688px" />

- introspection endpoint صرفا فقط مسئولیت تصمیم گیری در مورد موفقیت درخواست های API را برعهدا دارد.
- introspection endpoint باید تمام چک های لازم و مناسب را برای access token انجام دهد، اعم از token's state و token's exp و token's signature .

#### عمل فیشینگ توکن ها

(token fishing)

از آنجایی که resource server ها حاوی اطلاعات بخصوص و مهمی از هر کاربر هستند، پتانسیل بالایی برای حملات fishing نیز دارند.

introspection endpoint ای که به صورت عمومی قابل دسترسی باشد یک موقعیت برای هکرها و اتکرها فراهم میکندتا به راحتی به عمل fishing بپردازند برای حل این موضوع یا  سرور باید از یک احراز هویت اجباری برای کلاینت ها ی استفاده کننده از این endpoint استفاده کند و یا این که endpoint ما فقط به صورت داخلی قابل دسترس باشد نه خارجی.

#### درباره کش کردن اطلاعات

(caching)

```json
::Less secure::  ==>>  long cach expitation time  ==>>  mitigate load on endpoint
```

```json
::High secure::  ==>>  shorter cach expitation time  ==>>  more query to introspection endpoint frequently  ==>>  increased load on the endpoint
```

- بهترین راه برای caching این هست که مدت زمان cach ما از exp تایم موجود داخل access token بیشتر نباشد، همچنین میتوانیم از مقدار همین پارامتر access token برای caching time استفاده کنیم.

#### محدود کردن اطلاعات

(limiting information)

introspection endpoint نباید لزوما یک پاسخ یا response یکسان برای همه  کوئری های مربوط به یک access token برگرداند. مثلا ۲ تا resource server مختلف (با فرض این که هر ۲ از طرف endpoint ما احراز هویت شده اند) ممکن است view های مختلفی از state  یک توکن را دریافت کنند که از این موضوع می توان برای محدود کردن اطلاعات برگشته از توکن ارسالی (توسط کلاینت) به چند resource server استفاده کرد.

- این موضوع باعث میشه تا ما توکن هایی داشته باشیم که می توانند توسط چند resource server استفاده شوند بدون اینکه هر کدام بدانند که این توکن توسط endpoint دیگری قابل استفاده است.

### توکن های خود شمول

([self encoded access token](https://www.oauth.com/oauth2-servers/access-tokens/self-encoded-access-tokens/))

- در این روش نیازی به database نیست و  تمام اطلاعات مورد نیاز در خود رشته توکن ذخیره می شود.
- ویژگی عمده این مدل اینه که امکان  validate کردن acces token ها را بدون نیاز به query دیتابیسی فراهم میکند و باعث مقیاس پذیری بیشتر API می شود.
- این نکته بسیار حائز اهمیت هست که اگر ما از قبل یک سیستم دیتابیسی برای توکن هامون ایجاد کردیم، الان استفاده از self-encoded token ها برامون هیچ ارزش افزوده ای ندارد و حتی در مورد منقضی کردن توکن ها برامون مشکل ساز میشود.
- در استفاده از self-encoded token ها بیشتر از همه پیاده سازی این مدل توکن ها مهم است چرا که اطلاعات توکن ما در معرض دیگر توسعه دهنده ها نیست(به علت رمزگذاری انجام شده توسط خودمان)
- یکی از راه های ساخت self-encoded token ساختن یک json serialized representaion از تمام اطلاعات موجود در توکن و استفاده از یک امضا برای آن با کلیدی است که فقط سرور آن را دارد.
- تکنیک معمول برای ساخت این مدل توکن ها json web signature یا همان jws که یک استاندارد برای handle کردن encoding هست می باشد حال jwt یا همان json web token یکسری مقررات استفاده از jws تعریف می کند که می توانیم داخل کد خود استفاده کنیم مثل قوانین تعریف timestamp که مثلا مشخص کننده تاریخ انقضای توکن ما هست.
- ضعف های ویژه این روش:
    1- هرکسی که به توکن دسترسی پیدا کند می تواند که با یک decoder اطلاعات را بخواند، پس باید اطلاعات مهم را در توکن قرار ندهیم و این اگر نیاز به قرار دادن اطلاعات مهم هست باید با استفاد از json web encryption اطلاعات داخل توکن را رمز گذاری کنیم.
    2- از آنجایی که این مدل توکن ها بدون هیچ کوئری دیتابیسی راستی آزمایی می شوند، امکان منقضی کردن یا باطل کردن زودتر از موعد انقضای داخی خودشان وجود ندارد. حال اگر شما می خواهید این کار را انجام دهید باید با خلاقیت خود چندین گام اضافه تر برای رفع این مشکل طراحی کنید.

#### رمزنگاری

(encoding)

کد زیر به زبان php نوشته شده و از کتابخانه firebase php-jwt برای encode کردن و راستی آزمایی کردن توکن استفاده شده است.

```php
<?php
use \Firebase\JWT\JWT;

# Define the secret key used to create and verify the signature
$jwt_key = 'secret';

# Set the user ID of the user this token is for
$user_id = 1000;

# Set the client ID of the app that is generating this token
$client_id = 'https://example-app.com';

# Provide the list of scopes this token is valid for
$scope = 'read write';

$token_data = array(

  # Subject (The user ID)
  'sub' => $user_id,

  # Issuer (the token endpoint)
  'iss' => 'https://' . $_SERVER['PHP_SELF'],

  # Client ID (this is a non-standard claim)
  'cid' => $client_id,

  # Issued At
  'iat' => time(),

  # Expires At
  'exp' => time()+7200, // Valid for 2 hours

  # The list of OAuth scopes this token includes
  'scope' => $scope
);
$token_string = JWT::encode($token_data, $jwt_key);
```

توکن خروجی اطلاعات بالا به صورت زیر خواهد بود:

```text
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEwMDAsI
mlzcyI6Imh0dHBzOi8vYXV0aG9yaXphdGlvbi1zZXJ2ZXIuY29tIiw
iY2lkIjoiaHR0cHM6Ly9leGFtcGxlLWFwcC5jb20iLCJpYXQiOjE0N
zAwMDI3MDMsImV4cCI6MTUyOTE3NDg1MSwic2NvcGUiOiJyZWFkIHd
yaXRlIn0.QiIrnmaC4VrbAYAsu0YPeuJ992p20fSxrXWPLw-gkFA
```

این توکن از 3 بخش اصلی تشکیل شده که با نقطه جدا شده اند که هرکدام از بخش های آن به ترتیب زیر معرف یک اطلاعاتی می باشند.

- قسمت اول توکن مشخص کننده نوع توکن و الگوریتم رمزگذاری استفاده شده در آن است.

    ```json
    {
      "typ": "JWT",
      "alg": "HS256"
    }
    ```

- قسمت دوم توکن حاوی اطلاعات اصلی و محتوای مورد نیاز ماست.

    ```json
    {
      "sub": 1000,
      "iss": "https://authorization-server.com",
      "cid": "https://example-app.com",
      "iat": 1470002703,
      "exp": 1470009903,
      "scope": "read write"
    }
    ```

- قسمت سوم توکن مشخص کننده امضا یا signature توکن می باشد.

    - الگووریتم رمز گذاری Base64-encoding قسمت اول و دوم توکن را که صورت های زیر هستند ترکیب کرده و یک امضا(رمز گذاری دیگر) روی آنها قرار می دهد.
    - قسمت اول:

        ```text
        eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
        ```

    - قسمت دوم:

        ```text
        eyJzdWIiOjEwMDAsImlzcyI6Imh0dHBzOi8vYXV0aG9yaXphdGlvbi1z
        ZXJ2ZXIuY29tIiwiY2lkIjoiaHR0cHM6Ly9leGFtcGxlLWFwcC5jb20i
        LCJpYXQiOjE0NzAwMDI3MDMsImV4cCI6MTUyOTE3NDg1MSwic2NvcGUi
        OiJyZWFkIHdyaXRlIn0
        ```

    - قسمت سوم: ترکیب این دو با استفاده از secret key خود سرور و ساخت امضا(قسمت سوم):

        ```text
        QiIrnmaC4VrbAYAsu0YPeuJ992p20fSxrXWPLw-gkF
        ```

    - خروجی ترکیب این 3 با هم به صورت زیر در می آید:

        ```text
        eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEwMDAsI
        mlzcyI6Imh0dHBzOi8vYXV0aG9yaXphdGlvbi1zZXJ2ZXIuY29tIiw
        iY2lkIjoiaHR0cHM6Ly9leGFtcGxlLWFwcC5jb20iLCJpYXQiOjE0N
        zAwMDI3MDMsImV4cCI6MTUyOTE3NDg1MSwic2NvcGUiOiJyZWFkIHd
        yaXRlIn0.QiIrnmaC4VrbAYAsu0YPeuJ992p20fSxrXWPLw-gkFA
        ```

#### بازگشایی رمز

(decoding)

با استفاده از همان کتابخانه استفاده شده برای encode و secret key موجود در سرور می توان token را decode کرد. باید توجه داشت که عمل راستی آزمایی (validate) و decode کردن همزمان اتفاق می افتد. البته در این نقطه ۲ استثنا وجود دارد که اگر اتفاق بیافتد ادامه کار متوقف شده و به فرایند جلوتر نمی رود.

1. امضا یا signature نادرست باشد.
2. توکن منقضی شده باشد.

هر کسی توانایی دارد که اگر به توکن دسترسی پیدا کرد با یکسری ابزار آنلاین حتی، آنرا decode کند و به اطلاعاتش دسترسی پیدا کند، پس باید توجه داشت که اطلاعات حساسی را در داخل توکن قرار ندهیم و اگر مجبور به اینکار شدیم از  JSON Web Encryption استفاده کنیم که محتوای داخل توکن به شکل زیر (رمز گذاری شده) نمایش داده خواهد شد.

```php
try {
  # Note: You must provide the list of supported algorithms in order to prevent
  # an attacker from bypassing the signature verification. See:
  # https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/
  $token = JWT::decode($token_string, $jwt_key, ['HS256']);
  $error = false;
} catch(\Firebase\JWT\ExpiredException $e) {
  $token = false;
  $error = 'expired';
  $error_description = 'The token has expired';
} catch(\Firebase\JWT\SignatureInvalidException $e) {
  $token = false;
  $error = 'invalid';
  $error_description = 'The token provided was malformed';
} catch(Exception $e) {
  $token = false;
  $error = 'unauthorized';
  $error_description = $e->getMessage();
}

if($error) {
  header('HTTP/1.1 401 Unauthorized');
  echo json_encode(array(
    'error'=>$error,
    'error_description'=>$error_description
  ));
  die();
} else {
  // Now $token has all the data that we encoded in it originally
  print_r($token);
}
```

در این نقطه سرویس به تمام اطلاعات مورد نیاز خود از جمله id و scope و ... داخل توکن باز شده دسترسی خواهد داشت بدون آنکه به هیچ کوئری دیتابیسی نیاز داشته باشد.

#### باطل کردن

(Invalidating)

از آنجایی که توکن ها همگی بدون هیچ کوئری دیتابیسی راستی آزمایی می شوند، راهی برای باطل کردن آنها زودتر از موعد expire داخل خود توکن وجود ندارد. البته شما خودتان می توانید با طراحی چندین گام اضافه تر، این مشکل را به روش خودتون handle کنید.

### کوئری دیتا بیسی برای توکن های دسترسی

(database query for access token)

اگر شما از یک دیتابیس برای ذخیره کردن توکن های ساخته شده استفاده می کنید، راستی آزمایی کردن هر توکن با یک کوئری دیتابیسی ساده قابل انجام خواهد بود.

## توکن های دسترسی مادام العمر

([Access Token Lifetime](https://www.oauth.com/oauth2-servers/access-tokens/access-token-lifetime/))

1. access token های با تاریخ انقضای کوتاه به همراه ساخت refresh token ها

   (Short-lived access tokens and long-lived refresh tokens)

    - هنگام استفاده از self-encoded token ها کاربرد دارد
    - برای محدود کردن ریسک لو رفتن access token
    - فراهم کردن یک sdk که می تواند برای handle کردن منطق پیاده سازی refresh code برای developer ها شفاف سازی کند.

2. access token های با تاریخ انقضای کوتاه بدون ساخت refresh token ها

   (Short-lived access tokens and no refresh tokens)

    - برای محافظت بیشتر از لو رفتن access token
    - هنگامی که می خواهیم همیشه کاربر از دسترسی سرویس ثالث به اطلاعاتش مطلع باشد
    - هنگامی که نمی خواهیم سرویس های ثالث به صورت آفلاین به داده های کاربر دسترسی داشته باشند.

3. access token های بدون تاریخ انقضا

   (Non-expiring access tokens)

    - هنگامی که یک مکانیزم خاص برای باطل کردن access token ها داریم
    - هنگامی که لو رفتن توکن باعث ریسک زیادی برای ما نباشد (زیاد خطر آفرین نباشد)
    - هنگامی که می خواهید یک مکانیزم احراز هویت راحت برای developer ها فراهم کنید
    - هنگامی که می خواهید به سرویس های ثالث اجازه دسترسی آفلاین به داده های کاربران را بدهید

# Gradient Descent With Momentum

## Description

<span dir="rtl">با استفاده از این تکنیک، بعد از محاسبه</span> <span dir="ltr">dw</span> <span dir="rtl">و</span> <span dir="ltr">db</span> <span dir="rtl">بجای استفاده مستقیم از اونا، اول توی فرمول</span> <span dir="ltr">exponential weighted moving average</span> <span dir="rtl">قرار میدیم و نتیجه حاصل رو برای محاسبه</span> <span dir="ltr">w</span> <span dir="rtl">و</span> <span dir="ltr">b</span> <span dir="rtl">بعدی استفاده میکنیم، با این کار عملا سرعت یادگیری رو بالا تر میبریم و زودتر به گلوبال مینیمم میرسیم، البته باید توجه کنیم که مقدار</span> <span dir="ltr">β</span> <span dir="rtl">رو ما خودمون باید به شکل تجربی بسته به شرایط انتخاب کنیم.</span>

<img src="image1.jpg" style="width:2.99842in" />

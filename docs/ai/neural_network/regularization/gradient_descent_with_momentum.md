# Gradient Descent With Momentum

## Description

<span dir="rtl">با استفاده از این تکنیک، بعد از محاسبه dw و db بجای استفاده مستقیم از اونا، اول توی فرمول exponential weighted moving average قرار میدیم و نتیجه حاصل رو برای محاسبه w و b بعدی استفاده میکنیم، با این کار عملا سرعت یادگیری رو بالا تر میبریم و زودتر به گلوبال مینیمم میرسیم، البته باید توجه کنیم که مقدار β رو ما خودمون باید به شکل تجربی بسته به شرایط انتخاب کنیم.</span>

## Formula

Compute $dW, db$

$$
v_{dw} = \beta v_{dw} + (1 - \beta)dW \\
v_{db} = \beta v_{db} + (1 - \beta)db \\
W = W - \alpha v_{dw}, b = b - \alpha v_{db}
$$

$\beta = 0.9$

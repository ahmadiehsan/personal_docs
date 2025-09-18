# Adam

## Description

<img src="image2.jpg" style="width:5in" />

<span dir="rtl">طبق یه الگوریتمی تشخیص میده اگر حرکت به سمت نقطه minimum داره صورت میگیره سرعت حرکت رو با افزایش مقدار α بیشتر میکنه در غیر این صورت سرعت رو با کاهش مقدار α کمتر میکنه.</span>

## Formula

Initialize: $V_{dw} = 0$, $S_{dw} = 0$, $V_{db} = 0$, $S_{db} = 0$

On iteration $t$: Compute $dW$, $db$ using the current mini-batch.

$V_{dw} = \beta_1 V_{dw} + (1 - \beta_1) dW$, $V_{db} = \beta_1 V_{db} + (1 - \beta_1) db$ <-- "momentum" $\beta_1$

$S_{dw} = \beta_2 S_{dw} + (1 - \beta_2) dW^2$, $S_{db} = \beta_2 S_{db} + (1 - \beta_2) db^2$ <-- "RMSprop" $\beta_2$

$V_{dw}^{\text{corrected}} = V_{dw} / (1 - \beta_1^t)$, $V_{db}^{\text{corrected}} = V_{db} / (1 - \beta_1^t)$

$S_{dw}^{\text{corrected}} = S_{dw} / (1 - \beta_2^t)$, $S_{db}^{\text{corrected}} = S_{db} / (1 - \beta_2^t)$

$W := W - \alpha \frac{V_{dw}^{\text{corrected}}}{\sqrt{S_{dw}^{\text{corrected}}} + \epsilon}$, $b := b - \alpha \frac{V_{db}^{\text{corrected}}}{\sqrt{S_{db}^{\text{corrected}}} + \epsilon}$

!!! info

    <span dir="rtl">در اصل این تکنیک ترکیبی از تکنیک های Gradient Descent With Momentum و RMS-prop هستش.</span>

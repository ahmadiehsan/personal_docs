# Feed Forward (FFNN) [Fully-Connected]

## Description

This is the most straightforward type of neural network. Information in this network moves in one direction only, from the input layer through any hidden layers to the output layer. The network has no cycles or loops; it’s a straight, “feedforward” path.

<img src="image3.png" style="width:3.72396in" />

Multilayer perceptron (MLP) is a type of feedforward network that has at least one hidden layer in addition to its input and output layers. The layers are fully connected, meaning each neuron in a layer connects with every neuron in the next layer. MLPs can model complex patterns and are widely used for tasks such as image recognition, classification, speech recognition, and other types of machine learning tasks. The MLP is a feedforward network with layers of neurons arranged sequentially. Information flows from the input layer through hidden layers to the output layer in one direction.

<img src="image4.jpg" style="width:3.01563in" />

<span dir="rtl">تصویر بالا نمونه یک شبکه عصبی با سه لایه هستش که موارد زیر بهش صدق میکنه:</span>

- <span dir="rtl">به</span> <span dir="ltr">layer</span> <span dir="rtl">1 و</span> <span dir="ltr">layer</span> <span dir="rtl">2 لایه های مخفی (</span><span dir="ltr">hidden layers</span><span dir="rtl">) می گن</span>
- <span dir="rtl">بخش نارنجی رنگ رو</span> <span dir="ltr">layer</span> <span dir="rtl">0 میگن ولی جزو لایه های نمیشمارن</span>
- <span dir="rtl">علاوه بر</span> <span dir="ltr">x</span> <span dir="rtl">به بخش نارنجی رنگ</span<img src="span> <span dir="rtl">هم می گن</span>
- <span dir="rtl">به هر دایره یک</span> <span dir="ltr">neuron</span> <span dir="rtl">و یا</span> <span dir="ltr">unit</span> <span dir="rtl">می گن</span>
- <span dir="rtl">به خروجی هر لایه</span> <span dir="ltr">activation</span> <span dir="rtl">میگن که با عملات</span> <span dir="ltr">a</span> <span dir="rtl">نشون داده میشه</span>

<span dir="ltr"></span>

<img src="image10.png" style="width:1.67964in" />

<img src="image11.png" style="width:1.66462in" />

- <span dir="rtl">تو دو تا تصویر بالا منظور از \[1\] یا \[2\] و … نشان دهنده تعلق فرمول به چندمین لایه شبکه هستش</span>
- <span dir="rtl">تو دو تا تصویر بالا منظور از 1 یا 15 و … در زیر هر علامت نشان دهنده تعلق فرمول به چندمین</span> <span dir="ltr">unit</span> <span dir="rtl">یک لایه هستش. توجه بشه که اعداد ربطی به ایندکس آن متغیر در داخل فرمول نداره و بالاش علامت</span> <span dir="ltr">vector</span> <span dir="rtl">اومده که نشون میده این علامت نماینده چندین متغیر در داخل فرمول هستش</span>

## Life Cycle

<img src="image8.jpg" style="width:4.77437in" />

- <span dir="rtl">تو تصویر بالا به خوبی نحوه عملکرد شبکه عصبی برای یک ورودی</span> <span dir="ltr">x</span> <span dir="rtl">شرح داده شده</span>
- <span dir="rtl">سیستم به صورت ریکرسیو عمل میکنه</span>
- <span dir="rtl">فلش های آبی نشون دهنده</span> <span dir="ltr">Forward propagation</span> <span dir="rtl">و فلش های قرمز نشون دهنده</span> <span dir="ltr">Backward propagation</span> <span dir="rtl">هستن</span>

## Vectorized Version

<img src="image2.jpg" style="width:2.32746in" />

<img src="image7.jpg" style="width:2.22727in" />

<img src="image6.jpg" style="width:4.14343in" />

<img src="image1.jpg" style="width:2.44874in" />

<span dir="rtl">برای فهم بهتر به لینک زیر بروید:</span>

[Link](https://jonaslalin.com/2021/12/10/feedforward-neural-networks-part-1/)

## Dimensions

| نوع                                          | z       | w       | x       | b       |
|---------------------------------------------|---------|---------|---------|---------|
| یک عصب، نشان: 1<br />یک فیچر، نشان: 1<br />یک نمونه، نشان: 1 | (1, 1)  | (1, 1)  | (1, 1)  | (1, 1)  |
| یک عصب، نشان: 1<br />چند فیچر، نشان: x<br />یک نمونه، نشان: 1 | (1, 1)  | (1, x)  | (x, 1)  | (1, 1)  |
| یک عصب، نشان: 1<br />چند فیچر، نشان: x<br />چند نمونه، نشان: m | (1, m)  | (1, x)  | (x, m)  | (1, 1)  |
| چند عصب، نشان: j<br />یک فیچر، نشان: 1<br />یک نمونه، نشان: 1 | (j, 1)  | (j, 1)  | (1, 1)  | (j, 1)  |
| چند عصب، نشان: j<br />چند فیچر، نشان: x<br />یک نمونه، نشان: 1 | (j, 1)  | (j, x)  | (x, 1)  | (j, 1)  |
| چند عصب، نشان: j<br />چند فیچر، نشان: x<br />چند نمونه، نشان: m | (j, m)  | (j, x)  | (x, m)  | (j, 1)  |

## Batch Normalization

<span dir="rtl">این تکنیک دقیقا تکنیک</span> <span dir="ltr">Z-score normalization</span> <span dir="rtl">هستش ولی فقط تو قالب شبکه عصبی پیاده میشه.</span>

<img src="image5.jpg" style="width:1.31909in" />

- <span dir="rtl">علامت</span> <span dir="ltr">μ</span> <span dir="rtl">میانگین تمامی نتایج لایه هستش</span>
- <span dir="rtl">فرمول خط چهارم در اصل نتیجه حاصل از</span> <span dir="ltr">Normalization</span> <span dir="rtl">هستش ولی چون ممکنه رنج این نتیجه مناسب لایه بعدی نباشه با استفاده از فرمول خط پنجم و دو متغیر</span> <span dir="ltr">ɣ</span> <span dir="rtl">و</span> <span dir="ltr">β</span> <span dir="rtl">یه سری تغییر توش میدیم که رنجش عوض بشه</span>

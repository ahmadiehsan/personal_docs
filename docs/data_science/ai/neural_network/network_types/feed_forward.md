# Feed Forward (FFNN) [Fully-Connected]

## Description

This is the most straightforward type of neural network. Information in this network moves in one direction only, from
the input layer through any hidden layers to the output layer. The network has no cycles or loops; it’s a straight,
"feedforward" path.

<img src="image3.png" style="width:3.72396in" />

Multilayer perceptron (MLP) is a type of feedforward network that has at least one hidden layer in addition to its input
and output layers. The layers are fully connected, meaning each neuron in a layer connects with every neuron in the next
layer. MLPs can model complex patterns and are widely used for tasks such as image recognition, classification, speech
recognition, and other types of machine learning tasks. The MLP is a feedforward network with layers of neurons arranged
sequentially. Information flows from the input layer through hidden layers to the output layer in one direction.

<img src="image4.jpg" style="width:3.01563in" />

<span dir="rtl">تصویر بالا نمونه یک شبکه عصبی با سه لایه هستش که موارد زیر بهش صدق میکنه:</span>

- <span dir="rtl">به layer 1 و layer 2 لایه های مخفی (hidden layers) می گن</span>
- <span dir="rtl">بخش نارنجی رنگ رو layer 0 میگن ولی جزو لایه های نمیشمارن</span>
- <span dir="rtl">به هر دایره یک neuron و یا unit می گن</span>
- <span dir="rtl">به خروجی هر لایه activation میگن که با عملات a نشون داده میشه</span>

<img src="image10.png" style="width:1.67964in" />

<img src="image11.png" style="width:1.66462in" />

- <span dir="rtl">تو دو تا تصویر بالا منظور از \[1\] یا \[2\] و … نشان دهنده تعلق فرمول به چندمین لایه شبکه هستش</span>
- <span dir="rtl">تو دو تا تصویر بالا منظور از 1 یا 15 و … در زیر هر علامت نشان دهنده تعلق فرمول به چندمین unit یک لایه
  هستش. توجه بشه که اعداد ربطی به ایندکس آن متغیر در داخل فرمول نداره و بالاش علامت vector اومده که نشون میده این علامت
  نماینده چندین متغیر در داخل فرمول هستش</span>

## Life Cycle

<img src="image8.jpg" style="width:4.77437in" />

- <span dir="rtl">تو تصویر بالا به خوبی نحوه عملکرد شبکه عصبی برای یک ورودی x شرح داده شده</span>
- <span dir="rtl">سیستم به صورت ریکرسیو عمل میکنه</span>
- <span dir="rtl">فلش های آبی نشون دهنده Forward propagation و فلش های قرمز نشون دهنده Backward propagation هستن</span>

## Vectorized Version

$z_{j,i}^{[l]} = \sum_k w_{j,k}^{[l]} a_{k,i}^{[l-1]} + b_j^{[l]},$

$a_{j,i}^{[l]} = g_j^{[l]} \left( z_{1,i}^{[l]}, \dots, z_{j,i}^{[l]}, \dots, z_{n^{[l]},i}^{[l]} \right)$

| Entity            | Description                                                                                                                                                              |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $l$               | The current layer $l = 1, \ldots, L$, where $L$ is the number of layers that have weights and biases. We use $l = 0$ and $l = L$ to denote the input and output layers.  |
| $n^{[l]}$         | The number of nodes in the current layer.                                                                                                                                |
| $n^{[l-1]}$       | The number of nodes in the previous layer.                                                                                                                               |
| $j$               | The $j$-th node of the current layer, $j = 1, \ldots, n^{[l]}$.                                                                                                          |
| $k$               | The $k$-th node of the previous layer, $k = 1, \ldots, n^{[l-1]}$.                                                                                                       |
| $i$               | The current training example $i = 1, \ldots, m$, where $m$ is the number of training examples.                                                                           |
| $z^{[l]}_{j,i}$   | A weighted sum of the activations of the previous layer, shifted by a bias.                                                                                              |
| $w^{[l]}_{j,k}$   | A weight that scales the $k$-th activation of the previous layer.                                                                                                        |
| $b^{[l]}_j$       | A bias in the current layer.                                                                                                                                             |
| $a^{[l]}_{j,i}$   | An activation in the current layer.                                                                                                                                      |
| $a^{[l-1]}_{k,i}$ | An activation in the previous layer.                                                                                                                                     |
| $g^{[l]}_j$       | An activation function $g^{[l]}_j: \mathbb{R}^{n^{[l]}} \rightarrow \mathbb{R}$ used in the current layer.                                                               |

$$
\begin{bmatrix}
z_{1,i}^{[l]} \\
\vdots \\
z_{j,i}^{[l]} \\
\vdots \\
z_{n^{[l]},i}^{[l]}
\end{bmatrix}
=
\begin{bmatrix}
w_{1,1}^{[l]} & \dots & w_{1,k}^{[l]} & \dots & w_{1,n^{[l-1]}}^{[l]} \\
\vdots & \ddots & \vdots & \ddots & \vdots \\
w_{j,1}^{[l]} & \dots & w_{j,k}^{[l]} & \dots & w_{j,n^{[l-1]}}^{[l]} \\
\vdots & \ddots & \vdots & \ddots & \vdots \\
w_{n^{[l]},1}^{[l]} & \dots & w_{n^{[l]},k}^{[l]} & \dots & w_{n^{[l]},n^{[l-1]}}^{[l]}
\end{bmatrix}
\begin{bmatrix}
a_{1,i}^{[l-1]} \\
\vdots \\
a_{k,i}^{[l-1]} \\
\vdots \\
a_{n^{[l-1]},i}^{[l-1]}
\end{bmatrix}
+
\begin{bmatrix}
b_1^{[l]} \\
\vdots \\
b_j^{[l]} \\
\vdots \\
b_{n^{[l]}}^{[l]}
\end{bmatrix}
$$

$$
\begin{bmatrix}
a_{1,i}^{[l]} \\
\vdots \\
a_{j,i}^{[l]} \\
\vdots \\
a_{n^{[l]},i}^{[l]}
\end{bmatrix}
=
\begin{bmatrix}
g_1^{[l]}(z_{1,i}^{[l]}, \dots, z_{j,i}^{[l]}, \dots, z_{n^{[l]},i}^{[l]}) \\
\vdots \\
g_j^{[l]}(z_{1,i}^{[l]}, \dots, z_{j,i}^{[l]}, \dots, z_{n^{[l]},i}^{[l]}) \\
\vdots \\
g_{n^{[l]}}^{[l]}(z_{1,i}^{[l]}, \dots, z_{j,i}^{[l]}, \dots, z_{n^{[l]},i}^{[l]})
\end{bmatrix}
$$

<span dir="rtl">برای فهم بهتر به لینک زیر بروید:</span>

[Link](https://jonaslalin.com/2021/12/10/feedforward-neural-networks-part-1/)

## Dimensions

| نوع                                                                                    | z      | w      | x      | b      |
|----------------------------------------------------------------------------------------|--------|--------|--------|--------|
| <span dir="rtl">یک عصب، نشان: 1<br />یک فیچر، نشان: 1<br />یک نمونه، نشان: 1</span>    | (1, 1) | (1, 1) | (1, 1) | (1, 1) |
| <span dir="rtl">یک عصب، نشان: 1<br />چند فیچر، نشان: x<br />یک نمونه، نشان: 1</span>   | (1, 1) | (1, x) | (x, 1) | (1, 1) |
| <span dir="rtl">یک عصب، نشان: 1<br />چند فیچر، نشان: x<br />چند نمونه، نشان: m</span>  | (1, m) | (1, x) | (x, m) | (1, 1) |
| <span dir="rtl">چند عصب، نشان: j<br />یک فیچر، نشان: 1<br />یک نمونه، نشان: 1</span>   | (j, 1) | (j, 1) | (1, 1) | (j, 1) |
| <span dir="rtl">چند عصب، نشان: j<br />چند فیچر، نشان: x<br />یک نمونه، نشان: 1</span>  | (j, 1) | (j, x) | (x, 1) | (j, 1) |
| <span dir="rtl">چند عصب، نشان: j<br />چند فیچر، نشان: x<br />چند نمونه، نشان: m</span> | (j, m) | (j, x) | (x, m) | (j, 1) |

## Batch Normalization

<span dir="rtl">این تکنیک دقیقا تکنیک Z-score normalization هستش ولی فقط تو قالب شبکه عصبی پیاده میشه.</span>

$\mu = \frac{1}{m} \sum_i z^{(i)}$

$\sigma^2 = \frac{1}{m} \sum_i (z^{(i)} - \mu)^2$

$z_{norm}^{(i)} = \frac{z^{(i)} - \mu}{\sqrt{\sigma^2 + \epsilon}}$

$\tilde{z}^{(i)} = \gamma z_{norm}^{(i)} + \beta$

- <span dir="rtl">علامت $\mu$ میانگین تمامی نتایج لایه هستش</span>
- <span dir="rtl">فرمول خط چهارم در اصل نتیجه حاصل از Normalization هستش ولی چون ممکنه رنج این نتیجه مناسب لایه بعدی
  نباشه با استفاده از فرمول خط پنجم و دو متغیر ɣ و β یه سری تغییر توش میدیم که رنجش عوض بشه</span>

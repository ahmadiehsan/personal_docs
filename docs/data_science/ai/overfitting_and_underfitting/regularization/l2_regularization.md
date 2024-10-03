# L2 regularization (Ridge)

## Description

Ridge regression, a linear regression method applicable to feature selection, closely resembles ordinary least squares regression but introduces a penalty term to the cost function to counter overfitting.

In ridge regression, the cost function undergoes modification with the inclusion of a penalty term directly proportional to the square of the coefficients’ magnitude. This penalty term is regulated by a hyperparameter, often denoted as λ or α dictating the regularization strength. When α is set to zero, ridge regression reverts to ordinary least squares regression.

The penalty term’s impact manifests in shrinking the coefficients’ magnitude toward zero. This proves beneficial in mitigating overfitting, discouraging the model from excessively relying on any single feature. In effect, the penalty term acts as a form of feature selection by reducing the importance of less relevant features.

Ridge regression can be used for feature selection by examining the magnitudes of the coefficients produced by the model. Features with coefficients that are close to zero or smaller are considered less important and can be dropped from the model. The value of α can be tuned using cross-validation to find the optimal balance between model complexity and accuracy.

One of the main advantages of ridge regression is its ability to handle multicollinearity, which occurs when there are strong correlations between the independent variables. In such cases, ordinary least squares regression can produce unstable and unreliable coefficient estimates, but ridge regression can help stabilize the estimates and improve the overall performance of the model.

## Formula

The equation for the ridge regression loss function is as follows:

<img src="image1.png" style="width:2.26563in" />

Here, we have the following:

- N is the number of samples in the training set.
- y is the column vector of target values of size N.
- X is the design matrix of input features.
- w is the vector of regression coefficients to be estimated.
- α is the regularization parameter that controls the strength of the penalty term. It is a hyperparameter that needs to be tuned.

The first term in the loss function measures the mean squared error between the predicted values and the true values. The second term is the 𝓁 2 penalty term that shrinks the coefficients toward zero. The ridge regression algorithm finds the values of the regression coefficients that minimize this loss function. By tuning the regularization parameter, α, we can control the bias-variance trade-off of the model, with higher alpha values leading to more regularization and lower overfitting.

## How It Works

<img src="image4.png" style="width:3.5293in" />

<span dir="rtl">تو تصویر بالا نشون داده شده که با اعمال ضریب های (</span><span dir="ltr">w</span><span dir="rtl">) کوچک امتحان میکنیم که آیا حذف یک متغیر دارای توان به حل مشکل ما کمک میکند یا خیر، از آنجایی که مقادیر</span> <span dir="ltr">w</span> <span dir="rtl">و</span> <span dir="ltr">b</span> <span dir="rtl">را سیستم بطور اتوماتیک تعیین میکند و ما در آنها نقشی نداریم لذا با استفاده از روش زیر، سیستم را مجبور به انتخاب اعداد کوچک برای ضریب های (</span><span dir="ltr">w</span><span dir="rtl">) دلخواه خود میکنیم:</span>

<img src="image3.png" style="width:3.63959in" />

<span dir="ltr"></span> <span dir="rtl">در تصویر بالا ما تنها تاثیر دو متغیر</span> <span dir="ltr">w</span> <span dir="rtl">سه و</span> <span dir="ltr">w</span> <span dir="rtl">چهار را کم کردیم، اما در سیستم های پیچیده تر بجای این کار از الگوی زیر استفاده می شود:</span>

<img src="image2.png" style="width:3.42707in" />

<span dir="rtl">در الگوی بالا</span> <span dir="ltr">n</span> <span dir="rtl">تعداد متغیر های (</span><span dir="ltr">w</span><span dir="rtl">) های حاضر در معادله هستش، با بالا بردن</span> <span dir="ltr">λ</span> <span dir="rtl">سیستم مجبور به انتخاب</span> <span dir="ltr">w</span> <span dir="rtl">های کوچکتر می شود که دقیقا هدف ما از انجام</span> <span dir="ltr">Regularization</span> <span dir="rtl">هستش</span>

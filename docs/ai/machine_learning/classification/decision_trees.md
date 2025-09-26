# Decision Trees [Sup] {Random Forest} {XGBoost]}

## Description

Introduction Decision Trees are a type of Supervised Machine Learning (that is you explain what the input is and what the corresponding output is in the training data) where the data is continuously split according to a specific parameter.
The tree can be explained by two entities, namely decision nodes, and leaves.

<img src="decision_trees_overview.jpg" style="width:3.5in" />

<span dir="rtl">همیشه باید بشکنه به دو تا حالت (Ture یا False) اگر فیچری داشتیم که باعث میشد سه یا بیشتر حالت پیش بیاد با اون فیچر رو به حالت های ریز تر که Ture یا False ای هستن بشکنیم</span>

## Varieties

=== "Random Forest"

    The random forest is a classification algorithm consisting of many decision trees.
    It uses bagging and features randomness when building each tree to try to create an uncorrelated forest of trees whose prediction by committee is more accurate than that of any individual tree.

    <img src="random_forest_overview.png" style="width:4in" />

    One of the most commonly known ensemble models is random forest, where the model combines the predictions of multiple decision trees and outputs the predictions.
    This is usually more accurate and prone to overfitting.

    <span dir="rtl">تو این الگوریتم با انتخاب تصادفی از دیتا ست اصلی چندین دیتا ست کوچیک تر میسازه و از رو هر کدوم یک decision tree میسازه و ورودی رو به همه اون ها میده و در نهایت بین جواب های حاصل برایند میگیره و نظر نهاییش رو اعلام میکنه</span>

=== "XGBoost"

    XGBoost (eXtreme Gradient Boosting) is a popular supervised-learning algorithm used for regression and classification on large datasets.
    It uses sequentially-built shallow decision trees to provide accurate results and a highly scalable training method that avoids overfitting.

    <img src="xgboost_overview.png" style="width:4in" />

    <span dir="rtl">بر خلاف random forest که دیتاست های رندم میسازه، تو این الگو یک دیتا ست اولیه میسازه و بر اساسش یک decision tree میسازه و با تست کردن نتایج و پیدا کردن نقاط ضعفش این بار یک دیتاست دقیق تر رو انتخاب میکنه دوباره decision tree رو ایجاد میکنه، انقدر این کارو تکرار میکنه تا یه decision tree کامل و با کمترین اشکال ایجاد کنه.</span>

## Random Forest Vs PCA

- In each of the supervised learning use cases, random forest can be used to reduce the number of dimensions in data.
- For unsupervised dimensionality reduction tasks, PCA can be helpful.

## Information Gain Technique

![](decision_trees/image1.png)

- <span dir="rtl">از این فرمول برای انتخاب ترتیب شکستن شاخه ها استفاده میشه</span>
- <span dir="rtl">هر چقدر یک ویژگی (feature یا input) به ما entropy بهتری بده (نزدیکتر به ۰) به این معنیه که اول بر اساس اون ویژگی بشکنیم بعدش بریم سراغ ویژگی های بعدی</span>

![](decision_trees/image4.png)

<span dir="rtl">تو تصویر بالا جایی که هیچکدوم از حیوون ها گربه نیستن فرمول به ما ۰ داده و همینطور جایی که همه شون گربه هستن هم ۰ داده (فرقی نداره که همه باشن یا هیچکدوم نباشن، همین که purity رعایت بشه کافیه)</span>

![](decision_trees/image2.png)

<span dir="rtl">حالا وقتی میخوایم از فرمول entropy برای decision trees استفاده کنیم، باید entropy هر طرف رو حساب کنیم، میانگینش رو بدست بیاریم (میانگین بر اساس تعداد دیتاهای هر سمت) و آخرسر نتیجه رو از entropy اولیه دیتا ست کم کنیم، به این فرمول میگن فرمول information gain که هرچقدر حاصل فرمول information gain بیشتر باشه یعنی گزینه بهتریه. (تو تصویر چون information gain سمت چپی بیشتره پس بر اساس اون دیتا مون رو میشکنیم)</span>

<span dir="rtl">برای فیچر هایی که یک مقدار ثابت ندارن (مثلا وزن) با استفاده از تکنیک تصویر زیر اون هارو به حالت True و False ای تغییر میدیم:</span>

![](decision_trees/image5.png)

# Simple Recommendation {Unsup}

## Description

Recommendation engines are a subclass of machine learning which generally deal with ranking or rating products / users. Loosely defined, a recommender system is a system which predicts ratings a user might give to a specific item.

<img src="image3.jpg" style="width:4.95313in" />

- <span dir="rtl">این یه الگوریتم واقعی نیستش، فقط برای فهم بهتر الگوریتم Collaborative Filtering مطرح شده</span>

## Formula

<img src="image2.jpg" style="width:4.89254in" />

<span dir="rtl">دقیقا مشابه با Linear regression هستش با این تفاوت که برای هر کاربر سامانه یه فرمول جدا و مخصوص به خودش داریم، چون نمیشه یه شبکه عصبی درست کرد و برای همه استفاده کرد هرکس سلیقه خودشو داره.</span>

## Specific Cost Function (Squared Error Loss)

<img src="image4.jpg" style="width:4.73846in" />

<img src="image1.jpg" style="width:4.62143in" />

<span dir="rtl">چون چندین Linear regression داریم اینجا برای محاسبه Cost function مجموع تمامی (دوتا سیگما) رو در نظر میگیریم.</span>

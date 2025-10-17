# Vs (Recall & Precision)

## Description

Often you have a trade-off between Recall and Precision.

While **recall** expresses the ability to find all relevant instances in a dataset, **precision** expresses the proportion of the data points our model says were relevant actually were relevant.

## Example

- <span dir="rtl">به عنوان مثال یک الگوریتم یادگیری ماشینی از میان ۱۲ تصویر سگ و گربه ۸ مورد سگ را تشخیص می‌دهد. از ۸ سگ ۵ مورد واقعاً سگ هستند (مثبت درست یا true positives) و ۳ مورد دیگر گربه هستند؛ که مثبت نادرست یا false positives هستند. مقدار precision برابر با ۵/۸ است و مقدار recall برابر با ۵/۱۲ است.</span>
- <span dir="rtl">وقتی موتور جستجو ۳۰ صفحه را بازمی‌گرداند و فقط ۲۰ موردش مرتبط هستند و به اشتباه ۴۰ مورد دیگر که مرتبط بودند را باز نمی‌گرداند. مقدار precision برابر با ۲۰/۳۰=۲/۳ و مقدار recall برابر با ۲۰/۶۰=۱/۳ است. در نتیجه در این مورد precision نشان می‌دهد که چقدر موتور جستجو به درد بخور است و recall نشان می‌دهد که چه مقدار پاسخش کامل و جامع است.</span>

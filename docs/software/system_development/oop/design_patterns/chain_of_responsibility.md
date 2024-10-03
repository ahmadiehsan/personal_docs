# Chain of Responsibility (Request delegation chain) [Behavioral]

## Description

![](chain_of_responsibility/image2.jpg)

Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

![](chain_of_responsibility/image1.jpg)

<span dir="rtl">حاشیه ها:</span>

- <span dir="rtl">از این پترن در دستگاه های ای تی ام استفاده میکنن، به شکلی که هر باکس پول تلاش میکنه کل مبلغ درخواستی رو از خودش تامین کنه اگر نشد میده به باکس بعدی پول.</span>
- <span dir="rtl">از نمونه های دیگه اش، میشه به استفاده اش تو کروم استفاده کرد, سیستمش به این شکله که وقتی کلیک میکینم این ایونت انقدر بین المنت ها پاس داده میشه تا بالاخره برسه به المنتی که میتونه کلیک رو هندل کنه.</span>

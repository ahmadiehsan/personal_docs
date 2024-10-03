# Proxy (Controlled access) [Structural]

## Description

<img src="image2.jpg" style="width:5.77565in" />

Provides a surrogate or placeholder for another object to control access to it.

Use the Proxy Pattern to create a representative object that controls access to another object, which may be remote, expensive to create, or in need of securing.

- As we know, a remote proxy controls access to a remote object.
- A virtual proxy controls access to a resource that is expensive to create.
- A protection proxy controls access to a resource based on access rights.
- A caching proxy maintains a cache of previously created objects and when a request is made it returns a cached object, if possible.

<span dir="rtl">حاشیه ها:</span>

- <span dir="rtl">بطور کلی، وقتی که میخوایم یه سری کارهای مربوط به کنترل دسترسی رو انجام بدیم از این پترن استفاده میکنیم.</span>
- <span dir="rtl">یکی از کاربردهای جالبش در ساخت او آر ام های اکتیو رکورد هستش.</span>
- <span dir="rtl">یکی دیگه از کاربردهای خوبش زمانیه که میخوایم از یه کتابخونه استفاده کنیم ولی قبلش لازم داریم روی آبجکت اون کتابخونه تغییراتی داشته باشیم.</span>
- <span dir="rtl">یه فرقی که این پترن با دکوریتور داره اینه که هدف اصلیش اضافه کرنم بیهیویر یه آبجکت نیست (البته که ممکنه این کارو بکنه)، از این گذشته به دکوریتور حتما باید آبجکت رو پاس بدی ولی اینجا ممکنه آبجکت توسط خود پراکسی ساخته بشه.</span>

## Remote Proxy

<img src="image3.jpg" style="width:4.69034in" />

With the Remote Proxy, the proxy acts as a local representative for an object that lives in a different JVM. A method call on the proxy results in the call being transferred over the wire and invoked remotely, and the result being returned to the proxy and then to the Client.

## Virtual Proxy

<img src="image1.jpg" style="width:4.54488in" />

The Virtual Proxy acts as a representative for an object that may be expensive to create. The Virtual Proxy often defers the creation of the object until it is needed; the Virtual Proxy also acts as a surrogate for the object before and while it is being created. After that, the proxy delegates requests directly to the RealSubject.

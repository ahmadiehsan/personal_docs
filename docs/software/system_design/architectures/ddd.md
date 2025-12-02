# DDD

## Description

<img src="image2.jpg" style="width:2.64908in" />

<img src="image3.jpg" style="width:4.47917in" />

Types of Domain:

- Core domain
- Supporting domain
- Generic domain

Glossary:

- **Entities**: Domain objects with a unique identity. Embodies a set of critical business rules.
- **Aggregates**: Group of Entity objects which always need to be in a consistent state.
- **Aggregate Root (AR)**: Entry point Entity for an aggregate. All business operations should go through the root. An Aggregate should be referenced from outside only through its root. AR should have pure, side-effect-free functions.
- **Value Objects**: Immutable objects without identity. Only value matters. Brings context to the value.
- **Domain Events**: Decouple different domains. Describe things that happen and change the state of a domain. It makes the system extendable. Domain event listeners run in a different transaction than the event publishers. In Domain-driven systems, domain events are an excellent way of achieving eventual consistency. Any system or module that needs to update itself when something happens in another module or system can subscribe to the domain events coming from that system.
- **Domain Services**: Business logic that cannot fit in the aggregate. Used when multiple aggregates are required in business logic. Can interact with other domain services.
- **Application Services**: Allows the isolated domain to communicate with the outside. Orchestrates transactions, and security, look up proper aggregates, and saves state changes of the domain to the database. Does not contain any business logic. Domain event listeners are a special kind of Application service that is triggered by domain events. Each domain event listener can have a separate domain service to handle business logic.

## Core Domain Parts

### Aggregate

<img src="image10.jpg" />

- <span dir="rtl">یک سلسله انتیتی هایی که با هم ساخته و تغییر میکنند</span>
- <span dir="rtl">تا جایی که میشه باید کوچیک باشه</span>

### Aggregate Root

- <span dir="rtl">انتیتی اصلی ای که توی یک اگریگیت وجود دارد و آی دی کل اگریگیت رو برابر با آی دی این انتیتی قرار میدهیم</span>
- <span dir="rtl">یعنی آی دی دیگر انتیتی های داخل یک اگریگیت توسط اگریگیت های دیگر قابل دسترسی نیست</span>

### Value Object

<img src="image1.jpg" style="width:4.42239in" />

- Should be immutable
- <span dir="rtl">ولیو های انتیتی ما هستن ولی چون لاجیک در خودشون دارن براشون یه کلاس جدا می سازیم تا ولیدیت و یا مثلا ترکیبشون با هم روی قواعد خودشون باشه و به اشتباه با ولیو آبجکت های دیگه جمع و یا منها نشن</span>

### Micro/Tiny types

- <span dir="rtl">همون ولیو آبجکت هایی هستن که هیچ لاجیکی نداره و صرفا برای افزایش خوانایی کد اضافه میشن، البته در گذر زمان و اضافه شدن لاجیک به این آبجکت ها از نظر منطقی به ولیو آبجکت تغییر میکنند</span>

### Invariants

- <span dir="rtl">به معنای ثابت، ولیدیشن هایی هستند که در طول زمان به هیچ عنوان تغییر نخواهند یافت</span>

### Behaviour

- <span dir="rtl">فانکشن هایی که در خود انتیتی قرار میگیرن و تغییری در دیتای آن انتیتی انجام میدهند، و طبق این گفتار پس ست کردن مستقیم در انتیتی معنا ندارد</span>

### Event

<img src="image11.jpg" />

Where to fire the event? In Application service. Domain layer should not know about how to fire the event.

- <span dir="rtl">سر یک واقعه خاص ریز می‌شود و هرکی خواست کشش می‌کنه و بسته به اون دیتای خودشو آپدیت می‌کنه</span>
- <span dir="rtl">در دل domain ساخته میشوند اما در دل application service ریز میشوند، چون ارتباط با لایه دیتا به وسیله application service انجام میشه و در صورت بروز خطا تو این لایه نباید event ریز بشه</span>

### Repository

- <span dir="rtl">یک لایه ای است که وظیفه گت و ست دیتا در بخش persist data به وسیله زبان دامین را داراست</span>
- <span dir="rtl">فهم خودم: توش از orm استفاده میشه ولی اسم فانکشن هاش با زبان دامنه تعیین میشه</span>

### Audit log

- <span dir="rtl">فیلدهایی مثل زمان ساخت و زمان آپدیت عناوینی کاملا فنی هستند و به لایه بیزینس بی ربط، لذا این فیلدها به هیچ وجه نباید در انتیتی قرار بگیرند و در صورت نیاز تنها در data access layer ذخیره و در همانجا میمانند و به هیچ عنوان بالاتر نخواهند آمد و تنها در صورت نیاز فنی به آنها مراجعه خواهد شد</span>
- <span dir="rtl">حال سوال این است که در مفهوم ساخت خبر فیلد پابلیش شدن خبر جزو بیزینس است، چه کنیم؟ پاسخ این است که بجز فیلد زمان ساخت که بنا شد در انتیتی نباشد یک پراپرتی زمان پابلیش در انتیتی که به زبان بیزینس است داخل انتیتی قرار می‌دهیم</span>

### Event sourcing

- <span dir="rtl">برای هر اگریگیتی که نیاز شد هیستوریشو داشته باشیم از این روش استفاده میکنیم، به این معنی که بجای ذخیره سازی وضعیت نهایی آن (مثلا موجودی حساب) تمامی وقایع رو جدا ذخیره و در زمان واکشی دیتا از روی تمامی وقایع به وضعیت فعلی آن خواهیم رسید، ممکنه بگیم یه انتیتی ممکنه ده سال عوض شده باشه خوندن ده سال وقایع زمان بره به همین خاطر از اسنپ‌شات استفاده میکنیم (بعضی از دیتابیس‌ها خودشون به راحتی event sourcing رو هندل کردن)</span>

## Services

### Domain Service

<img src="image7.jpg" style="width:4.81342in" />

### Application Service

Can handle validations, data mappings, transaction management and security

<img src="image9.jpg" />

### Domain vs Application

Domain services hold domain logic whereas application services don't

## Sample Project Architecture

<img src="image6.jpg" />

<img src="image4.png" />

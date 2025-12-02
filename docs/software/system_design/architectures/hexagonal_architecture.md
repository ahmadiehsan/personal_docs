# Hexagonal Architecture

## Description

<img src="image1.png" style="width:4.2in" />

Facts:

- Invented in 2005 by Alistair Cockburn
- it's an alternative name for the original name "Ports & Adapters"
- There are no layers. You have the application, the ports, and the adapters. The ports belong to the application, they are the API/SPI of the application. Adapters are outside the application, and each one depends on the port of the application.
- Says nothing about the structure of the inside of the hexagon (the application)
- Separate the project into two parts, inside and outside

!!! info

    <span dir="rtl">اولین بار ایده این که با جداسازی هسته از کتابخانه ها و فریم ورک ها (به وسیله dependency inversion) میتونیم پروژه استیبل با امکان تست پذیری خوبی رو داشته باشیم رو مطرح کرد ولی اطلاعات خاصی درباره هسته نداد، بعدها رابرت سی مارتین اومد این ایده رو گسترش داد و یه مقداری درباره هسته هم صحبت کرد.</span>

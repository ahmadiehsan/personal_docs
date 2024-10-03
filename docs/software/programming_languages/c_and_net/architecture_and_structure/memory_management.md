# Memory Management

## Schema

<img src="image5.jpg" style="width:4.69167in" />

## Stack

- Part of ram
- Very fast
- Last in, first out
- All the local variables will store in here
- Reference of one obj will store here

## Heap (a.k.a Virtual Memory)

Key Points:

- Part of ram
- Slower than stack
- All the objects will store here
- Has 64 MB space

Generation:

![](memory_management/image6.jpg)

- <span dir="rtl">اول موقع ساخت</span> <span dir="ltr">object</span> <span dir="rtl">اون آبجکت داخل</span> <span dir="ltr">G</span><span dir="rtl">0 ساخته میشه، بعد از یه مدتی منتقل میشه به</span> <span dir="ltr">G</span><span dir="rtl">1 و بعدش هم به</span> <span dir="ltr">G</span><span dir="rtl">2</span>

<img src="image1.jpg" style="width:4.175in" />

<img src="image2.jpg" style="width:4.26667in" />

<img src="image3.jpg" style="width:4.2125in" />

## Garbage Collector (GC)

Description:

![](memory_management/image8.jpg)

GC Trigger:

<img src="image9.jpg" style="width:5.39167in" />

Tips:

![](memory_management/image7.jpg)

## Managed vs Unmanaged Resources

![](memory_management/image4.jpg)

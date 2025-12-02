# Command (Encapsulated request object) [Behavioral]

## Description

<img src="image1.jpg" />

<img src="image2.jpg" style="width:4in" />

The Command Pattern allows you to decouple the requester of an action from the object that acts.

<img src="image3.jpg" />

!!! info

    <span dir="rtl">خیلی مناسبه اینه که اکشن های سیستم رو حفظ و نگهداری کرد و ازشون برای کارهای مختلفی مثل آندو کردن یه اکشن یا بازیابی سیستم بعد از کرش کردن استفاده کرد</span>

## MacroCommands

MacroCommands are a simple extension of the Command Pattern that allows multiple commands to be invoked.
Likewise, MacroCommands can easily support undo().

## Transactional systems

Command patterns may also be used to implement logging and transactional systems.

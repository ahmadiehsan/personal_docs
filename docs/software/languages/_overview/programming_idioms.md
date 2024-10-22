# Programming Idioms

## Language Structure

- **Expression:** Evaluates to a value

  ```python
  >>> 23
  23
  >>> 23l
  23L
  >>> range(4)
  [0, 1, 2, 3]
  >>> 2L*bin(2)
  '0b100b10'
  >>> def func(a):        # Statement, just part of the example...
  ...     return a*a      # Statement...
  ...
  >>> func(3)*4
  36
  >>> func(5) is func(a=5)
  True
  ```

- **Statement:** Do Something and are often composed of expressions (or other statements)

  ```python
  >>> x + 2                # an expression
  >>> x = 1                # a statement
  >>> y = x + 1            # a statement
  >>> print y              # a statement (in 2.x)
  2
  ```

## Principles

- **EAFP:** Easier to ask for forgiveness than permission (try/except)
- **LBYL:** Look Before You Leap (if/else)

## Functions

- <span dir="rtl">**Closure:** به معنی بسته، وقتی که یه فانکشن داخل یک فانکشن مادر هستش و متغیر های مادرشو یادش میمونه با این که اسکوپ فانکشن مادرش تموم شده.</span>
- <span dir="rtl">**Procedure:** به معنی روش، وقتی یه فانکشن چیزی ریترن نمیکنه بهش میگن، مثل فانکشن پرینت در پایتون.</span>

## OOP

- <span dir="rtl">**Cohesion:** به معنی انسجام، زمانی که متد های یک کلاس به هم مربوط باشند و در آن متد بی ربط که اصل سینگل ریسپانسیبیلیتی را زیر سوال نبرد وجود نداشته باشد میگویند آن کلاس کوهیژن بالایی دارد.</span>
- <span dir="rtl">**POCO (Plain Old Class Object):** کلاس های ساده ای که برای استفاده در دل یک فریمورک یا کتابخانه خاصی آماده نشده اند (مثلا دکوریتور یا اتربیوت خاصی</span>
- <span dir="ltr">**Fluent Interface:** In software engineering, a fluent interface is an object-oriented API whose design relies extensively on method chaining. Its goal is to increase code legibility by creating a domain-specific language (DSL).</span>

## Data Structures

- <span dir="rtl">**FIFO - LIFO:** خلاصه دو کلمه first-in first-out و last-in first-out هستن که نمونه اولی سیستم های صف و نمونه دومی حافظه استک مموری هستش.</span>
- <span dir="rtl">**Stack:** نحوه ذخیره دیتایی که آخرین المنت وارد شده اول خارج می شود.</span>
- <span dir="rtl">**Queue:** نحوه ذخیره دیتایی که اولین المنت وارد شده اول خارج می شود.</span>
- <span dir="rtl">**BFS (breadth-first search):** سرچ افقی یک درخت</span>
- <span dir="rtl">**DFS (depth-first search):** سرچ عمودی در یک درخت</span>

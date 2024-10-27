# DateTime

## Description

The `System.DateTime` is a structure that represents date and time value. (Default format: `yyyy-MM-dd hh:mm:ss.fff tt`)

Creating `DateTime` using `Parse` method:

```csharp
DateTime.Parse("2025-12-31 11:59:59.999 PM")
```

Creating `DateTime` using `ToDateTime` method:

```csharp
Convert.ToDateTime("2025-12-31 11:59:59.999 PM")
```

| DateTime | Value |
|----------|-------|
| `yyyy`   | 2025  |
| `MM`     | 12    |
| `dd`     | 31    |
| `hh`     | 11    |
| `HH`     | 23    |
| `mm`     | 59    |
| `ss`     | 59    |
| `fff`    | 999   |
| `tt`     | PM    |

## Features

### Constructor

| Signature                                                                                   | Description                                                                                                                                   |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `DateTime(int year, int month, int day, int hour, int minute, int second, int millisecond)` | Creates a new instance (structure instance) with the specified date and time values. The "hour" should specified in 24-hour format (0 to 23). |

### Properties

| Property                       | Description                                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------------------|
| `int Day { get; }`             | It returns the day (1 to 31) of the current date & time value.                                       |
| `int Month { get; }`           | It returns the month (1 to 12) of the current date & time value.                                     |
| `int Year { get; }`            | It returns the year (1 to 9999) of the current date & time value.                                    |
| `int Hour { get; }`            | It returns the hour (0 to 23) of the current date & time value.                                      |
| `int Minute { get; }`          | It returns the minute (0 to 59) of the current date & time value.                                    |
| `int Second { get; }`          | It returns the second (0 to 59) of the current date & time value.                                    |
| `int Millisecond { get; }`     | It returns the millisecond (0 to 999) of the current date & time value.                              |
| `int DayOfYear { get; }`       | It returns the day of the year (1 to 366) based on the current date & time value.                    |
| `DayOfWeek DayOfWeek { get; }` | It returns the day of the week - Sunday to Saturday (0 to 6) based on the current date & time value. |
| `static DateTime Now { get; }` | It returns an instance of the DateTime structure that represents the current system date & time.     |

### Methods

| Method                                        | Description                                                                                                                                      |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `string ToString()`                           | It returns the date & time value in the default date format, based on current Windows settings.                                                  |
| `string ToString(string format)`              | It returns the date & time value in the specified format.                                                                                        |
| `string ToShortDateString()`                  | It returns the date value in the default short date format, based on current Windows settings. **Eg:** MM/dd/yyyy (12/31/2030)                   |
| `string ToLongDateString()`                   | It returns the date value in the default long date format, based on current Windows settings. **Eg:** dd MMMM yyyy (31 December 2030)            |
| `string ToShortTimeString()`                  | It returns the date value in the default short time format, based on current Windows settings. **Eg:** hh:mm tt (11:59 PM)                       |
| `string ToLongTimeString()`                   | It returns the date value in the default long time format, based on current Windows settings. **Eg:** hh:mm:ss tt (11:59:59 PM)                  |
| `static int DaysInMonth(int year, int month)` | It returns the number of days in the specified month in the specified year.                                                                      |
| `int CompareTo(DateTime value)`               | It compares this instance to another date. Returns `-1` if earlier, `0` if equal, and `1` if later.                                              |
| `TimeSpan Subtract(DateTime value)`           | It returns an instance of `TimeSpan` structure representing the date difference between the current instance and the given date value.           |
| `DateTime AddDays(double value)`              | It creates and returns a new instance of `DateTime` structure after adding specified days (+ve or -ve) to the current date & time value.         |
| `DateTime AddMonths(double value)`            | It creates and returns a new instance of `DateTime` structure after adding specified months (+ve or -ve) to the current date & time value.       |
| `DateTime AddYears(double value)`             | It creates and returns a new instance of `DateTime` structure after adding specified years (+ve or -ve) to the current date & time value.        |
| `DateTime AddHours(double value)`             | It creates and returns a new instance of `DateTime` structure after adding specified hours (+ve or -ve) to the current date & time value.        |
| `DateTime AddMinutes(double value)`           | It creates and returns a new instance of `DateTime` structure after adding specified minutes (+ve or -ve) to the current date & time value.      |
| `DateTime AddSeconds(double value)`           | It creates and returns a new instance of `DateTime` structure after adding specified seconds (+ve or -ve) to the current date & time value.      |
| `DateTime AddMilliseconds(double value)`      | It creates and returns a new instance of `DateTime` structure after adding specified milliseconds (+ve or -ve) to the current date & time value. |

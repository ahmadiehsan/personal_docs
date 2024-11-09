# Data Types

## Primitive vs Non-Primitive

| **Primitive Types**                                                                      | **Non-Primitive Types**                                 |
|------------------------------------------------------------------------------------------|---------------------------------------------------------|
| (sbyte, byte, short, ushort, int, uint, long, ulong, float, double, decimal, char, bool) | (string, Classes, Interfaces, Structures, Enumerations) |
| Strictly stores single value                                                             | Stores one or more values                               |
| Primitive Types are basic building blocks of non-primitive types                         | Usually contains multiple members                       |

- All primitive types are structures.
- Example: `sbyte` is a primitive type, which is equivalent to `System.SByte` (can also be written as `SByte` structure).
- In C#, it is recommended to always use primitive types instead of structure names.
- Data type are specific to C# but their structure/class are specific to .NET

| Data Type | Structure/Class | Name of Structure/Class | Full Path (with Namespace) |
|-----------|-----------------|-------------------------|----------------------------|
| sbyte     | Structure       | SByte                   | System.SByte               |
| byte      | Structure       | Byte                    | System.Byte                |
| short     | Structure       | Int16                   | System.Int16               |
| ushort    | Structure       | UInt16                  | System.UInt16              |
| int       | Structure       | Int32                   | System.Int32               |
| uint      | Structure       | UInt32                  | System.UInt32              |
| long      | Structure       | Int64                   | System.Int64               |
| ulong     | Structure       | UInt64                  | System.UInt64              |
| float     | Structure       | Single                  | System.Single              |
| double    | Structure       | Double                  | System.Double              |
| decimal   | Structure       | Decimal                 | System.Decimal             |
| char      | Structure       | Char                    | System.Char                |
| bool      | Structure       | Boolean                 | System.Boolean             |
| string    | Class           | String                  | System.String              |

## Reference and Value

### VS

| **Value Types**                                                                                       | **Reference Types**                                                                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| (Structures, Enumerations)                                                                            | (string, Classes, Interfaces, Delegates)                                                                   |
| Mainly meant for storing simple values.                                                               | Mainly meant for storing complex / large amount of values.                                                 |
| Instances (examples) are called as "structure instances" or "enumeration instances".                  | Instances (examples) are called as "Objects" (Class Instances / Interface Instances / Delegate Instances). |
| Instances are stored in **"Stack"**. Every time when a method is called, a new stack will be created. | Instances (objects) are stored in **"heap"**. Heap is only one for entire application.                     |

### Boxing

It is a process of converting a value from "Value-Type Data Type" to "Reference-Type Data Type", if they are compatible data types.

This can be done automatically (no need for any syntax).

```csharp
// primitive variable
int x = 10;

// boxing (value-type to reference-type)
object obj = x;

System.Console.WriteLine(x);   // Output: 10
System.Console.WriteLine(obj); // Output: 10
```

### Unboxing

It is a process of converting a value from "Reference-Type Data Type" to "Value-Type Data Type", if they are compatible data types.

This should be done explicitly (by using explicit casting).

```csharp
// reference type variable
object obj = 10;

// unboxing (reference-type to value-type)
int x = (int)obj;

System.Console.WriteLine(x);   // Output: 10
System.Console.WriteLine(obj); // Output: 10
```

When we aren't sure about the incoming type, we will store it in a variable with object type and after that we will using unboxing for converting it to the proper type

## Types

### Byte

| **Type**             | **sbyte**            | **byte**               |
|----------------------|----------------------|------------------------|
| **Size**             | 1 byte               | 1 byte                 |
| **Range**            | -128 to 127          | 0 to 255               |
| **Type**             | 8-bit signed integer | 8-bit unsigned integer |
| **Default Value**    | 0                    | 0                      |
| **MinValue Command** | sbyte.MinValue       | byte.MinValue          |
| **MaxValue Command** | sbyte.MaxValue       | byte.MaxValue          |

### Short

| **Type**             | **short**             | **ushort**              |
|----------------------|-----------------------|-------------------------|
| **Size**             | 2 bytes               | 2 bytes                 |
| **Range**            | -32,768 to 32,767     | 0 to 65,535             |
| **Type**             | 16-bit signed integer | 16-bit unsigned integer |
| **Default Value**    | 0                     | 0                       |
| **MinValue Command** | short.MinValue        | ushort.MinValue         |
| **MaxValue Command** | short.MaxValue        | ushort.MaxValue         |

### Int

| **Type**             | **int**                                                                                          | **uint**                                                                                         |
|----------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Size**             | 4 bytes                                                                                          | 4 bytes                                                                                          |
| **Range**            | -2,147,483,648 to 2,147,483,647                                                                  | 0 to 4,294,967,295                                                                               |
| **Type**             | 32-bit signed integer                                                                            | 32-bit unsigned integer                                                                          |
| **Default Value**    | 0                                                                                                | 0                                                                                                |
| **MinValue Command** | int.MinValue                                                                                     | uint.MinValue                                                                                    |
| **MaxValue Command** | int.MaxValue                                                                                     | uint.MaxValue                                                                                    |
| **Notes**            | By default, integer literals between -2,147,483,648 and 2,147,483,647 are treated as `int` type. | By default, integer literals between 2,147,483,648 and 4,294,967,295 are treated as `uint` type. |

### Long

| **Type**             | **long**                                                                                                                  | **ulong**                                                                                                                  |
|----------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Size**             | 8 bytes                                                                                                                   | 8 bytes                                                                                                                    |
| **Range**            | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807                                                                   | 0 to 18,446,744,073,709,551,615                                                                                            |
| **Type**             | 64-bit signed integer                                                                                                     | 64-bit unsigned integer                                                                                                    |
| **Default Value**    | 0                                                                                                                         | 0                                                                                                                          |
| **MinValue Command** | long.MinValue                                                                                                             | ulong.MinValue                                                                                                             |
| **MaxValue Command** | long.MaxValue                                                                                                             | ulong.MaxValue                                                                                                             |
| **Notes**            | By default, integer literals between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807 are treated as `long` type. | By default, integer literals between 9,223,372,036,854,775,808 and 18,446,744,073,709,551,615 are treated as `ulong` type. |

### Float

| **Type**             | **float**                                                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Size**             | 4 bytes                                                                                                                                        |
| **Range**            | -3.402823E+38 to 3.402823E+38                                                                                                                  |
| **Range (expanded)** | Minus three hundred forty-two hundred eighty-two three hundred nonillion to three hundred forty-two hundred eighty-two three hundred nonillion |
| **Type**             | 32-bit signed floating-point number                                                                                                            |
| **Precision**        | 7 digits                                                                                                                                       |
| **Default Value**    | 0F                                                                                                                                             |
| **MinValue Command** | float.MinValue                                                                                                                                 |
| **MaxValue Command** | float.MaxValue                                                                                                                                 |

### Double

| **Type**                       | **double**                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Size**                       | 8 bytes                                                                                                                                                                                                                                                                                                                                                                                        |
| **Range**                      | -$1.79769313486232 \times 10^{308}$ to $1.79769313486232 \times 10^{308}$                                                                                                                                                                                                                                                                                                                      |
| **Range (Expanded)**           | MINUS one hundred seventy-nine trillion seven hundred sixty-nine billion three hundred thirteen million four hundred eighty-six thousand two hundred thirty-two UNTRIGINTILLION DUOTRIGINTILLION to one hundred seventy-nine trillion seven hundred sixty-nine billion three hundred thirteen million four hundred eighty-six thousand two hundred thirty-two UNTRIGINTILLION DUOTRIGINTILLION |
| **Precision**                  | 15 digits                                                                                                                                                                                                                                                                                                                                                                                      |
| **Default Value**              | 0D                                                                                                                                                                                                                                                                                                                                                                                             |
| **Min and Max Value Commands** | `double.MinValue`, `double.MaxValue`                                                                                                                                                                                                                                                                                                                                                           |
| **Notes**                      | By default, floating-point literals in the specified range are treated as "double" type.                                                                                                                                                                                                                                                                                                       |

### Decimal

| **Type**                       | **decimal**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Size**                       | 16 bytes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Range**                      | -79228162514264337593543950335 to 79228162514264337593543950335                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Range (Expanded)**           | MINUS seventy-nine octillion two hundred twenty-eight septillion one hundred sixty-two sextillion five hundred fourteen quintillion two hundred sixty-four quadrillion three hundred thirty-seven trillion five hundred ninety-three billion five hundred forty-three million nine hundred fifty thousand three hundred thirty-five to seventy-nine octillion two hundred twenty-eight septillion one hundred sixty-two sextillion five hundred fourteen quintillion two hundred sixty-four quadrillion three hundred thirty-seven trillion five hundred ninety-three billion five hundred forty-three million nine hundred fifty thousand three hundred thirty-five |
| **Precision**                  | 28 digits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Default Value**              | 0M                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Min and Max Value Commands** | `double.MinValue`, `double.MaxValue`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Char

| **Type**           | **char**                                                                        |
|--------------------|---------------------------------------------------------------------------------|
| **Size**           | 2 bytes                                                                         |
| **Range**          | 0 to 137,994 (Unicode codes that represent characters)                          |
| **Type**           | 16-bit Single Unicode character                                                 |
| **ASCII Standard** | ASCII is 0 to 255 (English language characters only)                            |
| **Unicode**        | Unicode is the superset of ASCII and includes other natural language characters |
| **Default Value**  | \0                                                                              |
| **Notes**          | Character literals should be written in single quotes only. Ex: 'A'             |

!!! info

    \\0 means null

Important ASCII/Unicode Numbers for Characters:

- 65 to 90: A-Z
- 97 to 122: a-z
- 48 to 57: 0-9
- 32: Space
- 8: Backspace
- 13: Enter

### String

| **Type**          | **string**                                                            |
|-------------------|-----------------------------------------------------------------------|
| **Size**          | Length $\times$ 2 bytes                                               |
| **Range**         | 0 to 2 billion characters                                             |
| **Type**          | Collection of Unicode characters                                      |
| **Default Value** | null                                                                  |
| **Notes**         | String literals should be written in double quotes only. Ex: "Abc123" |

### Boolean

| **Type**            | **bool**                           |
|---------------------|------------------------------------|
| **Size**            | 1 bit                              |
| **Possible Values** | true, false                        |
| **Default Value**   | false                              |
| **Notes**           | Stores logical values (true/false) |

## Type Conversion

### Classification

Type Conversion is a process of converting a value from one type (source type) to another type (destination type).

- Implicit Casting: from lower-numerical-type to higher-numerical-type
- Explicit Casting: from higher-numerical-type to lower-numerical-type
- Parsing / TryParse: from string to numerical-type
- Conversion Methods: from any-primitive-type to any-primitive-type

### Implicit Casting

| Conversion From | Conversion To                                                 |
|-----------------|---------------------------------------------------------------|
| sbyte           | short, int, long, float, double, decimal                      |
| byte            | short, ushort, int, uint, long, ulong, float, double, decimal |
| short           | int, long, float, double, decimal                             |
| ushort          | int, uint, long, ulong, float, double, decimal                |
| int             | long, float, double, decimal                                  |
| uint            | long, ulong, float, double, decimal                           |
| long            | float, double, decimal                                        |
| ulong           | float, double, decimal                                        |
| float           | double                                                        |
| double          | [none]                                                        |
| decimal         | [none]                                                        |
| char            | ushort, int, uint, long, ulong, float, double, decimal        |
| bool            | [none]                                                        |
| string          | [none]                                                        |

!!! info

    No need to any syntax, compiler will do it for us

### Explicit Casting

| Conversion From | Conversion To                                                              |
|-----------------|----------------------------------------------------------------------------|
| sbyte           | byte, ushort, uint, ulong                                                  |
| byte            | sbyte                                                                      |
| short           | sbyte, byte, ushort, uint, ulong                                           |
| ushort          | sbyte, byte, short                                                         |
| int             | sbyte, byte, short, ushort, uint, ulong                                    |
| uint            | sbyte, byte, short, ushort, int                                            |
| long            | sbyte, byte, short, ushort, int, uint, ulong                               |
| ulong           | sbyte, byte, short, ushort, int, uint, long                                |
| float           | sbyte, byte, short, ushort, int, uint, long, ulong, decimal                |
| double          | sbyte, byte, short, ushort, int, uint, long, ulong, float, decimal         |
| decimal         | sbyte, byte, short, ushort, int, uint, long, ulong, float, double          |
| char            | sbyte, byte, short, ushort, int, uint, long, ulong, float, double, decimal |
| bool            | [none]                                                                     |
| string          | [none]                                                                     |

!!! warning

    If the destination type is not sufficient enough to store the converted value, the value may lose.

```csharp
MyType a = (MyType)myObj;  // throws an exception if type is wrong
MyType a = myObj as MyType;  // return null if type is wrong
```

### Parsing

String to any numerical type

Syntax:

```csharp
DestinationDataType.Parse(SourceValue)
```

### Try Parsing

The string value can be converted into any numerical data type, by using the "TryParse" technique (same as "parse"); but it checks the source value before attempting to parse.

- If the source value is invalid, it returns `false`; It doesn't raise any exception in this case.
- If the source value is valid, it returns `true` (indicates conversion is successful).
- It avoids `FormatException`.

Syntax:

```csharp
bool variable = DestinationType.TryParse(SourceValue, out DestinationVariable)
```

### Conversion Methods

Conversion method is a pre-defined method, which converts any primitive type (and also "string") to any other primitive type (and also "string").

- The `System.Convert` is a class that contains a set of pre-defined methods.
- It raises `FormatException` if the source value is invalid.
- For each data type, we have a conversion method.
- All conversion methods are static methods.

Syntax:

```csharp
type destinationVariable = Convert.ConversionMethod(SourceValue)
```

Conversion table:

| **Conversion To** | **Conversion Method**               |
|-------------------|-------------------------------------|
| `sbyte`           | `System.Convert.ToSByte( value )`   |
| `byte`            | `System.Convert.ToByte( value )`    |
| `short`           | `System.Convert.ToInt16( value )`   |
| `ushort`          | `System.Convert.ToUInt16( value )`  |
| `int`             | `System.Convert.ToInt32( value )`   |
| `uint`            | `System.Convert.ToUInt32( value )`  |
| `long`            | `System.Convert.ToInt64( value )`   |
| `ulong`           | `System.Convert.ToUInt64( value )`  |
| `float`           | `System.Convert.ToSingle( value )`  |
| `double`          | `System.Convert.ToDouble( value )`  |
| `decimal`         | `System.Convert.ToDecimal( value )` |
| `char`            | `System.Convert.ToChar( value )`    |
| `string`          | `System.Convert.ToString( value )`  |
| `bool`            | `System.Convert.ToBoolean( value )` |

## System.Object

The "System.Object" is a pre-defined class, which is the "Ultimate super class (base class)" in .NET.

All the classes and other types are inherited from System.Object directly or indirectly.

Class hierarchy:

```text
class System.Object
├── class System.ValueType
│   ├── Structures
│   └── Enumerations
├── Classes
└── Interfaces
```

Code definition:

```csharp
namespace System
{
    class Object
    {
        virtual bool Equals( object value );
        virtual int GetHashCode( );
        Type GetType( );
        virtual string ToString( );
    }
}
```

Class methods:

- `bool Equals( object value )`

   - Compares the current object with the given argument object; returns true if both are the same objects; returns false if both are different objects.

- `int GetHashCode( object value )`

   - Returns a number that represents the object. It is not guaranteed that the hash code is unique, by default.

- `Type GetType( )`

   - Returns the name of the class (including namespace path), based on which the object is created.

- `string ToString( )`

   - By default, it returns the name of the class (including namespace path), based on which the object is created.
   - It is a virtual method, which can be overridden in the child class.

## Nullable Type

| **Value Types**                                                                 | **Reference Types**                                             |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------|
| *(structures, enumerations)*                                                    | *(classes, interfaces)*                                         |
| Value Types are by default non-nullable types.                                  | Reference Types are by default nullable types.                  |
| Non-nullable types don't support `null` values to be assigned to its variables. | Nullable types support `null` values assigned to its variables. |
|                                                                                 | They don't require the following syntax.                        |

Converting Value-Types to Nullable-Types example:

```csharp
Nullable<int> x = null;
// or
int? x = null;
```

## Pattern Matching

It allows you to declare a variable while checking the data type (class) of a reference variable, and automatically type-casts the reference variable into the specified data type (class).

The classic way to check data type:

```csharp
if (referenceVariable is Class1) {
    Class1 c1 = (Class1)referenceVariable;
    c1.Property....;
}
```

The Pattern-Matching way to check data type:

```csharp
if (referenceVariable is Class1 c1) {
    c1.Property....;
}
```

## Implicit Typed Variables

The variables that are declared with `var` keyword are called 'implicitly-typed variables' (a.k.a type-inference).

Implicitly-typed variables are declared without specifying the `type` explicitly, so the C# compiler automatically identifies the appropriate data type at compilation-time based on the value assigned at the time of declaration.

Example:

```csharp
var variableName = value;
```

- Is good when the type name is long
- Is good when we don't know the output type (For example the LINQ query result)
- It is not possible to declare multiple implicitly typed variables in the same statement.

  ```csharp
  // Example:
  var x = 10, y = 20;  // error
  ```

- It is not possible to assign `"null"` to implicitly typed variables during declaration.

  ```csharp
  // Example:
  var x = null;  // error
  ```

## Dynamically Typed Variables

Dynamically Typed Variables are the variables that are declared with the `dynamic` keyword.

Example:

```csharp
dynamic variableName = value;
```

- Declared without specifying the type explicitly.
- There is no fixed type for the variable.
- You can assign any type of value to these variables.
- C# compiler skips "type-checking" at compilation time; instead, it resolves the data types of its values at run-time.
- The `dynamic` type variables are converted as `object` type in most cases:

  ```csharp
  dynamic dynamicVariable = 100;  // Equivalent to: object dynamicVariable = 100;
  ```

- The Dynamically Typed Variable can change its data type, any number of times, at run-time.
- Methods and other members of `dynamically typed variables` will not be checked by the compiler at compilation time; it will be checked by the CLR at runtime.

   - If the method or other member is not available, it would not cause a compile-time error; it raises a run-time error when the execution flow encounters that particular statement.

   ```csharp
   dynamicVariable.NonExistingMethod();  // run-time error (exception)
   ```

- The Dynamically Typed Variables need not be initialized while declaring.

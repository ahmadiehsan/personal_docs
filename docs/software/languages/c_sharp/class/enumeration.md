# Enumeration

## Description

**Enumeration** is a collection of constants.

```csharp
enum EnumerationName {
    Constant1,
    Constant2,
    ...
}
```

- Enumeration is used to specify the list of options allowed to be stored in a field/variable.
- Use enumeration if you don't want to allow other developers to assign other value into a field/variable, other than the list of values specified in the enumeration.
- Accessing Members: `EnumerationName.ConstantName`
- By default, each constant will be assigned to a number, starting from zero. However, you can change the number (integer only).

    ```csharp
    enum EnumerationName {
        Constant1 = value, Constant2 = value, ...
    }
    ```

- The default data type of the enum member is `"int"`. However, you can change its data type as follows:

    ```csharp
    enum EnumerationName : datatype {
        Constant1 = value, Constant2 = value, ...
    }
    ```

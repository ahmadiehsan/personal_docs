# Interface

## Description

```csharp
interface InterfaceName
{
    ReturnDataType MethodName(param1, ...);
}

class ChildClassName : InterfaceName
{
    public ReturnDataType MethodName(param1, ...)
    {
    }
}
```

- The child class that implements the interface, **MUST implement ALL METHODS** of the interface.
- Interface methods are by default **"public"** and **"abstract"**.
- The child class must implement all interface methods, with the **same signature**.
- You **can't create an object** for an interface.
- You **can create a reference variable** for the interface.
- The reference variable of interface type can only store the **address of objects** of any one of the corresponding child classes.
- You can implement **multiple interfaces** in the same child class (**Multiple Inheritance**).
- An interface can be a **child of another interface**.
- Interfaces name, should start with capital i
- Interfaces file name, should start with capital i also

## Features

| Feature                                                            | Normal Class | Abstract Class | Interface |
|--------------------------------------------------------------------|--------------|----------------|-----------|
| Non-Static Fields                                                  | Yes          | Yes            | No        |
| Non-Static Methods                                                 | Yes          | Yes            | No        |
| Non-Static Constructors                                            | Yes          | Yes            | No        |
| Non-Static Properties                                              | Yes          | Yes            | No        |
| Non-Static Events                                                  | Yes          | Yes            | Yes       |
| Non-Static Destructors                                             | Yes          | Yes            | No        |
| Constants                                                          | Yes          | Yes            | No        |
| Static Fields                                                      | Yes          | Yes            | No        |
| Static Methods                                                     | Yes          | Yes            | No        |
| Static Constructors                                                | Yes          | Yes            | No        |
| Static Properties                                                  | Yes          | Yes            | No        |
| Static Events                                                      | Yes          | Yes            | No        |
| Virtual Methods                                                    | Yes          | Yes            | No        |
| Abstract Methods                                                   | No           | Yes            | Yes       |
| Non-Static Auto-Impl Properties                                    | Yes          | Yes            | No        |
| Non-Static Indexers                                                | Yes          | Yes            | No        |
| Can have abstract methods                                          |              |                | Yes       |
| Can have setter and getters (properties), but can't implement them |              |                | Yes       |
| Can't have constructors                                            |              |                | Yes       |

## Explicit Implementation

"Explicit Interface Implementation" is used to implement an interface method privately; that means the interface method becomes a "private member" to the child class.

```csharp
interface IVehicle
{
    void Move();
}

interface IFlyingMachine
{
    void Move();
}

class FlyingVehicle : IVehicle, IFlyingMachine
{
    void IVehicle.Move()
    {
        // Implementation of IVehicle's Move method
    }

    void IFlyingMachine.Move()
    {
        // Implementation of IFlyingMachine's Move method
    }
}

// The `FlyingVehicle` class implements both the `IVehicle` and `IFlyingMachine` interfaces.
// The `Move()` method from each interface is implemented **explicitly**, meaning it can only be accessed using an instance of the interface and not directly.
```

!!! info

    - <span dir="rtl">برای زمانی است که یک متد هم نام داخل دو interface وجود داره و ما لازم داریم که حتما implementation های مختلفی برای هر کدام پیاده کنیم</span>
    - <span dir="rtl">در صورتی که یک implementation برای هر دو interface کافی باشد، دیگر نیازی به پیاده سازی آنها به شکل بالا نیست</span>
    - <span dir="rtl">در صورت استفاده از explicit implementation این متد ها همگی به صورت اجباری باید private باشند، اما زبان به طور خودکار امکان صدا زدن public آنها به شکل ذکر شده در interface را به ما میدهد!</span>

## Default Method

Default methods are methods in interfaces with concrete implementation.

These methods are accessible through a reference variable of the interface type.

```csharp
interface interface_name
{
    access_modifier return_type method_name(parameters)
    {
        // method body
    }
}
```

## Popular Predefined Interfaces

### IEquatable

The `System.IEquatable<T>` interface has a method called **Equals**, which determines whether the current object and parameter object are logically equal or not, by comparing data of fields.

- It can be implemented in the class to make the objects comparable.
- It is useful to invoke **List.Contains** method to check whether the object is present in the collection or not.

```csharp
public interface IEquatable<T>
{
    bool Equals(T other);
}
```

### IComparable

The `System.IComparable` interface has a method called `CompareTo`, which determines the order of two objects, i.e., the current object and the parameter object.

- It can be implemented in the class to make the objects sortable.
- It is useful to invoke `List.Sort` method to sort the collection of objects.

```csharp
public interface IComparable
{
    int CompareTo(object obj);
}
```

| Return Value | Meaning                                                                    |
|--------------|----------------------------------------------------------------------------|
| 0            | "this" object and parameter object occur in the same position (unchanged). |
| < 0          | "this" object comes first; parameter object comes next.                    |
| > 0          | parameter object comes first; "this" object comes next.                    |

### IComparer

The `System.Collections.Generic.IComparer` interface has a method called "Compare", which determines the order of two objects i.e. current object and parameter object.

- It can be implemented by a separate class to make the objects sortable.
- It is useful to invoke `List.Sort` method to sort the collection of objects.
- It is an alternative to `IComparable`; useful for classes that don't implement `IComparable`.

```csharp
interface System.Collections.Generic.IComparer
{
    public class ClassName : IComparer<T>
    {
        public int Compare(T x, T y)
        {
            return value;
        }
    }
}
```

| Return Value | Meaning                                                       |
|--------------|---------------------------------------------------------------|
| 0            | both x and y are equal; so will be kept in the same position. |
| < 0          | x comes first; y comes next.                                  |
| > 0          | y comes first; x comes next.                                  |

### IEnumerable

The `IEnumerable` interface represents a group of elements.

- It is the parent interface of all types of collections.
- It is the parent of `ICollection` interface, which is implemented by other interfaces such as `IList`, `IDictionary`, etc.

```csharp
// System.Collections.Generic.IEnumerable<T>
public interface IEnumerable<out T> : IEnumerable
{
    IEnumerator<T> GetEnumerator();
}

// System.Collections.IEnumerable
public interface IEnumerable
{
    IEnumerator GetEnumerator();
}
```

### IEnumerator

The `IEnumerator` interface is meant for readonly and sequential navigation of a group of elements.

- `IEnumerator` is used by `foreach` loop internally.
- `IEnumerable` interface has a method called `GetEnumerator` that returns an instance of `IEnumerator`.
- `IEnumerator` by default starts with the first element; `MoveNext()` method reads the next element; the `Current` property returns the current element based on the current position.

```csharp
// System.Collections.Generic.IEnumerator<T>
public interface IEnumerator<out T> : IDisposable, IEnumerator
{
    T Current { get; }
}

// System.Collections.IEnumerator
public interface IEnumerator
{
    object Current { get; }
    bool MoveNext();
    void Reset();
}
```

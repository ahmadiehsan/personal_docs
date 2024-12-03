# Structure

## Description

Structure is a "type", similar to "class", which can contain fields, methods, parameterized constructors, properties, and events.

- The instance of structure is called as **"structure instance"** or **"structure variable"**; but not called as *'object'*.

   - We can't create object for structure.
   - Objects can be created only based on *'class'*.

- Structure instances are stored in *'stack'*.
- Structure doesn't support *'user-defined parameter-less constructor'* and also destructor.
- Structure can't inherit from other classes or structures.
- Structure can implement one or more interfaces.
- Structure doesn't support virtual and abstract methods.
- Structures are mainly meant for storing small amounts of data (one or very few values).
- Structures are faster than classes, as their instances are stored in *'stack'*.
- Structures are value type but classes are reference type
- Will store in stack
- Is good for one or two fields
- Can inherit from interfaces but can't inherit from other classes or structures

```csharp
struct StructureName {
    // Fields
    // Methods
    // Parameterized Constructors
    // Properties
    // Events
}
```

Example:

```csharp
struct Student
{
    public int studentId;
    public string studentName;

    public string GetStudentName()
    {
        return studentName;
    }
}
```

## Key Points

| Property                          | Normal Class | Abstract Class | Interface | Sealed Class | Static Class | Structure |
|-----------------------------------|--------------|----------------|-----------|--------------|--------------|-----------|
| Can Inherit from Other Classes    | Yes          | Yes            | No        | Yes          | No           | No        |
| Can Inherit from Other Interfaces | Yes          | Yes            | Yes       | Yes          | No           | Yes       |
| Can be Inherited                  | Yes          | Yes            | Yes       | No           | No           | No        |
| Can be Instantiated               | Yes          | No             | No        | Yes          | No           | Yes       |
| Non-Static Fields                 | Yes          | Yes            | No        | Yes          | No           | Yes       |
| Non-Static Methods                | Yes          | Yes            | No        | Yes          | No           | Yes       |
| Non-Static Constructors           | Yes          | Yes            | No        | Yes          | No           | Yes       |
| Non-Static Properties             | Yes          | Yes            | No        | Yes          | No           | Yes       |
| Non-Static Events                 | Yes          | Yes            | Yes       | Yes          | No           | Yes       |
| Non-Static Destructors            | Yes          | Yes            | No        | Yes          | No           | No        |
| Constants                         | Yes          | Yes            | No        | Yes          | Yes          | Yes       |
| Static Fields                     | Yes          | Yes            | No        | Yes          | Yes          | Yes       |
| Static Methods                    | Yes          | Yes            | No        | Yes          | Yes          | Yes       |
| Static Constructors               | Yes          | Yes            | No        | Yes          | Yes          | Yes       |
| Static Properties                 | Yes          | Yes            | No        | Yes          | Yes          | Yes       |
| Static Events                     | Yes          | Yes            | No        | Yes          | No           | No        |
| Virtual Methods                   | Yes          | Yes            | No        | Yes          | No           | No        |
| Abstract Methods                  | No           | Yes            | Yes       | Yes          | No           | No        |
| Non-Static Auto-Impl Properties   | Yes          | Yes            | No        | Yes          | No           | No        |
| Non-Static Indexers               | Yes          | Yes            | No        | Yes          | No           | Yes       |

## Structures vs Classes

| Structures                                                                                                      | Classes                                                                                         |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Structures are "value-types".                                                                                   | Classes are "reference-types".                                                                  |
| Structure instances (includes fields) are stored in stack. Structures doesn't require Heap.                     | Class instances (objects) are stored in Heap; Class reference variables are stored in stack.    |
| Suitable to store small data (only one or two values).                                                          | Suitable to store large data (any no. of values).                                               |
| Memory allocation and de-allocation is faster, in case of one or two values.                                    | Memory allocation and de-allocation is a bit slower.                                            |
| Structures doesn't support Parameter-less constructor.                                                          | Classes support Parameter-less Constructor.                                                     |
| Structures doesn't support inheritance (can't be parent or child).                                              | Classes support Inheritance.                                                                    |
| The "new" keyword just initializes all fields of the "structure instance".                                      | The "new" keyword creates a new object.                                                         |
| Structures doesn't support abstract methods and virtual methods.                                                | Classes support abstract methods and virtual methods.                                           |
| Structures doesn't support destructors.                                                                         | Classes support destructors.                                                                    |
| Structures are internally derived from System.ValueType <br> `System.Object -> System.ValueType -> Structures`. | Classes are internally and directly derived from System.Object <br> `System.Object -> Classes`. |
| Structures doesn't support to initialize "non-static fields", in declaration.                                   | Classes support to initialize "non-static fields", in declaration.                              |
| Structures doesn't support "protected" and "protected internal" access modifiers.                               | Classes support "protected" and "protected internal" access modifiers.                          |
| Structure instances doesn't support to assign "null".                                                           | Class's reference variables support to assign "null".                                           |

## Constructor

C# provides a parameter-less constructor for every structure by default, which initializes all fields.

- You can also create one or more user-defined parameterized constructors in structure.
- Each parameterized constructor must initialize all fields; otherwise, it will be compile-time error.
- The “new” keyword used with structure doesn't create any object / allocate any memory in heap; It is just a syntax to call constructor of structure.

```csharp
public StructureName( datatype parameter )
{
    field = parameter;
}
```

!!! info

    <span dir="rtl">بدون استفاده از constructor اصلا نیازی به instantiate کردن و استفاده از کلیدواژه new نیست، مثل زیر:</span>

    ```csharp
    Structure1 structure1;

    structure1.x = 10;
    structure1.y = 20;
    ```

## Readonly Structure

Use readonly structures in case of all of these:

- All fields are readonly.
- All properties have only 'get' accessors (readonly properties).
- There is a parameterized constructor that initializes all the fields.
- You don't want to allow changes to any field or property of the structure.
- Methods can read fields but can't modify them.

Example:

```csharp
readonly struct Student
{
    public readonly int studentId;
    public string studentName { get; }

    public Student()
    {
        studentId = 1;
        studentName = "Scott";
    }
}
```

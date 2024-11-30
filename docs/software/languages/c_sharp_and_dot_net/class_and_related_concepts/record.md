# Record

## Description

Concise syntax to create a reference-type with immutable properties.

- Is a shortcut for creating immutable classes
- Records are 'immutable' by default (All the record members become as 'init-only' properties).
- Records can also be partially / fully mutable - by adding mutable properties.
- Supports value-based equality.
- Supports inheritance.
- Supports non-destructive mutation using 'with' expression.
- A record CAN inherit from another record.
- A record CAN'T inherit from another class.
- A class CAN'T inherit from another record.
- A record CAN implement (inherit) one or more interfaces.
- A record CAN be 'abstract' and 'sealed'.

```csharp
// Record declaration
record record_name(data_type Property1, data_type Property2, ...);

// Compiled code of Record
class record_name {
    public data_type Property1 { get; init; }
    public data_type Property2 { get; init; }

    public record_name(data_type Parameter1, data_type Parameter2)
    {
        this.Property1 = Parameter1;
        this.Property2 = Parameter2;
    }
}
```

## Features

### Mutable Properties

```csharp
record record_name(data_type Property_name, ...) {
    data_type Property_name { get; set; }
}
```

### Equality

Records provide a compiler-generated `Equals()` method and overloads `==` and `!=` operators that compare two instances of records that compare the **values** of fields (but doesn't compare references).

```csharp
record_name variable1 = new record_name(value1, value2);
record_name variable2 = new record_name(value1, value2);

variable1 == variable2;       // true
variable1.Equals(variable2);  // true
```

### Inheritance

```csharp
public record Parent_record_name(Properties_list);

public record Child_record_name(Properties_list) : Parent_record_name;
```

Example:

```csharp
public record Employee(string? Name, DateTime? DateOfBirth, int? Age, double? Salary): Person(Name, DateOfBirth, Age);
```

### Nested Record

```csharp
public record Person(string Name, int Age, Address PersonAddress);

public record Address(string City);
```

### Deconstruction

Records by default supports deconstruction

```csharp
Person person1 = new Person("John", 20, new Address("London", "UK"));
var (name, _, (city, country)) = person1;
```

## Record Struct

Record struct:

```csharp
record struct record_name(Properties_list);
```

- A **record struct** is a 'struct' internally (after compilation).
- All positional parameters of a **record struct** are read-write properties by default.

Record or record class:

```csharp
record record_name(Properties_list);
```

- A **record** is a class internally (after compilation).
- All positional parameters of a **record** are init-only properties by default.

Readonly record struct:

```csharp
readonly record struct record_name(Properties_list);
```

- A **readonly record struct** is a 'struct' internally (after compilation).
- All positional parameters of a **readonly record struct** are init-only properties by default.

## Record vs Record Struct

- The property of **normal records** are by default **init only**
- The property of **readonly record** structs are by default **init only**
- The property of **normal record structs** by default **has setter and getter**

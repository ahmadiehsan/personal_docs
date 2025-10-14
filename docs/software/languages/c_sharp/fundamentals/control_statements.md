# Control Statements

## Overview

- **Conditional Control Statements**

    - if (simple-if, if-else, else-if, nested-if)
    - switch-case

- **Looping Control Statements**

    - while
    - do-while
    - for

- **Jumping Control Statements**

    - goto
    - break
    - continue

## Switch-Case

Normal:

```csharp
switch (variable) {
    case value1: statement1;     break;
    case value2: statement2;     break;
    case value3: statement3;     break;
    ...
    default:     statement;      break;
}
```

With Type Casting:

```csharp
switch (variable) {
    case class_name another_variable:
        statements...; break;
}
```

```csharp
switch (variable) {
    case class_name another_variable
        when another_variable.property == value:
            statements...; break;
}
```

## Switch Expression

Switch Expression is a short-form of "switch-case", which is used to check the value of the source variable; assign value into result value based on the value of source variable.

```csharp
sourceVariable switch {
    value1 => result1,
    value2 => result2,
    ...
    _ => defaultResult
}
```

Normal:

```csharp
int operation = 1; //1 to 4
string result;

//switch expression
result = operation switch {
    1 => "Customer",
    2 => "Employee",
    3 => "Supplier",
    4 => "Distributor",
    _ => "No case available",
};

Console.WriteLine(result);
```

With Type Casting & When Pattern:

```csharp
variable switch {
    class_name another_variable
    when another_variable.property == value
    => statements...
}
```

```csharp
string result = person switch {
    Customer p when p.Age < 13 => $"{p.Name} is Child",
    Person p when p.Age < 20 && p.Age >= 13 => $"{p.Name} is a Teenager",
    Person p when p.Age >= 20 && p.Age < 60 => $"{p.Name} is Adult",
    Person p when p.Age >= 60 => $"{p.Name} is a senior citizen",
    _ => $"{person.Name} is a person"
};
```

With Type Casting & Property Pattern:

```csharp
//Check whether the variable is of specified 'class_name' type
variable switch {
    class_name another_variable when
    {
        { property: value }        //another_variable.property == expression
        { property: < value }      //another_variable.property < value
        { property: > value }      //another_variable.property > value
        { property: <= value }     //another_variable.property <= value
        { property: >= value }     //another_variable.property >= value
    }
    => result_expression...
}
```

```csharp
return person switch {
    Person { Gender: "Female", PersonMaritalStatus: MaritalStatus.Unmarried } => $"Miss. {person.Name}",
    Person { Gender: "Female", PersonMaritalStatus: MaritalStatus.Married } => $"Mrs. {person.Name}",
    Person { Gender: "Male", Age: < 18 } => $"Master. {person.Name}",
    Person { Gender: "Male", Age: >= 18 } => $"Mr. {person.Name}",
    Person { Gender: not ("Male" or "Female") } => $"Mx. {person.Name}",
    _ => $"{person.Name}"
};
```

Nested property pattern:

```csharp
{ outer_property: { nested_property: > value } }
```

Extended property pattern:

```csharp
{ outer_property.nested_property: > value }
```

With Type Casting & Tuple Pattern:

```csharp
(variable.property1, variable.property2) switch {
  (expression1, expression2)   // variable.property1 == expression1 && variable.property2 == expression2
    => result_expression...,

  (expression1, expression2)   // variable.property1 == expression1 && variable.property2 == expression2
    => result_expression...
}
```

```csharp
return (person, person.Gender, person.Age, person.PersonMaritalStatus) switch {
  (Person, "Female", _, MaritalStatus.Unmarried) => $"Miss. {person.Name}",
  (Person, "Female", _, MaritalStatus.Married) => $"Mrs. {person.Name}",
  (Person, "Male", < 18, _) => $"Master. {person.Name}",
  (Person, "Male", >= 18, _) => $"Mr. {person.Name}",
  (Person, not ("Male" or "Female"), _, _) => $"Mx. {person.Name}",
  _ => $"{person.Name}"
};
```

## Loops

For:

```csharp
for (initialization; condition; incrementation) {
    // for block
}
```

Do-While:

```csharp
initialization;
do {
    // do-while block
    // incr / decr here
} while (condition);
```

Foreach:

```csharp
foreach (DataType iterationVariable in arrayVariable) {
    iterationVariable;
}
```

| Pros                                    | Cons                                                                             |
| --------------------------------------- | -------------------------------------------------------------------------------- |
| Simplified Syntax                       | Slower performance, due to it treating everything as a collection                |
| Easy to use with arrays and collections | It can't be used to execute repeatedly without arrays or collections             |
| It internally uses "Iterators"          | It can't read part of an array/collection, or read arrays/collections in reverse |

## Goto

- Used to jump to a specific label.
- You must create a label with some specific name.
- The label can be present at the top of a `goto` statement or at the bottom, but it should be in the same method.

```csharp
statement1;
statement2;

labelname:

statement3;
statement4;

goto labelname;
```

Example:

```csharp
System.Console.WriteLine("one");
System.Console.WriteLine("two");

mylabel:
System.Console.WriteLine("three");
System.Console.WriteLine("four");

goto mylabel;
System.Console.WriteLine("five");
```

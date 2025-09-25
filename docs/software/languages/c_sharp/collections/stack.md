# Stack

## Description

Stack collection contains a group of elements based on **LIFO (Last-In-First-Out)** based collection.

```csharp
Stack<T> referenceVariable = new Stack<T>();
```

- Full Path: `System.Collections.Generic.Stack`
- It is based on LIFO (Last-In-First-Out).
- The `Stack` class is a generic class, requiring specification of the data type of elements when creating an object.
- You cannot access elements based on index.
- It is not index-based. You need to access elements by using `Pop`, `Peek`, and `foreach` loop.

Example:

```csharp
Stack<Student> marks = new Stack<Student>();

foreach (Student item in marks) {
    Console.WriteLine(item.Marks);
}
```

## Features

=== "Overview"

    | Feature       | Description                                                      |
    | ------------- | ---------------------------------------------------------------- |
    | `Count`       | Returns the count of elements in the stack.                      |
    | `Push(T)`     | Adds an element at the top of the stack.                         |
    | `Pop()`       | Removes and returns the element at the top of the stack.         |
    | `Peek()`      | Returns the element at the top of the stack without removing it. |
    | `Contains(T)` | Determines whether the specified element exists in the stack.    |
    | `ToArray()`   | Converts the stack into an array.                                |
    | `Clear()`     | Removes all elements from the stack.                             |

    !!! info

        All the shared features can be used for Stack

=== "Push"

    Is used to add an object to the top of the stack.

    Example:

    ```csharp
    marks.Push(new Student() { Marks = 45 });
    marks.Push(new Student() { Marks = 61 });
    marks.Push(new Student() { Marks = 80 });
    ```

=== "Pop"

    Is used to remove and return the object at the top of the stack.
    It modifies the stack by removing the top-most element.

    - Will remove the returned element.
    - If the stack is empty, it throws an `InvalidOperationException`.

    Example:

    ```csharp
    Student stu = marks.Pop();
    Console.WriteLine("Pop: " + stu.Marks);
    ```

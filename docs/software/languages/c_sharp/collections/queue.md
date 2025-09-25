# Queue

## Description

Queue collection contains a group of elements based on **FIFO** (First-In-First-Out) principle.

```csharp
Queue<T> referenceVariable = new Queue<T>();
```

- Full Path: `System.Collections.Generic.Queue`
- Elements are stored in a front-to-rear approach: Firstly-added item is at front, lastly-added item is at rear.
- It is based on FIFO (First-In-First-Out) principle.
- The `Queue` class is a generic class.
- Elements cannot be accessed by index.

Example:

```csharp
Queue<string> queue = new Queue<string>();

foreach (string item in queue) {
    Console.WriteLine(item); // Task 3, Task 5, ...
}
```

## Features

=== "Overview"

    | Feature       | Description                                              |
    | ------------- | -------------------------------------------------------- |
    | `Count`       | Returns count of elements.                               |
    | `Enqueue(T)`  | Adds an element at the top of the queue.                 |
    | `Dequeue()`   | Removes and returns the element at the top of the queue. |
    | `Peek()`      | Returns the element at the top of the queue.             |
    | `Contains(T)` | Determines whether the specified element exists.         |
    | `ToArray()`   | Converts the queue as an array.                          |
    | `Clear()`     | Removes all elements.                                    |

    !!! info

        All the shared features can be used for Queue

=== "Enqueue"

    Is used to add elements to the end of a `Queue<T>` collection.
    The `Enqueue` method ensures that elements are added at the end of the queue.

    Example:

    ```csharp
    queue.Enqueue("Task 3");
    queue.Enqueue("Task 5");
    queue.Enqueue("Task 1");
    queue.Enqueue("Task 2");
    ```

=== "Dequeue"

    Is used to remove and return the object at the beginning of the queue.
    When the method is called, it removes the item at the front of the queue and shifts all subsequent items forward.

    - Will remove the returned element.
    - If the queue is empty and you attempt to call `Dequeue`, an `InvalidOperationException` is thrown.

    Example:

    ```csharp
    string dq = queue.Dequeue();
    Console.WriteLine("Dequeue: " + dq);
    ```

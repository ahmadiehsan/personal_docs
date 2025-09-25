# List

## Description

List collection contains a group of elements of the same type.

```csharp
List<type> referenceVariable = new List<type>();
```

- Full Path: `System.Collections.Generic.List`
- The `List` class is a generic class; you need to specify the data type of value while creating an object.
- Will use array in its underlying layer
- It is dynamically sized. You can add, remove elements at any time.
- It allows duplicate values.
- It is index-based. You need to access elements by using a zero-based index.
- It is not sorted by default. The elements are stored in the same order they are initialized.
- It uses arrays internally; that means, it recreates the array when elements are added/removed.
- The **'Capacity' property** holds the number of elements that can be stored in the internal array of the List. If you add more elements, the internal array will resize to the **'Count' of elements**.

## Features

=== "Overview"

    | **Feature**                        | **Description**                                                                 |
    | ---------------------------------- | ------------------------------------------------------------------------------- |
    | `Count`                            | Gets the number of elements contained in the list.                              |
    | `Capacity`                         | Gets or sets the total number of elements the internal data structure can hold. |
    | `Add(T)`                           | Adds an element to the end of the list.                                         |
    | `AddRange(IEnumerable<T>)`         | Adds elements from a collection to the end of the list.                         |
    | `Insert(int, T)`                   | Inserts an element at the specified index.                                      |
    | `InsertRange(int, IEnumerable<T>)` | Inserts elements from a collection starting at the specified index.             |
    | `Remove(T)`                        | Removes the first occurrence of a specific element.                             |
    | `RemoveAt(int)`                    | Removes the element at the specified index.                                     |
    | `RemoveRange(int, int)`            | Removes a range of elements starting at a specific index.                       |
    | `RemoveAll(Predicate<T>)`          | Removes all elements that match the conditions defined by a predicate.          |
    | `Clear()`                          | Removes all elements from the list.                                             |
    | `IndexOf(T)`                       | Searches for an element and returns its first index.                            |
    | `BinarySearch(T)`                  | Searches for an element using binary search and returns its index.              |
    | `Contains(T)`                      | Determines whether an element is in the list.                                   |
    | `Sort()`                           | Sorts the elements in the list in ascending order.                              |
    | `Reverse()`                        | Reverses the order of the elements in the list.                                 |
    | `ToArray()`                        | Copies the elements of the list to a new array.                                 |
    | `ForEach(Action<T>)`               | Performs the specified action on each element in the list.                      |
    | `Exists(Predicate<T>)`             | Determines whether an element satisfies the conditions of a predicate.          |
    | `Find(Predicate<T>)`               | Searches for an element that matches a predicate and returns the first match.   |
    | `FindIndex(Predicate<T>)`          | Returns the index of the first element that matches a predicate.                |
    | `FindLast(Predicate<T>)`           | Searches for an element that matches a predicate and returns the last match.    |
    | `FindLastIndex(Predicate<T>)`      | Returns the index of the last element that matches a predicate.                 |
    | `FindAll(Predicate<T>)`            | Returns all elements that match the conditions of a predicate.                  |
    | `ConvertAll(T)`                    | Converts the elements of the list to another type using a converter function.   |

    !!! info

        All the shared features can be used for List

=== "Capacity"

    We can set List capacity (underlying Array capacity) like the below, List class will not create a new array for new items until its capacity, after that will create a new array for each element:

    ```csharp
    new List<int>(10) { 10, 20, 30 };
    ```

=== "RemoveAll"

    - This method removes all the elements that are matching with the given condition.
    - You can write your condition in the lambda expression of Predicate type.

    ```csharp
    void List.RemoveAll(value => condition)
    ```

=== "ForEach"

    This method executes the lambda expression once per each element.

    ```csharp
    void List.ForEach(Action<T>)
    ```

    Example:

    ```csharp
    List.ForEach(n => { Console.WriteLine(n); });
    ```

=== "Exists"

    - This method executes the lambda expression once per each element.
    - It returns true, if at least one element matches with the given condition; but returns false, if no element matches with the given condition.

    ```csharp
    bool List.Exists(Predicate<T>)
    ```

    Example:

    ```csharp
    List.Exists(n => n > 15)
    ```

=== "Find"

    - This method executes the lambda expression once per each element.
    - It returns the first matching element, if at least one element matches with the given condition; but returns the default value, if no element matches with the given condition.

    ```csharp
    T List.Find(Predicate<T>)
    ```

=== "FindIndex"

    - This method executes the lambda expression once per each element.
    - It returns the index of the first matching element, if at least one element matches with the given condition; but returns `-1`, if no element matches with the given condition.

    ```csharp
    int List.FindIndex(Predicate<T>)
    ```

=== "FindLast"

    This method executes the lambda expression once per each element.

    - It returns the last matching element if at least one element matches with the given condition.
    - It returns the default value if no element matches the given condition.

    ```csharp
    T List.FindLast(Predicate<T>)
    ```

=== "FindLastIndex"

    - This method executes the lambda expression once per each element.
    - It returns the index of the last matching element, if at least one element matches with the given condition; but returns -1, if no element matches with the given condition.

    ```csharp
    int List.FindLastIndex(Predicate<T>)
    ```

=== "FindAll"

    - This method executes the lambda expression once per each element.
    - It returns all matching elements as a collection, if there are one or more matching elements; but returns an empty collection if there are no matching elements.

    ```csharp
    List<T> List.FindAll(Predicate<T>)
    ```

=== "ConvertAll"

    - This method executes the lambda expression once per each element.
    - It adds each returned element into a new collection and returns the same at last; thus it converts all elements from the input collection as output collection.

    ```csharp
    List<TOuput> List.ConvertAll(
        Converter<TInput, TOutput>
    )
    ```

    Example:

    ```csharp
    List.ConvertAll(n => Convert.ToDouble(n))
    ```

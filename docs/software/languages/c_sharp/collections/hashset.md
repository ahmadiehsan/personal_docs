# Hashset

## Description

HashSet collection contains a group of elements of unique values stored at respective indexes.

```csharp
HashSet<T> referenceVariable = new HashSet<T>();
```

- Full Path: `System.Collections.Generic.HashSet`
- The `HashSet` class is a generic class.
- You can't set/get the element based on the key/index.
- Searches elements based on the index generated from the search value.
- HashSet allows only one null value, while Hashtable allows only one null key and multiple null values.
- You can't access elements based on key/index (Use the `Contains` method to search for an element).
- You can't sort elements in HashSet.
- Elements must be unique; duplicate elements are not allowed.

Example:

```csharp
HashSet<string> messages = new HashSet<string>()
{
    "Good Morning", "How Are You", "Have a good day"
};

foreach (string message in messages) {
    Console.WriteLine(message);
}
```

## Process of Adding an Element

1. **Generate index** based on the value (Example: `index = hash code % count`)
2. **Add the element (value)** next to the linked list at the generated index.

<img src="image40.jpg" style="width:3in" />

## Features

=== "Overview"

    | **Feature**                          | **Description**                                      |
    | ------------------------------------ | ---------------------------------------------------- |
    | `Count`                              | Returns count of elements.                           |
    | `void Add(T value)`                  | Adds an element (key/value pair).                    |
    | `void Remove(T value)`               | Removes an element based on specified key.           |
    | `void RemoveWhere(Predicate)`        | Removes elements that match a condition.             |
    | `bool Contains(T value)`             | Determines whether the specified value exists.       |
    | `void Clear()`                       | Removes all elements.                                |
    | `void UnionWith(IEnumerable<T>)`     | Unions the hashset and the specified collection.     |
    | `void IntersectWith(IEnumerable<T>)` | Intersects the hashset and the specified collection. |

    !!! info

        All the shared features can be used for HashSet

=== "RemoveWhere"

    It allows remove all elements from the collection that satisfy a specified condition.
    The condition is expressed using a predicate (a function delegate that returns a boolean).

    Example:

    ```csharp
    messages.RemoveWhere(m => m.EndsWith("You"));
    ```

=== "UnionWith"

    Is used to modify the current set to be the union of the current set and a specified collection.
    It adds all unique elements from the provided collection to the `HashSet`, ensuring no duplicates.

    Example:

    ```csharp
    // Create two HashSets
    HashSet<string> employees2021 = new HashSet<string>() { "Amar", "Akhil", "Samareen" };
    HashSet<string> newEmployees2022 = new HashSet<string>() { "John", "Scott", "Smith", "David" };

    // Union
    employees2021.UnionWith(newEmployees2022);
    ```

=== "IntersectWith"

    Is used to modify the current `HashSet<T>` by retaining only the elements that are also present in a specified collection.
    It performs a mathematical set intersection, which means that the resulting set contains only the common elements from both sets.
    This method is useful when narrowing down a collection to shared elements.

    Example:

    ```csharp
    // Create two HashSets
    HashSet<string> employees2021 = new HashSet<string>() { "Amar", "Akhil", "Samareen" };
    HashSet<string> employees2022 = new HashSet<string>() { "John", "Scott", "Amar", "Akhil", "Smith", "David" };

    // Use IntersectWith
    employees2021.IntersectWith(employees2022);
    ```

# SortedList

## Description

SortedList collection contains a group of elements of key/value pairs.

```csharp
SortedList<TKey, TValue> referenceVariable = new SortedList<TKey, TValue>();
```

- Full Path: `System.Collections.Generic.SortedList`.
- The `SortedList` class is a generic class; so you need to specify the data type of the key and the data type of the value while creating the object.
- You can set/get the value based on the key.
- The key can't be null or duplicate.
- It is dynamically sized. You can add, remove elements (key/value pairs) at any time.
- Key can't be null or duplicate, but value can be null or duplicate.
- It is not index-based. You need to access elements by using the key.
- It is sorted by default. The elements are stored in the sorted ascending order, according to the key.
- Each operation of adding an element, removing an element, or any other operation might be slower than a Dictionary, because internally it resorts the data based on the key.
- Will use BinarySearch in the background

## Features

=== "Overview"

    | Feature                      | Description                                    |
    | ---------------------------- | ---------------------------------------------- |
    | `Count`                      | Returns count of elements.                     |
    | `[TKey]`                     | Returns value based on specified key.          |
    | `Keys`                       | Returns a collection of keys (without values). |
    | `Values`                     | Returns a collection of values (without keys). |
    | `void Add(TKey, TValue)`     | Adds an element (key/value pair).              |
    | `bool Remove(TKey)`          | Removes an element based on specified key.     |
    | `bool ContainsKey(TKey)`     | Determines whether the specified key exists.   |
    | `bool ContainsValue(TValue)` | Determines whether the specified value exists. |
    | `int IndexOfKey(TKey)`       | Returns index of the specified key.            |
    | `int IndexOfValue(TValue)`   | Returns index of the specified value.          |
    | `void Clear()`               | Removes all elements.                          |

    !!! info

        All the shared features can be used for SortedList

## VS Dictionary

| Operation | Dictionary             | SortedList                        |
| --------- | ---------------------- | --------------------------------- |
| Insert    | Fast (No need to sort) | Slow (Needs to sort after insert) |
| Search    | Slow (Linear search)   | Fast                              |

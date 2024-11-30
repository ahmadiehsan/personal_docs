# Dictionary

## Description

Dictionary collection contains a group of elements of key/value pairs.

```csharp
Dictionary<TKey, TValue> referenceVariable = new Dictionary<TKey, TValue>();
```

- Full Path: `System.Collections.Generic.Dictionary`.
- The `Dictionary` class is a generic class; so you need to specify the data type of the key and the data type of the value while creating the object.
- You can set/get the value based on the key.
- The key can't be null or duplicate.
- It is dynamically sized. You can add, remove elements (key/value pairs) at any time.
- The key can't be null or duplicate, but values can be null or duplicate.
- It is not index-based. You need to access elements by using key.
- It is not sorted by default. The elements are stored in the same order, exactly how they are initialized.

Example:

```csharp
Dictionary<int, string> employees = new Dictionary<int, string>()
{
    { 101, "Scott" },
    { 102, "Smith" },
    { 103, "Allen" }
};

foreach (KeyValuePair<int, string> item in employees) {
    Console.WriteLine(item.Key + ", " + item.Value);
}
```

## Features

### Overview

| Feature                      | Description                                    |
|------------------------------|------------------------------------------------|
| `Count`                      | Returns count of elements.                     |
| `[TKey]`                     | Returns value based on specified key.          |
| `Keys`                       | Returns a collection of key (without values).  |
| `Values`                     | Returns a collection of values (without keys). |
| `void Add(TKey, TValue)`     | Adds an element (key/value pair).              |
| `bool Remove(TKey)`          | Removes an element based on specified key.     |
| `bool ContainsKey(TKey)`     | Determines whether the specified key exists.   |
| `bool ContainsValue(TValue)` | Determines whether the specified value exists. |
| `void Clear()`               | Removes all elements.                          |

!!! info

    All the shared features can be used for Dictionary

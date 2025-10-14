# Hashtable

## Description

<img src="image15.jpg" style="width:3.5in" />

Hashtable collection contains a group of elements of key/value pairs stored at respective indexes (Full Path: `System.Collections.Hashtable`).

```csharp
Hashtable referenceVariable = new Hashtable();
```

- Process of adding an element:

    1- Generate index based on the key (Ex: `index = hash_code % size_of_hashtable$).
    2- Add the element (key and value) next to the linked list at the generated index.

- GetHashCode method of the key value will be used in the index calculation process
- When we want to use the objs of our custom class as the key inside a hashtable, we should implement the GetHashCode method of that class
- Elements with the same calculated index will be stored in the same index with the linked list data structure
- Each time, when the size of hashtable changes, all the exists indexes will be calculated automatically
- Hashtable will return System.Object instance, because we can store any type of data in Hashtables.
- After retrieving data from hashtable (with `[TKey]` or foreach loop), we should convert the result.
- Hashtable $O(1)$ is faster than SortedList $O(\log n)$ in retrieving data
- Both Hashtable and SortedList have cost in data insert

Example:

```csharp
Hashtable employees = new Hashtable()
{
    { 102, "Smith" },
    { 105, "James" },
    { 103, "Allen" },
    { 101, "Scott" },
    { 104, "Jones" },
    { "hello", 10.934 }
};

foreach (DictionaryEntry item in employees) {
    Console.WriteLine(item.Key + ", " + item.Value);
}
```

## Features

=== "Overview"

    | Feature                              | Description                                    |
    | ------------------------------------ | ---------------------------------------------- |
    | `Count`                              | Returns count of elements.                     |
    | `[TKey]`                             | Returns value based on specified key.          |
    | `Keys`                               | Returns a collection of keys (without values). |
    | `Values`                             | Returns a collection of values (without keys). |
    | `void Add(object key, object value)` | Adds an element (key/value pair).              |
    | `void Remove(object key)`            | Removes an element based on specified key.     |
    | `bool ContainsKey(object key)`       | Determines whether the specified key exists.   |
    | `bool ContainsValue(object value)`   | Determines whether the specified value exists. |
    | `void Clear()`                       | Removes all elements.                          |

    !!! info

        All the shared features can be used for Hashtable

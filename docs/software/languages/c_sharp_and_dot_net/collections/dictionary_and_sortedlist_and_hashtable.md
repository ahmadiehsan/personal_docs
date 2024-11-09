# Dictionary & SortedList & Hashtable

## Dictionary

Dictionary collection contains a group of elements of key/value pairs (Full Path: `System.Collections.Generic.Dictionary`).

```csharp
Dictionary<TKey, TValue> referenceVariable = new Dictionary<TKey, TValue>();
```

- The "Dictionary" class is a generic class; so you need to specify the data type of the key and the data type of the value while creating the object.
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

Features:

| Property | Description                                    |
|----------|------------------------------------------------|
| `Count`  | Returns count of elements.                     |
| `[TKey]` | Returns value based on specified key.          |
| `Keys`   | Returns a collection of key (without values).  |
| `Values` | Returns a collection of values (without keys). |

| Method                       | Description                                    |
|------------------------------|------------------------------------------------|
| `void Add(TKey, TValue)`     | Adds an element (key/value pair).              |
| `bool Remove(TKey)`          | Removes an element based on specified key.     |
| `bool ContainsKey(TKey)`     | Determines whether the specified key exists.   |
| `bool ContainsValue(TValue)` | Determines whether the specified value exists. |
| `void Clear()`               | Removes all elements.                          |

!!! info

    All the shared features can be used for the Dictionary

## SortedList

SortedList collection contains a group of elements of key/value pairs (Full Path: `System.Collections.Generic.SortedList`).

```csharp
SortedList<TKey, TValue> referenceVariable = new SortedList<TKey, TValue>();
```

- The "**SortedList**" class is a generic class; so you need to specify the data type of the key and the data type of the value while creating the object.
- You can set/get the value based on the key.
- The key can't be null or duplicate.
- It is dynamically sized. You can add, remove elements (key/value pairs) at any time.
- Key can't be null or duplicate, but value can be null or duplicate.
- It is not index-based. You need to access elements by using the key.
- It is sorted by default. The elements are stored in the sorted ascending order, according to the key.
- Each operation of adding an element, removing an element, or any other operation might be slower than a Dictionary, because internally it resorts the data based on the key.
- Will use BinarySearch in the background

Features:

| Property | Description                                    |
|----------|------------------------------------------------|
| `Count`  | Returns count of elements.                     |
| `[TKey]` | Returns value based on specified key.          |
| `Keys`   | Returns a collection of keys (without values). |
| `Values` | Returns a collection of values (without keys). |

| Method                       | Description                                    |
|------------------------------|------------------------------------------------|
| `void Add(TKey, TValue)`     | Adds an element (key/value pair).              |
| `bool Remove(TKey)`          | Removes an element based on specified key.     |
| `bool ContainsKey(TKey)`     | Determines whether the specified key exists.   |
| `bool ContainsValue(TValue)` | Determines whether the specified value exists. |
| `int IndexOfKey(TKey)`       | Returns index of the specified key.            |
| `int IndexOfValue(TValue)`   | Returns index of the specified value.          |
| `void Clear()`               | Removes all elements.                          |

!!! info

    All the shared features can be used for the SortedList

vs Dictionary:

| Operation | Dictionary             | SortedList                        |
|-----------|------------------------|-----------------------------------|
| Insert    | Fast (No need to sort) | Slow (Needs to sort after insert) |
| Search    | Slow (Linear search)   | Fast                              |

## Hashtable

<img src="image15.jpg" style="width:3.5in" />

Hashtable collection contains a group of elements of key/value pairs stored at respective indexes (Full Path: `System.Collections.Hashtable`).

```csharp
Hashtable referenceVariable = new Hashtable();
```

- Process of adding an element:

   1. Generate index based on the key (Ex: `index = hash_code % size_of_hashtable$).
   2. Add the element (key and value) next to the linked list at the generated index.

- GetHashCode method of the key value will be used in the index calculation process
- When we want to use the objs of our custom class as the key inside a hashtable, we should implement the GetHashCode method of that class
- Elements with the same calculated index will be stored in the same index with the linked list data structure
- Each time, when the size of hashtable changes, all the exists indexes will be calculated automatically
- Hashtable will return System.Object instance, because we can store any type of data in Hashtables.
- After retrieving data from hashtable (with `[TKey]` or foreach loop), we should convert the result.
- Hashtable O(1) is faster than SortedList O(log n) in retrieving data
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

Features:

| Property | Description                                    |
|----------|------------------------------------------------|
| `Count`  | Returns count of elements.                     |
| `[TKey]` | Returns value based on specified key.          |
| `Keys`   | Returns a collection of keys (without values). |
| `Values` | Returns a collection of values (without keys). |

| Method                               | Description                                    |
|--------------------------------------|------------------------------------------------|
| `void Add(object key, object value)` | Adds an element (key/value pair).              |
| `void Remove(object key)`            | Removes an element based on specified key.     |
| `bool ContainsKey(object key)`       | Determines whether the specified key exists.   |
| `bool ContainsValue(object value)`   | Determines whether the specified value exists. |
| `void Clear()`                       | Removes all elements.                          |

## Shared Features

`[TKey]`:

```csharp
string s = employees[101];
Console.WriteLine("\nValue at 101: " + s);
```

`Keys`:

```csharp
foreach (int item in employees.Keys) {
    Console.WriteLine(item);
}
```

`Values`:

```csharp
foreach (string item in employees.Values) {
    Console.WriteLine(item);
}
```

`Add`:

```csharp
employees.Add(106, "Anna");
```

`Remove`:

```csharp
employees.Remove(102);
```

`ContainsKey`:

```csharp
bool a = employees.ContainsKey(103);
Console.WriteLine("ContainsKey: " + a);
```

`ContainsValue`:

```csharp
bool b = employees.ContainsValue("Scott");
Console.WriteLine("ContainsValue: " + b);
```

`Clear`:

```csharp
employees.Clear();
```

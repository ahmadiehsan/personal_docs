# Share (List & Hashset & ArrayList & Stack & Queue)

## Shared Features

### Add

This method adds a new element to the collection.

```csharp
void List.Add(T newValue)
```

### AddRange

This method adds a new set of elements to the collection.

```csharp
void List.AddRange(IEnumerable<T> newValue)
```

### Insert

This method adds a new element to the collection at the specified index.

```csharp
void List.Insert(int index, T newValue)
```

### InsertRange

This method adds a new set of elements to the collection at the specified index.

```csharp
void List.InsertRange(int index, IEnumerable<T> newValue)
```

### Remove

This method removes the specified element from the collection.

```csharp
void List.Remove(T newValue)
```

### RemoveAt

This method removes an element from the collection at the specified index.

```csharp
void List.RemoveAt(int index)
```

### RemoveRange

This method removes a specified count of elements starting from the specified `startIndex`.

```csharp
void List.RemoveRange(int index, int count)
```

### Clear

This method removes all elements in the collection.

```csharp
void List.Clear();
```

### IndexOf

This method searches the collection for the given value.

- If the value is found, it returns its index.
- If the value is not found, it returns -1.

```csharp
int List.IndexOf(T value, int startIndex)
```

### BinarySearch

This method searches the array for the given value.

- If the value is found, it returns its index.
- If the value is not found, it returns `-1`.

```csharp
int List.BinarySearch(T value)
```

### Contains

This method searches the specified element and returns `true`, if it is found; but returns `false`, if it is not found.

- This method performs a linear search in the List but will have O(1) in the Hashset

```csharp
bool List.Contains(T value)
```

### Sort

This method sorts the collection in ascending order.

```csharp
void List.Sort()
```

### Reverse

This method reverses the collection.

- For sorting a list in descending order, first we should call it's Sort method then we should fire its Reverse method

```csharp
void List.Reverse()
```

### ToArray

This method converts the collection into an array with the same elements.

```csharp
T[] List.ToArray()
```

### Peek

Retrieves the object at the front of a collection, such as a queue or stack, without removing it.

- Will not remove the returned element

Example:

```csharp
Student stu = marks.Peek();
Console.WriteLine("Peek: " + stu.Marks);
```

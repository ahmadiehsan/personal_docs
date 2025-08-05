# ArrayList

## Description

ArrayList collection contains a group of elements of any type.

```csharp
ArrayList referenceVariable = new ArrayList();
```

- Full Path: `System.Collections.ArrayList`
- The `ArrayList` class is not a generic class; so you need not specify data type value while creating an object.
- Exactly like List, except in the ArrayList we can store any type of data at the same time
- It is dynamically sized. You can add or remove elements at any time.
- It is index-based. You need to access elements by using the zero-based index.
- It is not sorted by default. The elements are stored in the same order in which they are initialized.
- You don't specify the data type of elements for ArrayList. So you can store any type of elements in ArrayList.
- Each element is treated as `System.Object` type while adding, searching, and retrieving elements.

## Features

### Overview

| **Feature**                     | **Description**                                                                 |
|---------------------------------|---------------------------------------------------------------------------------|
| `Count`                         | Retrieves the total number of elements.                                         |
| `Capacity`                      | Gets or sets the total number of elements the internal data structure can hold. |
| `Add(object)`                   | Adds an object to the list.                                                     |
| `AddRange(ICollection)`         | Adds all the elements in the specified collection to the list.                  |
| `Insert(int, object)`           | Inserts an object at the specified index.                                       |
| `InsertRange(int, ICollection)` | Inserts a collection of elements at the specified index.                        |
| `Remove(object)`                | Removes the first occurrence of a specific object in the list.                  |
| `RemoveAt(int)`                 | Removes the object at the specified index.                                      |
| `RemoveRange(int, int)`         | Removes a range of elements starting at a specified index.                      |
| `Clear()`                       | Removes all elements from the list.                                             |
| `IndexOf(object)`               | Returns the zero-based index of the first occurrence of an object.              |
| `BinarySearch(object)`          | Searches the list using binary search.                                          |
| `Contains(object)`              | Checks whether a specific object exists in the list or not.                     |
| `Sort()`                        | Sorts the elements of the list.                                                 |
| `Reverse()`                     | Reverses the order of the elements in the list.                                 |
| `ToArray()`                     | Copies the elements of the list to a new array.                                 |

!!! info

    All the shared features can be used for ArrayList

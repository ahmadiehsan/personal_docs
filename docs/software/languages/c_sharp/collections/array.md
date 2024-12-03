# Array

## Description

Array is a group of multiple values of the same type.

```csharp
type[] arrayReferenceVariableName = new type[size];
```

- Arrays are stored in continuous-memory-locations in the 'heap'.
- Each value of the array is called "element".
- All the elements are stored in continuous memory locations.
- The address of the first element of the array will be stored in the "array reference variable".
- The "Length" property stores count of elements of the array. The index starts from 0 (zero).
- Arrays are treated as objects of the "System.Array" class, so arrays are stored in the heap; the address (first element's address) is stored in a reference variable at stack.
- By default, all the array elements will store by their default value (int: 0, bool: false, string and other obj: null)
- Arrays will store the reference of objects not the actual object
- Arrays are object, so their elements (regardless of being primitive or non-primitive) will store in heap

Example:

```csharp
int[] a = new int[5] { 10, 20, 30, 40, 50 };
string[] b = new string[5] { "one", "two", "three", "four", "five" };
```

## Nested Arrays

### Multidimensional Array

Stores elements in rows & columns format.

```csharp
type[,] arrayReferenceVariable = new type[rowSize, columnSize];
```

- Every row contains a series of elements.
- You can create arrays with two or more dimensions, by increasing the number of commas (`,`).
- Child arrays should be the same size

Example:

```csharp
// multi-dim array 4 X 3
int[,] a = new int[4, 3]
{
    { 10, 20, 30 },
    { 40, 60, 70 },
    { 80, 90, 100 },
    { 110, 120, 130 }
};
```

### Jagged Arrays

Jagged Array is an "array of arrays". The member arrays can be of any size.

```csharp
type[][] arrayReferenceVariable = new type[rowSize][];
arrayReferenceVariable[index] = new type[size];
```

Example:

```csharp
//create jagged array
int[][] a = new int[5][];
a[0] = new int[3] { 10, 20, 30 };
a[1] = new int[5] { 40, 50, 60, 70, 80 };
a[2] = new int[2] { 90, 100 };
a[3] = new int[4] { 110, 120, 130, 140 };
a[4] = new int[8] { 150, 160, 170, 180, 190, 200, 210, 220 };
```

## System.Array

### Features

All the arrays internally will convert into this class.

Properties:

- Length

Methods:

- IndexOf
- BinarySearch
- Clear
- Resize
- Sort
- Reverse
- CopyTo
- Clone

### IndexOf

This method searches the array for the given value.

- The `IndexOf()` method performs a **linear search**. That means it searches all the elements of an array, until the search value is found (When the search value is found in the array, it stops searching and returns its index).
- If the value is found, it returns its index.
- If the value is not found, it returns -1.

```csharp
static int Array.IndexOf( System.Array array, int value )
```

!!! info

    The linear search has good performance if the array is small. But if the array is larger, **Binary search** is recommended to improve performance.

Example:

```csharp
//create array
double[] a = new double[6] { 10, 20, 30, 40, 50, 30 };

//search for 30 in the array
int n = Array.IndexOf(a, 30);
Console.WriteLine("30 is found at " + n);

//search for 30 in the array (second occurrence)
int n2 = Array.IndexOf(a, 30, 3);
Console.WriteLine("30 second occurrence is found at " + n2);

//search for 100 in the array (not exists)
int n3 = Array.IndexOf(a, 100);
Console.WriteLine("100 is found at " + n3);
```

### BinarySearch

This method searches the array for the given value.

- The **"Binary Search"** requires an array, which is already sorted.
- On unsorted arrays, binary search is not possible.
- It directly goes to the middle of the array (array size / 2), and checks that the item is less than/greater than the search value.
- If that item is greater than the search value, it searches only in the first half of the array.
- If that item is less than the search value, it searches only in the second half of the array.
- If the value is found, it returns its index.
- If the value is not found, it returns -1.
- Thus it searches only half of the array. So in this way, it saves performance.

```csharp
static int Array.BinarySearch(System.Array array, int value)
```

### Clear

This method starts with the given index and sets all the "length" no. of elements to zero (0).

```csharp
static void Array.Clear( System.Array array, int value, int length )

// array: This parameter represents the array, in which you want to clear the elements.
// index: This parameter represents the index, from which clearing process is to be started.
// length: This parameter represents the no. of elements that are to be cleared.
```

### Resize

```csharp
static void Array.Resize(ref System.Array array, int newSize)

// array: This parameter represents the array, which you want to resize.
// newSize: This parameter represents the new size of the array, how many elements you want to store in the array. It can be less than or greater than the current size.
```

- In case of increase, the new elements will fill with the type default value
- Actually, this method will create a new array and will copy the elements into the new one

### Sort

```csharp
static void Array.Sort( System.Array array )
```

- By default, will sort the array in ascending order

### Reverse

```csharp
static void Array.Reverse(System.Array array)
```

- For sorting an array in descending order, first we should use sort method and then passing the result into this method

### IndexFromEnd and Range Operator

The `^` operator returns the index of an element from the end of an array. The last element is treated as index `0`.

Here is an illustration:

| Expression | Accesses | Result |
|------------|----------|--------|
| a[^6]      | a[0]     | value0 |
| a[^5]      | a[1]     | value1 |
| a[^4]      | a[2]     | value2 |
| a[^3]      | a[3]     | value3 |
| a[^2]      | a[4]     | value4 |
| a[^1]      | a[5]     | value5 |
| a[^0]      | a[6]     | value6 |

Example:

```csharp
// create an array
int[] a = new int[] { 10, 20, 30, 40, 50, 60 };

// index-from-end operator
int result = a[^0];
Console.WriteLine(result); // Output: 60

// range operator
int[] result2 = a[2..5]; // Output: [20, 30, 40]
```

## Copy One Array

### Shallow (CopyTo)

- `CopyTo()` requires you to have an existing destination array; and the destination array should be large enough to hold all elements from the source array, starting from the specified `startIndex`.
- `CopyTo()` allows you to specify the `startIndex` at destination array.
- The result array need not be type-casted explicitly.

```csharp
//new array
Employee[] highlyPaidEmployees = new Employee[3];
employees.CopyTo(highlyPaidEmployees, 0);

//print destination array
foreach (Employee emp in highlyPaidEmployees) {
    Console.WriteLine(emp.EmployeeName + "," + emp.Role);
}
```

### Shallow (Clone)

- `Clone()` creates a new destination array; you need not have an existing array.
- `Clone()` doesn’t allow you to specify the `startIndex` at destination array.
- The result array will be returned as 'object' type; so it needs to be type-casted to array type.

```csharp
//Clone
Employee[] highlyPaidEmployees2 = (Employee[])employees.Clone(); // creates a new array & copies from source array to that new array
foreach (Employee emp in highlyPaidEmployees2) {
    // ...
}
```

### Deep

There isn't any specific way for deep copy in .NET but we can write the deep clone behaviour with ICloneable like the below:

```csharp
class Employee: ICloneable {
    public string EmployeeName { get; set; }
    public string Role { get; set; }

    public object Clone()
    {
        Employee new_one = new Employee()
        {
            EmployeeName = this.EmployeeName,
            Role = this.Role
        };
        return new_one;
    }
}

var result = (Employee)employees[i].Clone();
```

## Anonymous Array

You can create 'array of anonymous objects' or 'implicitly typed array' with a group of anonymous objects (All objects must contain the same set of properties).

Example:

```csharp
var referenceVariable = new[]
{
    new { Property1 = value, Property2 = value, ... },  // It equals to RandomClassName
    new { Property1 = value, Property2 = value, ... }  // It equals to RandomClassName
};

class RandomClassName {
    public type Property1 { get; set; }
    public type Property2 { get; set; }
}
```

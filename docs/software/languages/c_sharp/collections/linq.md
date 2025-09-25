# LINQ

## Description

LINQ is a 'uniform query syntax' that allows you to retrieve data from various data sources such as arrays, collections, databases, XML files.

- **Single Syntax - To Query Multiple Data Sources**: Developer uses the same LINQ syntax to retrieve information from various data sources such as collections, SQL Server database, Entity Framework DbSet's, ADO.NET DataSet, etc.
- **Compile-Time Checking of Query Errors**: Errors in the LINQ query will be identified during compilation time / while writing the code in Visual Studio.
- **LINQ stands for**: Language Integrated Query

Developer uses **LINQ** to Retrieve from:

- Collection of Objects *(LINQ to Collections)*
- SQL Server Database *(LINQ to SQL)*
- Entity Framework DbSet *(LINQ to Entities)*
- ADO.NET DataSet *(LINQ to DataSet)*
- XML Files *(LINQ to XML)*

```csharp
var result = Customers.Where(temp => temp.Location == "New York").ToList();
// returns a list of customers from New York location.
```

## Operators & Extension Methods

=== "Overview"

    | Classification     | LINQ Extension Methods / LINQ Operators                                                            |
    | ------------------ | -------------------------------------------------------------------------------------------------- |
    | **Filtering**      | Where, OfType                                                                                      |
    | **Sorting**        | OrderBy, OrderByDescending, ThenBy, ThenByDescending, Reverse                                      |
    | **Grouping**       | GroupBy                                                                                            |
    | **Join**           | Join                                                                                               |
    | **Project**        | Select, SelectMany                                                                                 |
    | **Aggregation**    | Average, Count, Max, Min, Sum                                                                      |
    | **Quantifiers**    | All, Any, Contains                                                                                 |
    | **Elements**       | ElementAt, ElementAtOrDefault, First, FirstOrDefault, Last, LastOrDefault, Single, SingleOrDefault |
    | **Set Operations** | Distinct, Except, Intersect, Union                                                                 |
    | **Partitioning**   | Skip, SkipWhile, Take, TakeWhile                                                                   |
    | **Concatenation**  | Concat                                                                                             |
    | **Equality**       | SequenceEqual                                                                                      |
    | **Generation**     | DefaultEmpty, Empty, Range, Repeat                                                                 |
    | **Conversion**     | AsEnumerable, AsQueryable, Cast, ToArray, ToDictionary, ToList                                     |

=== "OrderBy & ThenBy"

    The `OrderBy()` method sorts a collection based on a given lambda expression (property) and returns a new collection with sorted elements.

    ```csharp
    OrderBy(Func<TSource, TKey> keySelector)
    ```

    ```csharp
    var result = Customers.OrderBy(temp => temp.CustomerName).ToList();
    // returns a list of customers sorted based on customer name.
    ```

    We can chain orders by `ThenByDescending`:

    ```csharp
    ThenByDescending(Func<TSource, TKey> keySelector)
    ```

    ```csharp
    var result = Customers.OrderBy(temp => temp.Location)
                        .ThenByDescending(temp => temp.CustomerName).ToList();
    // returns a list of customers sorted based on location (ascending) and customer name (descending).
    ```

=== "First"

    `First()` method returns the first element in the collection that matches the condition.
    It throws an exception if no element matches the condition.

    ```csharp
    First(Func<TSource, bool> predicate)
    ```

    ```csharp
    var result = Customers.First(temp => temp.Location == "Dallas");
    // returns the first customer from Hyderabad location.
    ```

=== "FirstOrDefault"

    `FirstOrDefault()` method returns the first element that matches with the condition.
    It returns `null` if no element matches with the condition.

    ```csharp
    FirstOrDefault(Func<TSource, bool> predicate)
    ```

    ```csharp
    var result = Customers.FirstOrDefault(temp => temp.Location == "London");
    // returns the first customer from London location (or) returns null if not exists.
    ```

=== "Last"

    `Last()` method returns the last element in the collection that matches the given condition.
    Throws an exception if no element matches the condition.

    ```csharp
    Last(Func<TSource, bool> predicate)
    ```

    ```csharp
    var result = Customers.Last(temp => temp.Location == "Dallas");
    // returns the last customer from Dallas location.
    ```

=== "LastOrDefault"

    `LastOrDefault()` method returns the last element that matches the condition.
    It returns `null` if no element matches the condition.

    ```csharp
    LastOrDefault(Func<TSource, bool> predicate)
    ```

    ```csharp
    var result = Customers.LastOrDefault(temp => temp.Location == "London");

    // returns the last customer from London location (or returns null if not exists).
    ```

=== "ElementAt"

    `ElementAt()` method returns an element in the collection at the specified index.
    It throws an exception if no element exists at the specified index; to get `null` instead, use `ElementAtOrDefault()`.

    ```csharp
    ElementAt(int index)
    ```

    ```csharp
    var result = Customers.ElementAt(1);  // Returns the customer at index 1
    ```

=== "Single"

    It returns the first element (only one element) that matches with the collection.
    It throws an exception if no element or multiple elements match with the condition.

    ```csharp
    Single(Func<TSource, bool> predicate)
    ```

    ```csharp
    var result = Customers.Single(temp => temp.Location == "Dallas");

    // This returns the first (only one customer) from the Dallas location.
    // However, it throws an exception if none or multiple elements match the condition.
    ```

=== "SingleOrDefault"

    It returns the first element (only one element) that matches with the collection.
    It returns null if no element matches with the condition; but it throws an exception if multiple elements match with the condition.

    ```csharp
    SingleOrDefault(Func<TSource, bool> predicate)
    ```

    ```csharp
    var result = Customers.SingleOrDefault(temp => temp.Location == "London");

    // Returns the first (only one customer) from London location.
    // Throws an exception if multiple elements match; but null in case of no match.
    ```

=== "Take"

    Will receive the first number of elements

=== "Select"

    It returns a collection by converting each element into another type, based on the conversion expression.

    ```csharp
    Select(Func<TSource, TResult> selector)
    ```

    ```csharp
    var result = Customers.Select(temp => new RegisteredCustomer()
    {
        CustomerName = temp.CustomerName,
        Location = temp.Location
    });
    // Converts all customers into a collection of RegisteredCustomer class.
    ```

=== "Add"

    Will add one element into the collection

=== "AddRange"

    Will add multiple elements into the collection at once

=== "Remove"

    Will remove one element from the collection

=== "RemoveRange"

    Will remove multiple elements from the collection at once

=== "Min, Max, Sum, Average, Count"

    ```csharp
    List<Employee> employees = new List<Employee>()
    {
        new Employee(){ EmpID = 101, EmpName = "Henry", Job = "Designer", Salary = 900 },
        new Employee(){ EmpID = 102, EmpName = "Jack", Job = "Developer", Salary = 1200 },
        new Employee(){ EmpID = 103, EmpName = "Gabriel", Job = "Analyst", Salary = 650 },
        new Employee(){ EmpID = 104, EmpName = "William", Job = "Manager", Salary = 440 },
        new Employee(){ EmpID = 105, EmpName = "Alexa", Job = "Manager", Salary = 1100 },
        new Employee(){ EmpID = 106, EmpName = "Jessica", Job = "Manager", Salary = 800 }
    };

    double min = employees.Min(emp => emp.Salary);
    double max = employees.Max(emp => emp.Salary);
    double sum = employees.Sum(emp => emp.Salary);
    double avg = employees.Average(emp => emp.Salary);
    double cnt = employees.Count();
    ```

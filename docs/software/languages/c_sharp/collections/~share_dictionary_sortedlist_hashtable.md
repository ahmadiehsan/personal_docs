# Share (Dictionary & SortedList & Hashtable)

## Shared Features

### [TKey]

```csharp
string s = employees[101];
Console.WriteLine("\nValue at 101: " + s);
```

### Keys

```csharp
foreach (int item in employees.Keys) {
    Console.WriteLine(item);
}
```

### Values

```csharp
foreach (string item in employees.Values) {
    Console.WriteLine(item);
}
```

### Add

```csharp
employees.Add(106, "Anna");
```

### Remove

```csharp
employees.Remove(102);
```

### ContainsKey

```csharp
bool a = employees.ContainsKey(103);
Console.WriteLine("ContainsKey: " + a);
```

### ContainsValue

```csharp
bool b = employees.ContainsValue("Scott");
Console.WriteLine("ContainsValue: " + b);
```

### Clear

```csharp
employees.Clear();
```

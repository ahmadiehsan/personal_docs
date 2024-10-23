# Namespace

## Description

Namespaces is a collection of classes and other types such as interfaces, structures, delegate types, enumerations.

```csharp
namespace NamespaceName
{
    Classes
    Interfaces
    Structures
    Delegate Types
    Enumerations
}
```

- Will help us to spread our classes into multiple files
- In the future, when we want to refactor out project and moving some classes into other files, without any effort we can do it

Example:

```csharp
namespace FrontOffice
{
}

namespace HR
{
}
```

## Nested Namespace

The namespace which is declared inside another namespace is called as "Nested namespace" or "Inner Namespace".

- Use nested namespaces, in order to divide the classes of a larger namespace, into smaller groups.
- Accessing syntax: `OuterNamespace.InnerNamespace.TypeName`

Example:

```csharp
namespace OuterNamespace
{
    Classes
    Interfaces
    Structures
    Delegate Types
    Enumerations

    namespace InnerNamespace
    {
        Classes
        Interfaces
        Structures
        Delegate Types
        Enumerations
    }
}
```

## File Scoped Namespace

C# 9:

```csharp
using System;

namespace Namespace
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
```

C# 10:

```csharp
namespace FileScopedNamespace;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello World!");
    }
}
```

## `using` Directive

The "using" is a directive statement (top-level statement) that should be placed at the top of the file, which specifies the namespace, from which you want to import all the classes and other types.

```cs
using Namespacename;
```

- When you import a namespace, you can directly access all of its classes and other types (but not inner namespaces).
- The "using directives" are written independently for every file.
- "One using directive" can import "one namespace" only.

Alias:

The "using alias" directive allows you to create an "alias name" for the namespace.

```cs
using AliasName = Namespacename;
```

- Use "using alias" directive, if you want to access long namespaces with a shortcut name.
- It is much more useful to access a specific namespace when there is a namespace name ambiguity (e.g., two classes with the same name in two different namespaces, and both namespaces are imported into the same file).

Using Static:

The "using static" directive allows you to import a static class directly from a namespace so that you can directly access any of its methods anywhere in the current file.

```cs
using static Namespacename.StaticClassName;
```

- Use the "using static" directive to access the methods of a static class easily, without repeating the class name each time.
- With this feature we can treat a static class like namespace

# Property

## Syntax

<img src="image2.jpg" style="width:5in" />

## Set Accessor & Get Accessor

Set Accessor:

```csharp
set
{
    field = value;
}
```

- Has a default (implicit) parameter called "value", which represents the current value assigned to the property.
- Can't have any additional parameters.
- Can't return any value.

Get Accessor:

```csharp
get
{
    return field;
}
```

- Has no implicit parameters.
- Can't have parameters.
- Should return the value of the field.

## Read-Only & Write-Only

Readonly property:

```csharp
accessModifier type PropertyName {
    get
    {
        return field;
    }
}
```

- Contains only `get` accessor.
- Reads and returns the value of the field, but does not modify the value of the field.

Write-only property:

```csharp
accessModifier type PropertyName {
    set
    {
        field = value;
    }
}
```

- Contains only `set` accessor.
- Validates and assigns incoming values into the field, but does not return the value.

## Auto Implemented Property

Property with no definition for set-accessor and get-accessor.

- Used to create property easily (with shorter syntax).
- Creates a private field (with name as `_propertyName`) automatically, while compilation-time.
- Auto-implemented property can be 'Write-only Property (only set accessor)' or 'Read-only property (only get accessor)'.
- Useful only when you don't want to write any validation or calculation logic.

```csharp
accessModifier modifier type propertyName {
    accessModifier set;
    accessModifier get;
}
```

## Features

- Properties create a protection layer around fields, preventing assignment of invalid values into properties & also do some calculation automatically when someone has invoked the property.
- No memory will be allocated for the property.
- Access modifier is applicable for the property, set accessor, and get accessor individually.
- Access modifiers of accessors must be more restrictive than the access modifier of the property.

   ```csharp
   internal modifier dataType PropertyName
   {
       private set { property = value; }
       protected get { return property; }
   }
   ```

- It is recommended to use Properties always in real-time projects (You can also use 'Auto-implemented properties' to simplify the code).
- Properties don't occupy any memory (will not be stored).
- Properties form a protection layer surrounding the private field that validates the incoming value before assigning it to the field.
- Read-only property has only the 'get' accessor; Write-only property has only the 'set' accessor.
- Properties can't have additional parameters.

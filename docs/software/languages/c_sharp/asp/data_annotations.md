# Data annotations

## Description

When you use the Data Annotations Model Binder, you use validator attributes to perform validation. The System.ComponentModel.DataAnnotations namespace includes the following validator attributes:

- Range – Enables you to validate whether the value of a property falls between a specified range of values.
- RegularExpression – Enables you to validate whether the value of a property matches a specified regular expression pattern.
- Required – Enables you to mark a property as required.
- StringLength – Enables you to specify a maximum length for a string property.
- Validation – The base class for all validator attributes.

## Example

```csharp
public class Product {
    public int Id { get; set; }

    [Required]
    [StringLength(10)]
    public string Name { get; set; }

    [Required]
    public string Description { get; set; }

    [DisplayName("Price")]
    [RegularExpression(@"^\$?\d+(\.\d{2})?$")]
    public decimal UnitPrice { get; set; }
}
```

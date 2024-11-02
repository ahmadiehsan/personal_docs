# Operators

## Increment / Decrement Operators

| Operator | Explanation                                                   |
|----------|---------------------------------------------------------------|
| n++      | Post-Incrementation (First it returns value; then increments) |
| ++n      | Pre-Incrementation (First it increments value; then returns)  |
| n--      | Post-Decrementation (First it returns value; then decrements) |
| --n      | Pre-Decrementation (First it decrements value; then returns)  |

## Logical Operators

### And, Or, XOr, Negation

<!-- markdownlint-disable MD056 -->
| Operator | Explanation                                                                                                                      |
|----------|----------------------------------------------------------------------------------------------------------------------------------|
| &        | Logical AND (Both operands should be true) Evaluates both operands, even if left-hand operand returns false.                     |
| &&       | Conditional AND (Both operands should be true) Doesn't evaluate right-hand operand, if left-hand operand returns false.          |
| \|       | Logical OR (At least any one operand should be true) Evaluates both operands, even if left-hand operand returns true.            |
| \|\|     | Conditional OR (At least any one operand should be true) Doesn't evaluate right-hand operand, if left-hand operand returns true. |
| ^        | Logical Exclusive OR - XOR (Any one operand only should be true) Evaluates both operands.                                        |
| !        | Negation (true becomes false; False becomes true)                                                                                |
<!-- markdownlint-enable MD056 -->

### is

| Expression                                                 | Meaning                                                                                |
|------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `another_variable.property is value`                       | `another_variable.property == value`                                                   |
| `another_variable.property is < value`                     | `another_variable.property < value`                                                    |
| `another_variable.property is > value`                     | `another_variable.property > value`                                                    |
| `another_variable.property is <= value`                    | `another_variable.property <= value`                                                   |
| `another_variable.property is >= value`                    | `another_variable.property >= value`                                                   |
| `another_variable.property is expression1 and expression2` | `another_variable.property == expression1 && another_variable.property == expression2` |
| `another_variable.property is not expression`              | `another_variable.property != expression`                                              |

## Null Operators

### Coalescing

The 'null coalescing operator' checks whether the value is null or not.

- It returns the left-hand-side operand if the value is not null.
- It returns the right-hand-side operand if the value is null.
- Simplifying the syntax of the 'if statement' to check if the value is null.

```csharp
variableName ?? valueIfNull
```

### Propagation

The Null Propagation Operator (`?.`) and (`?[]`) checks the value of the left-hand operand whether it is null or not.

- It returns the right-hand-side operand (property or method), if the value is not null.
- It returns null, if the value is null.
- It accesses the property or method, only if the reference variable is "not null"; just returns "null", if the reference variable is "null".

```csharp
referenceVariable?.fieldName;

// Is same as:
(referenceVariable == null) ? null : referenceVariable.fieldName;
```

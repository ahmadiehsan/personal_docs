# Composition (Constructor Create)

## Description

- Represents a "has-a" relationship between classes where one class is composed of another.
- Shown as a solid diamond shape with a line connecting the composite class to the component class.
- The component class is part of the composite class and cannot exist independently.

<img src="image1.png" style="width:4.18048in" />

## Example

```python
class Engine:
    pass

class Car:
    def __init__(self) -> None:
        # Composition with Engine
        self.engine: Engine = Engine()
```

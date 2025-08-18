# Goose Typing

## Description

ABCs makes protocols explicit.

Abstract base classes complement duck-typing by providing a way to define interfaces when other techniques like hasattr() would be clumsy or subtly wrong (for example with magic methods).
ABCs introduce virtual subclasses, which are classes that don't inherit from a class but are still recognized by isinstance() and issubclass()

What goose typing means is: isinstance(obj, cls) is now just fine… as long as cls is an Abstract Base Class.

<img src="image1.jpg" style="width:3.99167in" />

# Vs (Adapter & Facade)

## Description

The Adapter Pattern changes the interface of one or more classes into one interface that a client is expecting.
While most textbook examples show the adapter adapting one class, you may need to adapt many classes to provide the interface a client is coded to.
Likewise, a Facade may provide a simplified interface to a single class with a very complex interface.

The difference between the two is not in terms of how many classes they "wrap," it is in their intent. The Adapter Pattern intends to alter an interface so that it matches one a client is expecting. The Facade Pattern intends to provide a simplified interface to a subsystem.

Facades and adapters may wrap multiple classes, but a facade intends to simplify, while an adapter converts the interface to something different.

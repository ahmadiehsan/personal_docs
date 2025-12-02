# Overview

## Creational Design Patterns

Creational design patterns are concerned with the way of creating objects.
These design patterns are used when a decision must be made at the time of the instantiation of a class (i.e. creating an object of a class).

This pattern can be further divided into class-creation patterns and object-creational patterns.
While class-creation patterns use inheritance effectively in the instantiation process, object-creation patterns use delegation effectively to get the job done.

!!! info

    <span dir="rtl">دیزاین پترن هایی که روی نحوه ساخت آبجکت ها تمرکز دارن کریشنال میگن.</span>

## Structural Design Patterns

Structural design patterns are concerned with how classes and objects can be composed, to form larger structures.
The structural design patterns simplify the structure by identifying relationships.

These patterns focus on how the classes inherit from each other and how they are composed of other classes.

Structural class-creation patterns use inheritance to compose interfaces.
Structural object patterns define ways to compose objects to obtain new functionality.

!!! info

    <span dir="rtl">دیزاین پترن هایی که روی نحوه ارتباط آبجکت ها با هم تمرکز دارن استراکچرال میگن.</span>

## Behavioral Design Patterns

Behavioral design patterns are concerned with the interaction and responsibility of objects.
In these design patterns, the interaction between the objects should be in such a way that they can easily talk to each other and still should be loosely coupled.

That means the implementation and the client should be loosely coupled to avoid hard coding and dependencies.

## Class Patterns & Object Patterns

<img src="image2.png" />

| **Scope**  | **Creational**   | **Structural**   | **Behavioral**          |
| ---------- | ---------------- | ---------------- | ----------------------- |
| **Class**  | Factory Method   | Adapter (class)  | Interpreter             |
| "          |                  |                  | Template Method         |
| **Object** | Abstract Factory | Adapter (object) | Chain of Responsibility |
| "          | Builder          | Bridge           | Command                 |
| "          | Prototype        | Composite        | Iterator                |
| "          | Singleton        | Decorator        | Mediator                |
| "          |                  | Facade           | Memento                 |
| "          |                  | Flyweight        | Observer                |
| "          |                  | Proxy            | State                   |
| "          |                  |                  | Strategy                |
| "          |                  |                  | Visitor                 |

## Design Pattern Relationships

<img src="image1.jpg" />

## Each Pattet for What Aspect

| **Purpose**    | **Design Pattern**      | **Aspect(s) That Can Vary**                                                                |
| -------------- | ----------------------- | ------------------------------------------------------------------------------------------ |
| **Creational** | Abstract Factory        | families of product objects                                                                |
| "              | Builder                 | how a composite object gets created                                                        |
| "              | Factory Method          | subclass of object that is instantiated                                                    |
| "              | Prototype               | class of object that is instantiated                                                       |
| "              | Singleton               | the sole instance of a class                                                               |
| **Structural** | Adapter                 | interface to an object                                                                     |
| "              | Bridge                  | implementation of an object                                                                |
| "              | Composite               | structure and composition of an object                                                     |
| "              | Decorator               | responsibilities of an object without subclassing                                          |
| "              | Facade                  | interface to a subsystem                                                                   |
| "              | Flyweight               | storage costs of objects                                                                   |
| "              | Proxy                   | how an object is accessed; its location                                                    |
| **Behavioral** | Chain of Responsibility | object that can fulfill a request                                                          |
| "              | Command                 | when and how a request is fulfilled                                                        |
| "              | Interpreter             | grammar and interpretation of a language                                                   |
| "              | Iterator                | how an aggregate's elements are accessed, traversed                                        |
| "              | Mediator                | how and which objects interact with each other                                             |
| "              | Memento                 | what private information is stored outside an object, and when                             |
| "              | Observer                | number of objects that depend on another object; how the dependent objects stay up to date |
| "              | State                   | states of an object                                                                        |
| "              | Strategy                | an algorithm                                                                               |
| "              | Template Method         | steps of an algorithm                                                                      |
| "              | Visitor                 | operations that can be applied to object(s) without changing their class(es)               |

!!! info

    <span dir="rtl">در جدول بالا به راحتی میتونیم ببینیم هر پترن کمک به داینامیک شدن چه جنبه ای میکنه (هدف از دیزاین پترن ها ایزوله کردن بخش هایی از کد هست که در آینده ممکنه تغییر کنن)</span>

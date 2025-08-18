# Delegate & Event

## Delegate

**Delegate type** is a "type" that represents methods that have specific parameters and return type. **Delegate** (a.k.a. delegate object) is an object that stores reference (address) of a specific method of a specific class, with compatible parameters and return type, which is already defined in the delegate type.

- You can invoke the methods using 'delegate objects' or 'delegates'.
- Delegates are used to pass methods as arguments to other methods.
- The method signature (parameters and return type) must match between the "method" and "delegate".
- Delegates can be used as "parameter type" or "return type" of a method.
- You can store references of non-static method or static method in the delegate object.
- The methods, which reference is stored in the "single-cast delegate object", can have a return value.
- The methods, which reference is stored in the "multi-cast delegate object", can't have a return value; in case, if they have a return value, the return value of lastly-executed method only can be received; others will be ignored.
- All delegate types are derived from the `System.Delegate` class.

```csharp
// 1. Creating a Delegate
public delegate ReturnType DelegateTypeName(param1, param2, ...);

// 2. Creating a Delegate Object
DelegateTypeName ReferenceVariable = MethodName;

// 3. Invoke Method using Delegate Object
ReferenceVariable.Invoke(arg1, arg2, ...);
```

Example:

```csharp
namespace ClassLibrary1
{
    // delegate type
    public delegate void MyDelegateType(double a, double b);
}
```

```csharp
// create object of Sample
Sample s = new Sample();

// create reference variable of MyDelegateType
MyDelegateType myDelegate;

// add ref of first target method
myDelegate = s.Add;

// add ref of second target method
myDelegate += s.Multiply;

// invoke both target methods
myDelegate.Invoke(40, 10);
```

Mulit-Cast vs Single-Cast:

| **Single-Cast Delegates**                               | **Multi-Cast Delegates**                                                      |
|---------------------------------------------------------|-------------------------------------------------------------------------------|
| Contains reference of only one method.                  | Contains references of multiple methods.                                      |
| When called, it directly invokes the referenced method. | When called, it invokes all the referenced methods, one-by-one in a sequence. |
|                                                         | All methods' parameters and return type should be the same.                   |

## Predefined Delegates

### Func

"Func" is a pre-defined generic-delegate, which can be used to create events quickly.

- Func supports parameters and return value also.
- Func must have 0 to 16 parameters.
- Func must have a return value.

```csharp
public Func<Param1DataType, Param2DataType, ReturnType> referenceVariable;

// Param1DataType, `Param2DataType`: Can be 0 to 16 parameters.
// ReturnType: The last one is treated as the "return type" (it is a must).
```

### Action

"Action" is a pre-defined delegate, which can be used to create events quickly, similar to "Func".

The difference with **Func**:

1. Func must have return value; Action doesn't have return value.
2. Action must have 0 to 16 parameters.

```csharp
public Action<Param1DataType, Param2DataType, Param3DataType> referenceVariable;

// Param1DataType, Param2DataType, Param3DataType: Can be 0 to 16 parameters
// [No return value]
```

### Predicate

"Predicate" is a pre-defined delegate, which can be used to create events quickly, similar to "Func".

The difference with **Func** and **Action**:

1. **Func** must have return value of any type; **Action** doesn't have a return value; **Predicate** must have return value of `bool` type.
2. **Func** can have 0 to 16 parameters of any type; **Action** can have 0 to 16 parameters of any type; **Predicate** must have only one parameter of any type.

```csharp
public Predicate<Param1DataType> referenceVariable;

// Param1DataType: Only one parameter
// Default return type is `bool`
```

### EventHandler

'EventHandler' is a pre-defined delegate type, which has two parameters called "object sender" and "EventArgs e"; and no return.

- **object sender**: Represents the source object, where the event is originally raised.
- **EventArgs e**: Represents additional parameters to pass to 'event handler method'. It is recommended to create a child class for 'EventArgs' class.

```csharp
public event EventHandler EventName;
```

### Expression Trees

Expression Tree is a collection of delegates represented in a tree-like structure.

- Expression Tree only executes when we compile and execute it.
- Expression Trees support all delegate types such as `Func`, `Action`, `Predicate`, or custom delegate types.

```csharp
// Creating Expression Tree based on Func
Expression<Func<type1, type2, ...>> referenceVariable;

// Compile and Execute Expression Tree
Func<type1, type2, ...> referenceVariable2 = referenceVariable.Compile();
referenceVariable2.Invoke(arg1, arg2, ...);
```

Example:

```csharp
// Create object of Student class
Student s = new Student() { StudentID = 101, StudentName = "Scott", Age = 15 };

// Create expression tree with Func
Expression<Func<Student, bool>> expression = st => st.Age > 12 && st.Age < 20;

// Compile expression using Compile method to invoke it as Delegate
Func<Student, bool> myDelegate = expression.Compile();

// Execute the method
bool result = myDelegate.Invoke(s);
```

## Events

**Event** is a multi-cast delegate that stores one or more methods; and invokes them every time when the event is raised (called).
The event can be raised only in the same class in which it is created.

- Events enable a class to send notifications to other classes when something occurs.
- Publisher class sends events; Subscriber class receives events.
- Process flow of Events:

   - The Publisher class creates an event.
   - The Subscriber class subscribes to the event, this means an "event handler" method is created in the subscriber class. The "event handler" method is nothing but the method dedicated to execution when the event is raised.
   - The publisher class can send (raise) events.
   - Every time the event is raised by the publisher, the corresponding "event handler" method executes automatically.

- The event should be created based on the delegate. That means, the event accepts the methods that are having specific parameters and return type, defined in the delegate.
- An event can have multiple subscribers.
- A subscriber can subscribe to multiple events from multiple publishers.
- Events are basically signals to inform other classes that some important thing happened in the publisher class.
- Events are a special kind of "multi-cast delegates", which can be raised only within the same class in which they are created.
- Events can be static, virtual, sealed, and abstract.
- Events will not be raised (throws exception) if there is no at least one subscriber.
- Events can be defined in interfaces.
- It's not a good idea to return value in events.

```csharp
// Step 1: Create a Delegate
public delegate ReturnType DelegateTypeName(param1, param2, ...);

// Step 2: Create an Event in Publisher Class
class Publisher
{
    private DelegateTypeName eventVariable;

    public event DelegateTypeName EventName
    {
        add
        {
            eventVariable += value;
        }

        remove
        {
            eventVariable -= value;
        }
    }
}

// Step 3: Raise the event in Publisher Class
if (EventName != null)
    EventName(arg1, arg2, ...);

// Step 4: Create Event Handler Method in Subscriber Class
class Subscriber
{
    public ReturnType EventHandlerMethodName(param1, param2, ...)
    {
        // Method body here
    }
}

// Step 5: Subscribe to the Event (Inside or Outside Subscriber Class)
EventName += EventHandlerMethodName;
```

Auto Implemented Event:

"Auto-Implemented Events" provide a shortcut syntax to create events with less code.

- In this case, you need not create "add" and "remove" accessors; the compiler does the same automatically.
- **Disadvantage**: We can't define custom logic for "add accessor" and "remove accessor".

```csharp
class Publisher
{
    public event MyDelegateType MyEvent;
}
```

## Anonymous Functions

### Anonymous Method

Anonymous methods are "name-less methods" that can be invoked by using the delegate variable or an event.

- Anonymous methods can be used anywhere within the method, to create methods instantly, without defining a method at the class level.
- **Advantage**: We need not create a "named method (normal method)" to quickly handle an event.
- It can't be called without a delegate or event.
- It can't contain jump statements like `goto`, `break`, or `continue`.
- It can access local variables and parameters of the outer method.
- It can be passed as a parameter to any method; in this case, the delegate acts as the data type for the anonymous method.
- It can't access `ref` or `out` parameters of an outer method.
- It is mainly used for event handlers.

```csharp
// Subscribe to event with anonymous method
EventName += delegate(param1, param2, ...)
{
    // method body here
}
```

!!! warning

    **Important note**: don't use it, instead use "lambda expressions"

### Lambda Expressions

"Lambda Expressions" (a.k.a. Statement Lambda) are "name-less methods", that can be invoked by using the delegate variable or an event, much like anonymous methods.

```csharp
// Handle event with lambda expressions
EventName += (param1, param2, ...) =>
{
    // method body here
};
```

- Lambda Expressions can be used anywhere within the method, to create methods instantly, without defining a method at the class level.
- **Advantage 1**: It provides an easier and more convenient syntax than "Anonymous methods".
- **Advantage 2**: It provides a more convenient syntax to create smaller methods that perform a single calculation or condition check.
- The `=>` operator is called the "goes to" or "goes into" operator.
- A lambda expression (or lambda function) can have a return type before the list of parenthesized parameters:
- Inline lambdas can receive one or more arguments and must return a value.
- Lambda function return type in C# 10:

   ```csharp
   return_type (Parameters_list) => return_value;
   ```

### Static Anonymous Function

A static anonymous function is an anonymous method or lambda expression, prefixed with the `static` keyword.

It **CAN'T** access the state (local variables, parameters, `this` keyword, and `base` keyword) of the enclosing method, and also **CAN'T** access instance members of the enclosing type.

Static anonymous function (Anonymous Method):

```csharp
static delegate(Parameters_list)
{
    // can't access locals, parameters, instance members
    // can access static members and constants
}
```

Static anonymous function (Lambda Expression):

```csharp
static (Parameters_list) =>
{
    // can't access locals, parameters, instance members
    // can access static members and constants
}
```

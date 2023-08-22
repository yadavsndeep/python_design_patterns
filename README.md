# python_design_patterns
Python design patterns 

## Solid Design Principles
### Single responsibility Principle (SRP) / Separation of concern (SOC)
- A class object should have  a single reason for change or a single responsilbility.
- Different classes handling different independent tasks/ problem.

### open Closed Principle (OCP)
-  A class should be open for extension but closed for modification.

### Liskov Substitution Principle (LSP)
- You should be able to substitite a base type with subtype
- Objects of a superclass should be replaceable with objects of its subclasses without breaking the application. In other words, the objects of our subclasses should be behaving the same way as the objects of superclass.

### Interface Segregation Principle (ISP)
- A client should never be forced to implement an interface that it doesn't use, or clients shouldn't be forced to depend on methods they do not use. A software system should be broken down into smaller, more specific interfaces, rather than one large interface that covers all possible functionality.
- Don't put too much into an interface; split into separate interfaces
- YAGNI - You Ain't Going to Need It.

### Dependency Inversion Principle (DIP)
- High-level modules should depend on abstractions rather than concrete implementations. This helps decouple the high-level and low-level modules, making it easier to change the low-level ones without affecting the high-level ones.

# Gamma Categorization
## Creational
- Deal with creation (Construction) of objects
- Explixit(constructor) vs implicit( Dependency injection, reflection etc.)
- Wholesale (single statement) vs piecewise( step-by-step)
##

    Builder - When piecewise object construction is complicated, BP provides an API for doing it succinctly.
    Factories
        Factory Method
        Abstract Factory
    Prototype
    Singleton


## Structural
- Concerned with structures ( eg. class memebers)
- Many patterns are wrappers that mimic underlying class' inteface
- Stress the importance of good API design
##


    Adapter
    Bridge
    Composite
    Decorator
    Facade
    Flyweight
    Proxy


## Behavioral
- They are all different, don't ahve any common theme
##
    Chain or responsibility
    Command
    Interpreter
    Iterator
    Mediator
    Memento
    Observer
    State
    Strategy
    Template Method
    Visitor
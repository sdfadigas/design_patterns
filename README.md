
## Design Patterns

## Table of contents

- [Concept](#concept)
- [Types of design patterns](#types-of-design-patterns)
  - [Creational](#creational)
    - [Singleton](#singleton)
    - [Factory](#factory)
    - [Abstract Factory](#abstract-factory)
    - [Builder](#builder)
  - [Structural](#structural)
    - [Adapter](#adapter)
    - [Decorator](#decorator)
    - [Facade](#facade)
    - [Proxy](#proxy)
  - [Behavioral](#behavioral)
    - [Command](#command)
    - [Mediator](#mediator)
    - [Observer](#observer)
    - [Strategy](#strategy)
    - [Template Method](#template-method)

## Concept
Design patterns are a set of solutions to common problems that arise during the design and development of software applications. They are based on best practices, experience, and expertise from the software engineering community. Design patterns provide developers with proven ways to solve problems and improve the quality, maintainability, and extensibility of their code.  

There are three types of design patterns: **creational**, **structural**, and **behavioral** patterns. Each type focuses on different aspects of software design.

## Types of design patterns
### **Creational**
Creational patterns are design patterns that are concerned with the creation of objects. They provide a way to create objects in a flexible and extensible way, and help to manage the complexity of object creation. There are several types of creational patterns, each with its own advantages and use cases. In class I studied these four creational patterns:

#### [_**Singleton**_](https://github.com/sdfadigas/design_patterns/tree/main/singleton)
The Singleton pattern is a creational pattern that ensures that only one instance of a class is created. This pattern is useful when there is a need to ensure that there is only one instance of a particular object in the entire application. The Singleton pattern provides a global point of access to that instance, which can be used by other objects in the system.  

#### [_**Factory**_](https://github.com/sdfadigas/design_patterns/tree/main/factory%20method)
The Factory pattern is a creational pattern that provides a way to create objects without exposing the creation logic to the client. The client requests an object from the factory, and the factory creates the object using the appropriate logic, providing the client with a new instance of the requested object. This pattern is useful when there is a need to create objects of different types in a flexible and extensible way.

#### [_**Abstract Factory**_](https://github.com/sdfadigas/design_patterns/tree/main/abstract%20factory)
The Abstract Factory pattern is a creational pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is useful when there is a need to create objects that belong to different classes, but share a common theme.
#### [_**Builder**_](https://github.com/sdfadigas/design_patterns/tree/main/builder)
The Builder pattern is a creational pattern that provides a way to create complex objects step by step. The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations of the object. This pattern is useful when there is a need to create objects with a large number of possible configurations.

### **Structural**
Structural patterns are design patterns that are concerned with the composition of classes and objects. They help to identify relationships between classes and objects, and provide a way to modify the composition of objects dynamically. There are several types of structural patterns, each with its own advantages and use cases. In class I studied these four structural patterns:

#### [_**Adapter**_](https://github.com/sdfadigas/design_patterns/tree/main/adapter)
The Adapter pattern is a structural pattern that allows incompatible interfaces to work together. This pattern provides a way to make two incompatible interfaces work together by creating an adapter object that acts as a bridge between them. This pattern is useful when there is a need to reuse existing code that cannot be directly integrated into the current system.

#### [_**Decorator**_](https://github.com/sdfadigas/design_patterns/tree/main/decorator)
The Decorator pattern is a structural pattern that allows adding behavior to an object dynamically, without changing its interface. This pattern provides a way to attach additional responsibilities to an object dynamically, without changing the interface of the original object. This pattern is useful when there is a need to add behavior to objects at runtime.

#### [_**Facade**_](https://github.com/sdfadigas/design_patterns/tree/main/façade)
The Facade pattern is a structural pattern that provides a simplified interface to a complex system. This pattern provides a way to simplify the interface of a complex system, allowing clients to interact with the system in a more intuitive way. This pattern is useful when there is a need to hide the complexity of a system from clients.

#### [_**Proxy**_](https://github.com/sdfadigas/design_patterns/tree/main/proxy)
The Proxy pattern is a structural pattern that provides a way to control access to an object. This pattern provides a way to create a surrogate for an object, allowing clients to interact with the surrogate instead of the original object. This pattern is useful when there is a need to control access to an object, or when creating an object is an expensive operation.

### **Behavioral**
Behavioral patterns are design patterns that focus on communication between objects and classes, and the delegation of responsibilities among them. These patterns provide a way to encapsulate behaviors and algorithms, making them easier to reuse and modify. There are several types of behavioral patterns, each with its own advantages and use cases. In class I studied these five behavioral patterns:

#### [_**Command**_](https://github.com/sdfadigas/design_patterns/tree/main/command)
The Command pattern is a behavioral pattern that encapsulates a request as an object, allowing the request to be queued, logged, or undone. This pattern provides a way to decouple the object that invokes a request from the object that performs it, allowing requests to be treated as objects. This pattern is useful when there is a need to support undo and redo operations, or when requests need to be logged for auditing purposes.

#### [_**Mediator**_](https://github.com/sdfadigas/design_patterns/tree/main/mediator)
The Mediator pattern is a behavioral pattern that defines an object that encapsulates how a set of objects interact. This pattern provides a way to reduce the dependencies between objects, allowing them to be more loosely coupled. This pattern is useful when there are a large number of objects that need to interact with each other.

#### [_**Observer**_](https://github.com/sdfadigas/design_patterns/tree/main/observer)
The Observer pattern is a behavioral pattern that defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically. This pattern provides a way to decouple objects that need to be notified of changes in state, allowing them to be more loosely coupled. This pattern is useful when there is a need to maintain consistency between objects that have a relationship.

#### [_**Strategy**_](https://github.com/sdfadigas/design_patterns/tree/main/strategy)
The Strategy pattern is a behavioral pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern provides a way to encapsulate algorithms and make them easily interchangeable, making it easier to modify or extend the behavior of an object. This pattern is useful when there is a need to change the behavior of an object dynamically.

#### [_**Template Method**_](https://github.com/sdfadigas/design_patterns/tree/main/template%20method)
The Template Method pattern is a behavioral pattern that defines the skeleton of an algorithm in a base class, allowing subclasses to provide concrete implementations of some of the steps. This pattern provides a way to define a basic algorithm structure, allowing it to be customized by subclasses. This pattern is useful when there is a need to define a common algorithm structure that can be customized by subclasses.

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass  # Abstract method

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows!")

dog = Dog("Buddy")  # Creating a Dog object
dog.make_sound()  # Output: Buddy barks!

cat = Cat("Whiskers")  # Creating a Cat object
cat.make_sound()  # Output: Whiskers meows!

# Output - Buddy barks!
# Whiskers meows!


"""
This code defines an example of abstraction in Python using an abstract class (Animal) and its subclasses (Dog and Cat). Below is the detailed explanation of each component and how abstraction is implemented in the code.

Key Concepts:
Abstraction: This is achieved by using abstract classes and methods. It allows you to define a common interface (methods) for a group of subclasses while hiding the internal implementation details of each subclass.
Inheritance: The subclasses (Dog and Cat) inherit from the abstract class Animal, which defines common functionality that must be implemented in the subclasses.
Code Breakdown:
1. Abstract Base Class (ABC) and Abstract Method

from abc import ABC, abstractmethod
The abc module stands for Abstract Base Class and is used to define abstract classes in Python.
The ABC is inherited by any class that wants to be treated as abstract.
@abstractmethod is a decorator that marks a method as abstract, meaning any subclass inheriting this class must implement this method.
2. Class Animal: The Abstract Class

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass  # Abstract method
Animal Class: This is an abstract class that cannot be instantiated directly. It serves as a blueprint for its subclasses.
__init__() Method: This is a constructor that initializes the name attribute for each Animal. Every object of the Animal class (or its subclass) will have a name.
self.name = name: This line sets the name of the animal when an object is created.
make_sound() Method: This is an abstract method decorated with @abstractmethod, meaning it is only declared here but not implemented. Every subclass of Animal must provide its own implementation of make_sound().
3. Class Dog: A Subclass of Animal

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks!")
Inherits from Animal: The Dog class is a subclass of Animal, meaning it inherits the __init__() method and must provide an implementation for the make_sound() method.
make_sound() Implementation: The method make_sound() is implemented specifically for Dog, where it prints a message indicating that the dog is barking.
f"{self.name} barks!": Uses an f-string to include the dog's name in the message. For example, if the dog's name is "Max", the output will be "Max barks!".
4. Class Cat: Another Subclass of Animal

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows!")
Inherits from Animal: The Cat class also inherits from Animal and must implement the make_sound() method.
make_sound() Implementation: The method is implemented for Cat, where it prints a message indicating that the cat is meowing.
f"{self.name} meows!": If the cat’s name is "Whiskers", the output will be "Whiskers meows!".
How the Code Works:
When you create an object of Dog or Cat, the __init__() method from the Animal class is called, and the animal's name is stored in self.name.
The abstract method make_sound() is implemented differently in the Dog and Cat subclasses, allowing you to have different behavior for each type of animal.
You cannot create an object directly from the Animal class because it contains an abstract method (make_sound()).
Example Usage:
Let’s see how you might use this code:


dog = Dog("Buddy")  # Creating a Dog object
dog.make_sound()  # Output: Buddy barks!

cat = Cat("Whiskers")  # Creating a Cat object
cat.make_sound()  # Output: Whiskers meows!
Creating Objects:
Dog("Buddy"): This creates a Dog object with the name "Buddy". The __init__() method from Animal is called to initialize self.name.
Cat("Whiskers"): This creates a Cat object with the name "Whiskers".
Calling Methods:
dog.make_sound() calls the make_sound() method of the Dog class, printing "Buddy barks!".
cat.make_sound() calls the make_sound() method of the Cat class, printing "Whiskers meows!".
Why Abstraction is Important (Interview Perspective):
Encapsulation of Behavior: In this example, the abstract method make_sound() enforces that any animal (subclass) must have a sound, but the exact sound (implementation) is determined by the subclass (Dog barks, Cat meows).
Code Reusability: The Animal class provides a common template for all animals, so you don’t need to rewrite the constructor (__init__()) for each new animal subclass.
Scalability: If you want to add more animals (e.g., Cow, Lion), you can easily do that by creating new subclasses and implementing the make_sound() method without modifying existing code.
Important Points for Interviews:
Abstract Classes are meant to be inherited and provide a structure for other classes.
Abstract Methods force subclasses to provide specific implementations, promoting consistency in the design.
Polymorphism: Although the Dog and Cat classes share the same method name (make_sound()), they exhibit different behavior when the method is called.
This design pattern is common when you want to define a common interface but leave the details to the subclasses.

Here, Animal is an abstract class with an abstract method make_sound(). Concrete classes like Dog and Cat inherit from Animal, provide implementations for make_sound(), and override the __init__() method if needed.
Theoretical Advantages:
•	Reduced Complexity: Abstract classes help you hide implementation details, simplifying your code.
•	Improved Reusability: By defining common functionality in an abstract class, you can create reusable components that other classes can inherit from.
•	Enforced Consistency: Enforces subclasses to implement essential behaviors.
•	Polymorphism: Abstract classes facilitate polymorphism, where objects of different subclasses can be treated uniformly using the same interface (abstract class).
•	.

Example (continued):
In the previous example, Dog and Cat are concrete classes. You can create objects like:
Python
fido = Dog("Fido")
fido.make_sound()  # Output: Fido barks!
Theoretical Advantages:
•	Flexibility: Concrete classes offer the flexibility to tailor behavior based on their specific purpose.
•	Usability: They are the building blocks that you directly interact with in your code.
Key Points:
•	Abstract classes define what a class must do, while concrete classes define how to do it.
•	Use abstract classes for common functionality and concrete classes for specific implementations.
•	They work together to create a well-structured and maintainable codebase.

"""


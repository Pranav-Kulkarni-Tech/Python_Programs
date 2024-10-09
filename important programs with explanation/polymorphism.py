# Base class (superclass)
class Animal:
    def speak(self):
        return "Animal speaks"

# Derived class 1 (subclass)
class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Derived class 2 (subclass)
class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Polymorphism in action
def animal_sound(animal):
    print(animal.speak())

# Create objects
dog = Dog()
cat = Cat()

# Call the function and pass objects
animal_sound(dog)  # Output: Dog barks
animal_sound(cat)  # Output: Cat meows

"""
Class Animal:

The Animal class defines a method speak(), which prints "Animal speaks". This method is meant to be overridden by subclasses to provide specific behavior for each animal.
Class Dog (Subclass of Animal):

The Dog class inherits from the Animal class.
It overrides the speak() method. When the speak() method is called on a Dog object, it returns "Dog barks" instead of the generic "Animal speaks".
Class Cat (Subclass of Animal):

Similar to Dog, the Cat class also inherits from Animal and overrides the speak() method to return "Cat meows".
Polymorphism:

In the function animal_sound(animal), we are passing an Animal object (or any of its subclasses, like Dog or Cat) and calling the speak() method.
Thanks to polymorphism, even though we are calling speak() from the superclass Animal, the program knows which subclass’s method (i.e., Dog or Cat) to call based on the object we pass to the function.
This is runtime polymorphism because the method that gets executed is determined at runtime based on the type of object passed.

Key Points:
Method Overriding: Polymorphism is achieved through method overriding, where a subclass provides its own implementation of a method that’s already defined in its superclass.

Dynamic Method Dispatch: The method call is dynamically resolved at runtime. When you call animal.speak(), it resolves to Dog or Cat depending on the type of object, which is not known until the program is running.

Reusability: Polymorphism allows the code to be flexible and reusable. You can call the same method (speak()) on different objects (Dog, Cat) and get the appropriate behavior.

Polymorphism allows different classes to have methods with the same name but different implementations. The method that gets executed depends on the object, even if the method is called using a reference to the superclass. This concept is particularly useful when working with large systems because it promotes flexibility and reusability of code. Method overriding is the key mechanism to achieve polymorphism in object-oriented programming.

Polymorphism allows objects of different types to be treated as instances of the same superclass. In other words, the same operation can behave differently on different classes of objects.
"Poly" means many, and "morph" means forms. So, polymorphism means "many forms.

Method Overriding is used to achieve this. In this, a subclass provides its own implementation of a method that is already defined in its superclass.
Example: A speak() method in both Dog and Cat classes overriding the speak() method of the Animal class.

When a method is called on an object, polymorphism ensures that the correct method (based on the object's actual type) is executed, even if the method is defined in a parent class.
Polymorphism often relies on inheritance and interfaces to provide different implementations of the same operation.

Advantages of Polymorphism:
Flexibility and Reusability: Polymorphism allows code to be more flexible and reusable. You can write more generic code that works with objects of different types and still behave correctly.
Extensibility: New types can be added to a system without modifying existing code. For example, if a new Bird class inherits from Animal and overrides speak(), the existing code using Animal will automatically work with Bird.
Cleaner Code: It allows you to write cleaner and more understandable code by defining a common interface for different types of objects.
"""
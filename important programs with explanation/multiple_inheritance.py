class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Max Speed: {self.max_speed} km/h")


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display_engine(self):
        print(f"Engine Type: {self.engine_type}")


# Multiple inheritance: Car inherits from both Vehicle and Engine
class Car(Vehicle, Engine):
    def __init__(self, name, max_speed, engine_type, doors):
        # Calling __init__ of Vehicle class using super()
        super().__init__(name, max_speed) # this are  above class variable
        
        # Calling __init__ of Engine class explicitly
        Engine.__init__(self, engine_type)
        
        self.doors = doors # this is car class attribute this is new variable.

    def display_info(self):
        # Calling the display_info method from Vehicle using super()
        super().display_info()
        # Display additional information specific to the Car class
        print(f"Number of Doors: {self.doors}")
        # Display engine information from the Engine class
        super(Car, self).display_engine()  # Explicitly calling display_engine from Engine

# Creating a Car object
my_car = Car("Tesla Model S", 250, "Electric", 4)

# Displaying all the information
my_car.display_info()
"""
Explanation of the Code:
Vehicle Class:

This class has two attributes: name (vehicle name) and max_speed (maximum speed of the vehicle).
The __init__() constructor initializes these attributes, and the display_info() method prints the information about the vehicle.
Engine Class:

The Engine class has one attribute, engine_type, which stores the type of engine.
It has a display_engine() method that prints the engine type.
Car Class:

This class inherits from both Vehicle and Engine (multiple inheritance).
The __init__() constructor of the Car class:
Uses super().__init__(name, max_speed) to call the constructor of the Vehicle class. This initializes the name and max_speed attributes from Vehicle.
Calls Engine.__init__(self, engine_type) explicitly to initialize the engine_type attribute from Engine. Here, we can't use super() directly to call Engine's __init__() due to multiple inheritance.
Initializes its own attribute doors to store the number of doors for the car.
The display_info() method:
Calls super().display_info() to print the vehicle information from the Vehicle class.
Prints additional car-specific information like the number of doors.
Uses super(Car, self).display_engine() to call the display_engine() method from the Engine class to display the engine type.


Let's break down this program step by step and understand the key concepts, especially focusing on the use of super() and why super(Car, self).display_engine() is explicitly used in the Car class.

1. Class Definitions:
Vehicle Class:

This class has two attributes, name and max_speed, initialized via the __init__() method.
It also contains the method display_info() which prints the vehicle's name and maximum speed.
Engine Class:

The Engine class has one attribute, engine_type, also initialized in its __init__() method.
It contains a method display_engine() which prints the engine type.
2. Multiple Inheritance:
The Car class inherits from both Vehicle and Engine, which means it inherits the properties and methods from both these classes.

The Car class defines its own __init__() method where it:
Calls the Vehicle class's __init__() method using super() to initialize the name and max_speed attributes.
Explicitly calls Engine.__init__(self, engine_type) to initialize the engine_type attribute from the Engine class.
Initializes its own attribute doors, which is specific to the Car class.
3. Initialization in the Car Class:
In the __init__() method of Car:


super().__init__(name, max_speed)  # Calls Vehicle's __init__
Engine.__init__(self, engine_type)  # Explicitly calls Engine's __init__
super().__init__(name, max_speed): This calls the __init__() method of the first parent class in the method resolution order (MRO), which is Vehicle. So, name and max_speed are initialized via Vehicle.__init__().

Engine.__init__(self, engine_type): This explicitly calls the __init__() method of the Engine class to initialize the engine_type. Since super() doesn’t automatically handle multiple parents in Python, this explicit call is necessary to ensure that Engine.__init__() is executed.

4. Method Overriding in the Car Class:
The Car class also overrides the display_info() method, adding its own logic to display additional information:


def display_info(self):
    super().display_info()  # Calls Vehicle's display_info method
    print(f"Number of Doors: {self.doors}")  # Prints Car-specific attribute
    super(Car, self).display_engine()  # Calls Engine's display_engine method
super().display_info(): This calls the display_info() method from the Vehicle class, which prints the vehicle's name and maximum speed.

print(f"Number of Doors: {self.doors}"): This is Car-specific logic, displaying the number of doors.

5. super(Car, self).display_engine():
Now, the important line:


super(Car, self).display_engine()
This is an explicit call to the display_engine() method from the Engine class. Here’s what’s happening:

super(Car, self): This form of super() tells Python to look for the method display_engine() in the next class in the MRO after Car. Normally, Python follows MRO and goes in the inheritance order (starting with Vehicle). However, since we explicitly specified super(Car, self), we are asking Python to look for display_engine() in Engine, which is another parent of Car.
In simpler terms:

super(Car, self) directs Python to start looking for the display_engine() method not in the immediate parent (Vehicle), but in the class hierarchy of Car, bypassing the normal MRO order.
Why is super(Car, self) used?
This form of super() is used to ensure that we are explicitly calling the Engine class's display_engine() method, as Python’s normal MRO would look for methods in Vehicle first. We could also directly call self.display_engine(), but this form of super() ensures that the method is being correctly resolved according to the MRO.
6. Object Creation:

my_car = Car("Tesla Model S", 250, "Electric", 4)
Here, an instance of the Car class is created:

name is "Tesla Model S".
max_speed is 250.
engine_type is "Electric".
doors is 4.
7. Method Call:

my_car.display_info()
This first calls super().display_info(), which invokes Vehicle's display_info(), printing the vehicle name and max speed.
Then, it prints the number of doors specific to the Car class.
Finally, super(Car, self).display_engine() ensures that Engine's display_engine() method is called, printing the engine type.
Output:

Vehicle Name: Tesla Model S
Max Speed: 250 km/h
Number of Doors: 4
Engine Type: Electric
Conclusion:
super() is used to handle the MRO and allow clean inheritance.
The explicit call to Engine.__init__() is necessary because Python doesn’t automatically initialize multiple parent classes.
The super(Car, self).display_engine() ensures that we’re explicitly calling the Engine class’s method rather than relying on MRO to resolve the method.
By understanding this flow, you gain control over how classes in a multiple inheritance scenario interact with each other!
"""
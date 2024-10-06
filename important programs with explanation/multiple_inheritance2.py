class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self):
        print(f"Driving at {self.speed} km/h.")

# Multiple inheritance: Robot inherits from both Animal and Vehicle
class Robot(Animal, Vehicle):
    def __init__(self, name, speed):
        Animal.__init__(self, name)  # Initializing Animal's attributes
        Vehicle.__init__(self, speed)  # Initializing Vehicle's attributes

    def display_info(self):
        print(f"Robot Name: {self.name}")
        print(f"Speed: {self.speed} km/h")

# Creating an object of Robot
my_robot = Robot("Robo", 100)

# Using methods from both Animal and Vehicle
my_robot.speak()  # Output: Robo makes a sound.
my_robot.drive()  # Output: Driving at 100 km/h.
my_robot.display_info()  # Output: Robot Name: Robo, Speed: 100 km/h


"""
Explanation:
Animal Class: Defines an animal with a name and a method speak() to print a message.
Vehicle Class: Defines a vehicle with a speed and a method drive() to print its speed.
Robot Class: Inherits from both Animal and Vehicle, meaning it can use methods from both classes. The Robot class also adds its own method display_info() to print more details about the robot.

"""
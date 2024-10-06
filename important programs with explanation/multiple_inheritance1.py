# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Base class 2
class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

# Derived class (inheriting from both Person and Employee)
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        # Initializing the Person class
        Person.__init__(self, name, age)
        # Initializing the Employee class
        Employee.__init__(self, employee_id, department)
        self.team_size = team_size

    def display_manager_info(self):
        # Display information from both base classes
        self.display_person_info()
        self.display_employee_info()
        # Display Manager-specific information
        print(f"Team Size: {self.team_size}")

# Create an object of the Manager class
manager = Manager("John Doe", 35, "M1234", "IT", 10)

# Display manager information
manager.display_manager_info()
"""
Name: John Doe
Age: 35
Employee ID: M1234
Department: IT
Team Size: 10


Explanation:
Person Class: Contains basic personal information (name and age) and a method display_person_info() to print that information.
Employee Class: Contains employee information (employee_id and department) and a method display_employee_info() to print that.
Manager Class: Inherits from both Person and Employee. It combines information from both classes and adds a new attribute team_size. It also defines a method display_manager_info() to display all the combined information.

"""
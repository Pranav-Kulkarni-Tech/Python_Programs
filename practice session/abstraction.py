from abc import ABC, abstractmethod 

class animal(ABC):
    def __init__(self, name):
        self.name=name

    @abstractmethod
    def vehicle(self):
        pass

class owl(animal):
    def vehicle(self):
        print(f"laxmi ma {self.name}")

class boy(animal):
    def vehicle(self):
        print(f"{self.name} improve yourself ")


class gaay(animal):
    def vehicle(self):
        print(f"{self.name} tells improve yourself pranva")



obj=owl('white')
obj.vehicle()

obj=boy('pranav')
obj.vehicle()

obj=gaay('shahani gaay')
obj.vehicle()
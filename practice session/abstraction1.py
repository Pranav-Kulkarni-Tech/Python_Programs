from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name=name


    @abstractmethod
    def Color(self):
        pass


class Cow(Animal):
    def Color(self):
        print(f"color of {self.name} is white")


class Owl(Animal):
    def Color(self):
        print(f"color of {self.name} is grey")


cw=Cow("mycow")
cw.Color()

ol=Owl("myowl")
ol.Color()



    
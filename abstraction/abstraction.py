#   Module that provides the base for defining Abstract Base Classes(ABC)
from abc import ABC, abstractmethod

class vehicle(ABC):
    #   regular method
    def what(self):
        print("How many wheels do I have?")

    #   A method becomes abstract when decorated with they keyword @abstractmethod
    @abstractmethod
    def numofwheels(self):
        pass

class car(vehicle):
    #   overrides abstract method
    def numofwheels(self):
        print("I am a car. I have 4 wheels!")

class motorcyle(vehicle):
    #   overrides abstract method
    def numofwheels(self):
        print("I am a motorcyle. I have 2 wheels!")

obj = car()
obj.what()
obj.numofwheels()

obj2 = motorcyle()
obj2.what()
obj2.numofwheels()



    

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod  #we can not make objects of abstractbaseclass

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class rectangle(Shape):
    type = "rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 4


    def printarea(self):
        return self.length * self.breadth

rect1 = rectangle()
print(rect1.printarea())
tryobj = Shape()
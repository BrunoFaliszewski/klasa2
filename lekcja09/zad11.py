from abc import ABC, abstractmethod
import math

class Figure(ABC):

    def __init__(self):
        self.area = 0
        self.perimeter = 0
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, name="No name", a=0, b=0):
        self.a = a
        self.b = b
        self.name = name
        super().__init__()
        self.calc_area()
        self.calc_perimeter()

    def calc_area(self):
        self.area = self.a * self.b

    def calc_perimeter(self):
        self.perimeter = 2 * self.a + 2 * self.b
    
    def __str__(self):
        info_str = f"""
            Rectangle:  {self.name}
            Dimensions: {self.a} x {self.b}
            Area: {self.area}
            Perimeter: {self.perimeter}
            """
        return info_str
    
class Triangle(Figure):
    def __init__(self, name="No name", a=0, h=0):
        self.a = a
        self.h = h
        self.name = name
        super().__init__()
        self.calc_area()
        self.calc_perimeter()
    
    def calc_area(self):
        self.area = self.a * self.h / 2

    def calc_perimeter(self):
        self.perimeter = self.a + 2 * (math.sqrt((self.a/2)**2 + self.h**2))
    
    def __str__(self):
        info_str = f"""
            Triangle:  {self.name}
            Dimensions: {self.a} x {self.h}
            Area: {self.area}
            Perimeter: {self.perimeter}
            """
        return info_str

class Square(Figure):
    def __init__(self, name="No name", a=0):
        self.a = a
        self.name = name
        super().__init__()
        self.calc_area()
        self.calc_perimeter()
    
    def calc_area(self):
        self.area = self.a**2

    def calc_perimeter(self):
        self.perimeter = self.a * 4
    
    def __str__(self):
        info_str = f"""
            Square:  {self.name}
            Dimensions: {self.a} x {self.a}
            Area: {self.area}
            Perimeter: {self.perimeter}
            """
        return info_str

T1 = Triangle("t1", 6, 4)
print(T1)
R1 = Rectangle("r1", 5, 4)
print(R1)
S1 = Square("s1", 3)
print(S1)
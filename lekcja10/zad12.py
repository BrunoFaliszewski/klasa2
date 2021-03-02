import math


class Vector:
    @classmethod
    def create_from_Cartesian_coordinates(cls, name="No name", x=0, y=0):
        return cls(name, x, y)

    @classmethod
    def create_from_polar_coordinates(cls, name="No name", r=0, theta=0):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return cls(name, x, y)

    def __init__(self, name="No name", x=0, y=0):
        self._x = x
        self._y = y
        self._name = name
        print(
            f"Wektor {self._name} o współrzędnych ({self._x}, {self._y}) został utworzony")

    def __del__(self):
        print(
            f"Wektor {self._name} o współrzędnych ({self._x}, {self._y}) został usunięty")

    @property
    def length(self):
        return math.sqrt(self._x**2 + self._y**2)

    @property
    def angle(self):
        return (math.acos(self._x/self.length)) * (180/math.pi)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __str__(self):
        _str = f"Wektor {self._name} ({self._x}, {self._y})"
        return _str

    def __add__(self, other):
        v = Vector.create_from_Cartesian_coordinates(
            "Vadd", self.x + other.x, self.y + other.y)
        return v
    
    def __sub__(self, other):
        v = Vector.create_from_Cartesian_coordinates(
            "Vsub", self.x - other.x, self.y - other.y)
        return v

    def __mul__(self, other):
        if(isinstance(other, int) or isinstance(other, float)):
            v = Vector.create_from_Cartesian_coordinates(
                "Vmul", self.x * other, self.y * other)
            return v
        else:
            raise TypeError("To nie jest mnożenie wektora przez liczbę!")
    
    def scalarmul(self, other):
        return self._x * other.x + self._y * other.y


v1 = Vector.create_from_Cartesian_coordinates("V1", 1, 2)
v2 = Vector.create_from_Cartesian_coordinates("V2", 3, 4)

print(v1)
print(v2)

v3 = v1 + v2
print(v3)

v4 = v1 * 2
print(v4)

v5 = v2 - v1
print(v5)

print(v2.length)
print(v2.angle)
print(v1.scalarmul(v2))
print(v4.scalarmul(v5))
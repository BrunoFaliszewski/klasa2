import math

class Vector:
    number_of_vectors = 0

    @classmethod
    def get_number_of_vectors(cls):
        return cls.number_of_vectors
    
    @classmethod
    def create_from_polar_coordinates(cls, r=0, theta=0):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return cls(x, y)

    @classmethod
    def create_from_cartesian_coordinates(cls, x=0, y=0):
        return cls(x, y)

    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
        Vector.number_of_vectors += 1
    
    def get_vector_distance(self, distance = 0):
        self.distance = math.sqrt(self._x**2 + self._y**2)
        return self.distance

    def __del__(self):
        Vector.number_of_vectors -= 1

def fun():
    vector1 = Vector.create_from_cartesian_coordinates(3, 4)
    print(f"Długość tego wektora to {vector1.get_vector_distance()}")
    print(f"Liczba wektorów to {Vector.get_number_of_vectors()}")

vector2 = Vector.create_from_polar_coordinates(10, 60)
fun()
print(f"Liczba wektorów to {Vector.get_number_of_vectors()}")
print(f"Długość tego wektora to {vector2.get_vector_distance()}")


import numpy as np
from Function import Function


class CubicFunction(Function):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = []
        self.y = []
        self.step = 1
        self.x_min = 0
        self.x_max = 0
        self.type = "cubic"
        self.info = f"f(x) = {self.a}*x**3 + {self.b}*x**2 + {self.c}*x + {self.d}"

    def set_x_range(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def set_step(self, step):
        self.step = step

    def calculate(self):
        self.x.clear()
        self.y.clear()
        self.x = list(np.arange(self.x_min, self.x_max, self.step))
        self.y = [self.a*x**3+self.b*x**2+self.c*x+self.d for x in self.x]

    @classmethod
    def create_function(cls, **kwargs):
        if 'a' in kwargs and 'b' in kwargs and 'c' in kwargs and 'd' in kwargs:
            a = int(kwargs['a'])
            b = int(kwargs['b'])
            c = int(kwargs['c'])
            d = int(kwargs['d'])
            return CubicFunction(a, b, c, d)
        else:
            raise Exception(
                "You should pass 'a', 'b', 'c' and 'd' parameters to cubic function")

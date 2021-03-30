import numpy as np
import math
from Function import Function


class LogarithmicFunction(Function):
    def __init__(self, a):
        self.a = a
        self.x = []
        self.y = []
        self.step = 1
        self.x_min = 0
        self.x_max = 0
        self.type = "logarithmic"
        self.info = f"f(x) = log(x, {self.a})"

    def set_x_range(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def set_step(self, step):
        self.step = step

    def calculate(self):
        self.x.clear()
        self.y.clear()
        self.x = list(np.arange(self.x_min, self.x_max, self.step, dtype=float))
        self.y = [math.log(math.abs(x), float(self.a)) for x in self.x]

    @classmethod
    def create_function(cls, **kwargs):
        if 'a' in kwargs:
            a = int(kwargs['a'])
            return LogarithmicFunction(a)
        else:
            raise Exception(
                "You should pass 'a' parameter to logarithmic function")

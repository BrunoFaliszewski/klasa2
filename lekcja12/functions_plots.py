from LinearFunction import LinearFunction
from SquareFunction import SquareFunction
from FunctionsSet import FunctionsSet
# from Function import Function
from FunctionsPlot import FunctionsPlot


# funkcja1 = LinearFunction(2, 3)
funkcja1 = LinearFunction.create_function(a=2, b=3)
# funkcja2 = SquareFunction(2, 3, 4)
funkcja2 = SquareFunction.create_function(a=2, b=3, c=4)
funkcja3 = LinearFunction.create_function(a=1, b=1)

zbior_funkcji = FunctionsSet()
wykresy_funkcji = FunctionsPlot(zbior_funkcji)
zbior_funkcji.add_function(funkcja1)
zbior_funkcji.add_function(funkcja2)
zbior_funkcji.add_function(funkcja3)
zbior_funkcji.delete_function(funkcja3)

wykresy_funkcji.set_x_range(-5, 5)
# wykresy_funkcji.set_y_range(-20, 30)
wykresy_funkcji.set_step(0.1)

wykresy_funkcji.plot()

from LinearFunction import LinearFunction
from SquareFunction import SquareFunction
from CubicFunction import CubicFunction
from ExponentialFunction import ExponentialFunction
from LogarithmicFunction import LogarithmicFunction
from FunctionsSet import FunctionsSet
# from Function import Function
from FunctionsPlot import FunctionsPlot
from Menu import display_menu, display_add_function_menu, return_new_float_value_or_previous_one, return_not_empty_new_string_or_previous_one


print('Program rysujący wykresy funkcji.')
zbior_funkcji = FunctionsSet()
wykresy_funkcji = FunctionsPlot(zbior_funkcji)
x_min = -10
x_max = 10
y_min = -10
y_max = 10
step = 0.1
file_name = "data.dat"


while(True):
    menu_selection = display_menu()
    if menu_selection == 1:  # dodawanie funkcji
        while(True):
            menu_add_function_selection = display_add_function_menu()
            if menu_add_function_selection == 1:
                a = float(input("Podaj wartość parametru 'a': "))
                b = float(input("Podaj wartość parametru 'b': "))
                funkcja = LinearFunction.create_function(a=a, b=b)
                zbior_funkcji.add_function(funkcja)
            elif menu_add_function_selection == 2:
                a = float(input("Podaj wartość parametru 'a': "))
                b = float(input("Podaj wartość parametru 'b': "))
                c = float(input("Podaj wartość parametru 'c': "))
                funkcja = SquareFunction.create_function(a=a, b=b, c=c)
                zbior_funkcji.add_function(funkcja)
            elif menu_add_function_selection == 3:
                a = float(input("Podaj wartość parametru 'a': "))
                b = float(input("Podaj wartość parametru 'b': "))
                c = float(input("Podaj wartość parametru 'c': "))
                d = float(input("Podaj wartość parametru 'd': "))
                funkcja = CubicFunction.create_function(a=a, b=b, c=c, d=d)
                zbior_funkcji.add_function(funkcja)
            elif menu_add_function_selection == 4:
                a = float(input("Podaj wartość parametru 'a': "))
                funkcja = ExponentialFunction.create_function(a=a)
                zbior_funkcji.add_function(funkcja)
            elif menu_add_function_selection == 5:
                a = float(input("Podaj wartość parametru 'a': "))
                funkcja = LogarithmicFunction.create_function(a=a)
                zbior_funkcji.add_function(funkcja)
            else:
                break

    elif menu_selection == 2:  # usuwanie funkcji

        print(zbior_funkcji)
        index = int(input("Którą funkcję chcesz usunąć? "))
        zbior_funkcji.delete_function_by(index)

    elif menu_selection == 3:  # wyświetlanie funkcji
        print(zbior_funkcji)
    elif menu_selection == 4:  # definiowanie parametrów wykresu funkcji
        x_min = return_new_float_value_or_previous_one(
            "Podaj minimalną wartość na osi x", x_min)
        x_max = return_new_float_value_or_previous_one(
            "Podaj maksymalną wartość na osi x", x_max)
        y_min = return_new_float_value_or_previous_one(
            "Podaj minimalną wartość na osi y", y_min)
        y_max = return_new_float_value_or_previous_one(
            "Podaj maksymalną wartość na osi x", y_max)
        step = return_new_float_value_or_previous_one(
            "Podaj krok obliczeń", step)

    elif menu_selection == 5:  # generowanie wykresu funkcji
        wykresy_funkcji.plot()
    elif menu_selection == 6:  # zapisywanie zbioru funkcji do pliku
        file_name = return_not_empty_new_string_or_previous_one(
            "Podej nazwę pliku", file_name)
        zbior_funkcji.save_to_file("data.dat")
    elif menu_selection == 7:  # odczytywanie zbioru funkcji z pliku
        file_name = return_not_empty_new_string_or_previous_one(
            "Podej nazwę pliku", file_name)
        zbior_funkcji.read_from_file("data.dat")
    else:
        break

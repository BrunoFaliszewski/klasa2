def defense_int_input(text, min_val, max_val):
    value = input(text)
    while ((int(min_val) > int(value)) or (int(value) > int(max_val))):
        print('Wartosc musi byc nie mniejsza niz', min_val,
              'i nie wieksza niz', max_val, sep=' ', end='\n')
        value = input(text)

    return int(value)


def display_menu():
    menu_selection = 0
    print('\nMenu:')
    print('1 - Dodawanie funkcji')
    print('2 - Usuwanie funkcji')
    print('3 - Wyswietlanie funkcji')
    print('4 - Definiowanie parametrów wykresu')
    print('5 - Generowanie wykresu')
    print('6 - Zapisywanie zbioru funkcji do pliku')
    print('7 - Odczytywanie zbioru funkcji z pliku')
    print('8 - Koniec programu')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 8)

    return menu_selection


def display_add_function_menu():
    menu_selection = 0
    print('\n')
    print('1 - Dodaj funkcję liniową')
    print('2 - Dodaj funkcję kwadratową')
    print('3 - Dodaj funkcję sześcienną')
    print('4 - Dodaj funkcję wykładniczą')
    print('5 - Dodaj funkcję logarytmiczną')
    print('6 - Wyjdź poziom wyżej')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 6)

    return menu_selection


def return_new_float_value_or_previous_one(info: str, previous_value: float) -> float:
    try:
        value = float(input(f"{info} [{previous_value}]: "))
    except:
        value = previous_value
    return value


def return_not_empty_new_string_or_previous_one(info: str, previous_string: str) -> str:
    string = input(f"{info} [{previous_string}]: ")
    if string:
        return string
    else:
        return previous_string

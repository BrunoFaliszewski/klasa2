print('Ten program oblicza miejsca zerowe dowolnej funkcji liniowej')

a = int(input('Podaj współczynnik kierunkowy twojej funkcji liniowej: '))
b = int(input('Podaj wyraz wolny twojej funkcji liniowej: '))
x1 = 0

if a != 0:
    x1 = -b / a
    print(f'Miejsce zerowe tej funkcji to x = {x1}')
elif b != 0:
    print('Ta funkcja nie ma miejsc zerowych!')
else:
    print('Ta funkcja ma nieskończenie wiele miejsc zerowych!')

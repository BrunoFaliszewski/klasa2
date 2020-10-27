import random
from statistics import median

my_list = []

elements = int(input('Ile elementów ma znajdować się w liście?: '))

while True:
    decision = input("Czy chcesz aby elemnty w liście zostały wygenerowane losowo?[tak/nie]: ")

    if (decision.lower() == "tak"):
        for element in range(elements):
            my_list.append(random.randint(1,100))
        break
    elif (decision.lower() == 'nie'):
        for i in range(elements):
            my_list.append(int(input(f'{i + 1} elemnt: ')))
        break

print(f'Elemnty listy to: {my_list}')
my_list_2 = my_list[:]
my_list_2.sort()
print(f'Posortowana lista to: {my_list_2}')
print(f'Można ją też posortować tak: {sorted(my_list)}')
print(f'Ta lista ma {len(my_list)} elementów')
print(f'Suma elementów tej listy to: {sum(my_list)}')
print(f'Minimalna wartość tej listy to :{min(my_list)}')
print(f'Maksymalna wartość tej listy to :{max(my_list)}')
print(f'Średnia elementów tej listy to: {sum(my_list) / len(my_list)}')
print(f'Mediana elemntów tej listy to: {median(my_list)}')
import random

class Lotto:
    def __init__(self):
        self.numbers = []
        for i in range(6):
            n = random.randint(1,49)
            while n in self.numbers:
                n = random.randint(1,49)
            self.numbers.append(n)

    def show(self):
        print(' '.join([str(i) for i in sorted(self.numbers)]))

    def save(self, filename):
        with open(f'lekcja8/{filename}', 'w') as file:
            file.write(' '.join([str(i) for i in sorted(self.numbers)])+'\n')

l1 = Lotto()
if input('Czy pokazać wyniki losowania?: ').upper() == "TAK":
    l1.show()
i2 = input('Czy zapisać wyniki losowania do pliku lotto.txt?: ').upper()
if i2 == "TAK":
    l1.save('lotto.txt')
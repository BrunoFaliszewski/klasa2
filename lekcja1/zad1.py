import random

guess = 0
number = random.randint(1,10)

while(number != guess):
    guess = int(input('Zgadnij liczbę całkowitą od 1 do 10: '))

    if(number == guess):
        print('zgadłeś!')
    elif(number > guess):
        print('Twoja liczba jest za mała!')
    elif(number < guess):
        print('Twoja liczba jest za duża!')
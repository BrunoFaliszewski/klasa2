def fmin_val():
    min_val = int(input('Podaj minimalną wartość losowanej liczby: '))

    return min_val

def fmax_val():
    import sys
    max_val = int(input('Podaj maksymalną wartość losowanej liczby (nie większą niż 9999): '))

    if max_val > 9999:
        print('Ta liczba jest większa niż 9999')
        sys.exit()
        
    return max_val

def fnliczb():
    nliczb = int(input('Podaj liczbe liczb w jednej próbie: '))

    return nliczb

def fnprob():
    nprob = int(input('Podaj liczbe prób: '))

    return nprob

def wwl(min_val, max_val, nliczb, nprob):
    from random import randint
    x = 0

    while x < nprob:
        y = 0
        while y < nliczb:
            print('{:>4}'.format(randint(min_val, max_val)), end = ' ')
            y += 1
        x += 1
        print()
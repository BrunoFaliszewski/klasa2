import random

def generate(**kwargs):
    minval = kwargs['fminval']
    maxval = kwargs['fmaxval']
    tries = kwargs['ftries']
    values = kwargs['fvalues']
    display = kwargs['fdisplay']
    save = kwargs['fsave']
    fname = kwargs['fname']
    value = []
    
    if(str(display).lower() == 'yes'):
        try:
            for _ in range(tries):
                for _ in range(values):
                    value.append(random.randint(minval, maxval))
                    print(value[-1], end = ' ')
                print()
        except TypeError:
            print('przekazałeś niewłaściwą wartość')
    elif(str(display).lower() == 'no'):
        pass
    else:
        raise ValueError("display parametr should be 'yes' or 'no'")

    if(str(save).lower() == 'yes'):
        with open(fname, 'w') as f:
            for i in range(len(value)):
                f.write(str(value[i]) + ' ')

minval = int(input('Podaj minimalną wartość losowanej liczby: '))
maxval = int(input('Podaj maksymalną wartość losowanej liczby: '))
values = int(input('Podaj liczbe liczb w jednej próbie: '))
tries = int(input('Podaj liczbe prób: '))
display = input('Czy chcesz wyświetlić losowanie(yes/no): ')
save = input('Czy chcesz zapisać losowanie do pliku "los.txt": ')

generate(fminval = minval, fmaxval = maxval, fvalues = values, ftries = tries, fdisplay = display, fsave = save, fname = str(r'C:\Users\Nitro\Desktop\klasa2\lekcja5\los.txt'))

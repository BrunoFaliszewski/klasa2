i = 1
n = int(input('Jak długa ma być choinka?: '))
for x in range(n):
    for x in range(1,4):
        print('{:>5}'.format(i*'*' + (3 - x)*' '))
        i += 2
    i = 1
for x in range(3):
    print('{:>5}'.format('*' + 2 * ' '))
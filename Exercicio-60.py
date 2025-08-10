print('Vamos calcular o fatorial')
n = int(input('Digite o valor que deseja saber o fatorial: '))
f = n -1
ff = 1
print('{}'.format(n), end='')

while f > 0:
    print(' x {}'.format(f), end='')
    ff *= f
    f = f - 1
    
print('= {}'.format(ff))
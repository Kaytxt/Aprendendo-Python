print('Gerador de PA')
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
s = 8
print("{} -> ".format(n), end='')

while s >= 0:
    s = s - 1
    n += r
    print("{}  ->  ".format(n), end='')

if s <= 0:
    print('Fim')
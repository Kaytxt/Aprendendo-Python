print('Gerador de PA')
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
m = 10
s = n

while m != 0:
    for i in range(m):
        print(f'{s} -> ', end='')
        s += r
        c += 1
    print('Pausa')
    m = int(input('Quantos termos você quer mostrar mais? '))
print('PA finalizada com sucesso')


def contagem(a, b, c):
    if b == 0:
        b = 1
    if a < c:
        for a in range(a, c, b):
            print(f'{a} ', end='')
        print('')
    elif a > c:
        for a in range(a, c, b):
            print(f'{a} ', end='')
        

contagem(1, 1, 10)
contagem(10, -2, 0)

print('Agora é a sua vez de personalizar a contagem!')
inicio = (int(input('Inicio: ')))
passo = (int(input('Passo: ')))
fim = (int(input('Fim: ')))

contagem(inicio, passo, fim)
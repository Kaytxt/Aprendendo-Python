def tamanho(txt):
    qtd = len(txt)
    print(qtd)
    i = 0
    for i in range(qtd):
        print('-', end='')
    i = 0
    print('')
    print(txt)
    for i in range(qtd):
        print('-', end='')

frase = str(input('Digite uma frase ou palavra: '))
tamanho(frase)
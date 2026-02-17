import random 
numeros = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 , 10]

def sorteia(listaSorteio):
    print(f'Valores sorteados: {listaSorteio}')
    somaPar(listaSorteio)    


def somaPar(lista):
    somaPar = 0
    for c in lista:
        if c % 2 == 0:
            somaPar += c
    print(f'a soma dos valores pares é igual a {somaPar}')

sorteia(random.sample(numeros, k=7))


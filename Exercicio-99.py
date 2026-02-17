import random

def maior(* num):
    listaNumero = num
    maiorNumero = listaNumero[0]
    for c in listaNumero:
        if maiorNumero < c:
            maiorNumero = c
    print('Analisando Valores passados: ')
    print(f'O numero {maiorNumero} foi o maior numero informado. Lista {listaNumero}')
    print('-='*35)


maior(8, 9, 8, 5, 2)
maior(9, 10, 21, 30)
maior(2, 3, 4)
maior(7, 2)
maior(2)
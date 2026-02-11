import random

maiorValor = 0
menorValor = 11

lista = []

for c in range(5):
    numero = random.randint(1, 10)
    lista.append(numero)
    if maiorValor < numero:
        maiorValor = numero
    if menorValor > numero:
        menorValor = numero

print("Os valores sorteados foram: {}".format(lista))
print("O maior valor sorteado foi {}".format(maiorValor))
print("O menor valor sorteado foi {}".format(menorValor))

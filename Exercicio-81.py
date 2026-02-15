lista = []

while True:
    lista.append(int(input("Digite um numero ou 0 para encerrar:  ")))
    if 0 in lista:
        break

print(f'A lista tem {len(lista)} numeros')

print(sorted(lista, reverse=True))
if 5 in lista:
    print("O numero 5 esta na lista")
else:
    print("O numero 5 nao esta na lista")
    
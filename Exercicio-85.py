todosNumeros = list()
listaPar = list()
listaImpar = list()

for n in range(0, 7):
    numeros = int(input(f"Digite o {n} numero: "))

    if numeros % 2 == 0:
        listaPar.append(numeros)
    else:
        listaImpar.append(numeros)

listaImpar.sort()
listaPar.sort()

todosNumeros.append(listaImpar)
todosNumeros.append(listaPar)

print(f'Os numeros digitados foram {todosNumeros}')
print(f'Os numeros impares são {listaImpar}')
print(f'Os numeros pares são {listaPar}')


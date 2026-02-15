lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input("Digite um valor: ")))
    if 0 in lista:
        lista.pop()
        break
    
for c in lista:
    if c % 2 == 0:
        listaPar.append(c)
    else:
        listaImpar.append(c)

print(f'Essa foi a sua lista de numeros: {lista}')
print(f'Esses são os numeros pares da sua lista: {listaPar}')
print(f'Esses são os numeros impares da sua lista: {listaImpar}')
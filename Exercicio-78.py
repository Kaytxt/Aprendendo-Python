lista = []

for c in range(5):
    lista.append(int(input("Digite um numero: ")))

listaM = sorted(lista, reverse=True)

print(listaM)
print(f'O maior valor digitado foi {listaM[0]} e o menor valor digitado foi {listaM[4]}')
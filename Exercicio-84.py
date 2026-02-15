dados = list()
pessoas = list()
listaPesado = list()
listaLeves = list()
quantidadePessoas = 0


while True:
    dados.append(str(input("Digite o seu nome: ")))
    dados.append(float(input("Digite o seu peso: ")))
    pessoas.append(dados[:])

    quantidadePessoas += 1
    dados.clear()

    continuar = str(input("Quer adicionar mais? [s/n]")).lower()

    if continuar == "n":
        break

for p in pessoas:
            if p[1] >= 100:
                listaPesado.append(p[0])
            if p[1] <= 70:
                listaLeves.append(p[0])

print(pessoas)
print(listaLeves)
print(dados)
print(f'O total de pessoas registradas foram {quantidadePessoas}')
print(f'As pessoas com peso acima ou igual a 100 são {listaPesado}')
print(f'As pessoas com o peso menor ou igual a 70 são {listaLeves}')
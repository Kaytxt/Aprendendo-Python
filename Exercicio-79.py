lista = []

while True:
    n = (int(input("Digite um valor: ")))
    if n not in lista:
        lista.append(n)
        print("Numero adicionado com sucesso")

    else:
        print("Valor ja existe na lista") 
        
    c = (str(input("Quer continuar? [S/N]"))).lower()
    if c == "n":
        break

print(sorted(lista))
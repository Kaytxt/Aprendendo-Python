n1 = int(input("Digite o primeiro valor:  "))
n2 = int(input("Digite o segundo valor:  "))
op = 0
s = 0

while op != 5:

    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novo numero")
    print("[5] sair")
    op = int(input("Escolhar sua opção: "))


    if op == 1:
        s = n1 + n2
        print(s)

    if op == 2:
        s = n1 * n2
        print(s)

    if op == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else: 
            print("{} é maior que {}".format(n2, n1))

    if op == 4:
        n1 = int(input("Digite o primeiro valor:"))
        n2 = int(input("Digite o segundo valor"))

    if op > 5:
        print("Valor invalido tente novamente")
    
if op == 5:
    print("Saindo do programa")



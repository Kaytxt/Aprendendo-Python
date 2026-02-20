import fun

try:
    with open("Exercicio-115/arquivo.txt", "x", encoding="utf-8") as arquivo:
        print("Arquivo 'arquivo.txt' criado com sucesso.")

except FileExistsError:
    print('Arquivo.txt ja foi criado.')

fun.escolhas
print('-='*20)
n = fun.escolhas('Sua opção: ')
print('-='*20)
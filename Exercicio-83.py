parenteses = 0
divisao = []
funcao = str(input("Digite uma expressao: "))

for char in funcao:
    divisao.append(char)
    if '(' in char or ')' in char:  
        parenteses += 1

print(divisao)

if parenteses % 2 == 0:
    print("Sua expressão esta com os parenteses corretos")
else: 
    print("Sua expressão esta com os parenteses incorretos")
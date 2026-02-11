numeros = []
nove = 0
numerosPar = []
c = 0

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))
n4 = int(input("Digite o ultimo numero: "))

numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
numeros.append(n4)

if 9 in numeros:
    nove += 1 

if 3 in numeros:
    posicao = numeros.index(3) + 1
    numero3 = True
else:
    numero3 = False

for c in numeros:
    if c % 2 == 0:
        numerosPar.append(c)


print("Os valores digitados foram: ".format(numeros))
print("Encontramos o numero 9 {} vezes".format(nove))
print("Os numeros pares digitados foram {}".format(numerosPar))

if numero3 == True:
    print("O numero 3 esta na posição {}".format(posicao))
else:
    print("O numero 3 não foi digitado")
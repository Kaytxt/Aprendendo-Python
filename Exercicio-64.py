soma = 0
cont = 0

while True:
    n = int(input("Digite um numero (999 para parar): "))
    if n == 999:
        print('Você digitou {} numeros e a soma deles foi igual a {}'.format(cont, soma))
        break
    else:
        soma = soma + n
        cont += 1
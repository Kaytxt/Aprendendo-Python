contagem = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']

while True:
    n = int(input("Digite um valor entre 1 a 20: "))
    if n > 20 or n < 1:
        print("Esse valor não é aceito")
    else: 
        break

print('O valor que você digitou foi {}'.format(contagem[n-1]))
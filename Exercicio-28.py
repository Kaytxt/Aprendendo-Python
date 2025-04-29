import random

numero = [1, 2, 4, 5]
num = int(input('Digite um numero: '))

sorte = random.choice(numero)

if num == sorte:
    print('Parabens você acertou')
else:
    print('Você errou, o numero era {}'.format(sorte))
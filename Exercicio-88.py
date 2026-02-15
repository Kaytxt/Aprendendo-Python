import random

numeros = list()

for p in range(0, 60):
    numeros.append(p)

jogos = int(input('Quantos jogos você quer sortear: '))

for j in range(0, jogos):
    print(f'Jogo {j+1}: {random.sample(numeros, k=6)}')
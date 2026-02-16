import random 
from time import sleep 
from operator import itemgetter

ranking = []

jogo = {'jogador 1': random.randint(1, 6),
        'jogador 2': random.randint(1, 6),
        'jogador 3': random.randint(1, 6),
        'jogador 4': random.randint(1, 6)}
print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)

print('Ranking: ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {[v[1]]}')
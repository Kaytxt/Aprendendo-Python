golsFeitos = []
jogador = {}
totGols = 0
i = 0

jogador['nome'] = str(input("Digite o nome do jogador: "))
partidas = int(input("Digite quantas partidas ele jogou: "))

for k in range(0, partidas):
    gols = (int(input(f'Quantos gols ele fez na partida {k}: ')))
    totGols += gols
    golsFeitos.append(gols)

jogador['gols'] = golsFeitos
jogador['partidas'] = partidas

print(jogador)

print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')

for k in golsFeitos:
    print(f'Na partida {i+1} ele fez {k} gols')

print(f'O total de gols foi {totGols}')

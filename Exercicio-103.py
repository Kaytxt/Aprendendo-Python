def ficha(nome='', gols=0):
    c = gols
    if nome == '':
        print(f'O jogador <desconhecido> fez {c} gol(s) no campeonato.')
    else:    
        print(f'O jogador {nome} fez {c} gol(s) no campeonato.')



nome = str(input('Digite o nome do jogador: '))
gol = str(input('Digite quantos gols ele fez no campeonato: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

    
ficha(nome, gol)
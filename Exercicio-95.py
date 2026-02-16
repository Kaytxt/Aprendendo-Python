totalJogadores = []
jogador = {}
gols_temporarios = []

while True:
    jogador.clear()
    gols_temporarios.clear() 
    
    jogador['nome'] = str(input("Nome do Jogador: ")).strip()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for k in range(0, partidas):
        gols = int(input(f'  -> Quantos gols na partida {k+1}? '))
        gols_temporarios.append(gols)

    jogador['gols'] = gols_temporarios[:] 
    jogador['total'] = sum(gols_temporarios)
    totalJogadores.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 40)

for i, j in enumerate(totalJogadores):
    print(f'{i:<4} {j["nome"]:<15} {str(j["gols"]):<15} {j["total"]:<5}')
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(totalJogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {totalJogadores[busca]["nome"]}:')
        for i, g in enumerate(totalJogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)

print('<< VOLTE SEMPRE >>')
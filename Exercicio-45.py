from random import choice

lista = ["pedra", "papel", "tesoura"]

escolha = str(input('Você quer pedra papel ou tesoura: ')).upper()

maquina = choice(lista)

#pedra
if escolha == 'PEDRA' and maquina == 'papel':
    print('Maquina venceu ela escolheu papel')

elif escolha == 'PEDRA' and maquina == 'tesoura':
    print('Você venceu a maquiana escolheu tesoura')

elif escolha == 'PEDRA' and maquina == 'pedra':
    print('Empate')

#tesoura
if escolha == 'TESOURA' and maquina == 'pedra':
    print('Maquina venceu ela escolheu pedra')

elif escolha == 'TESOURA' and maquina == 'papel':
    print('Você venceu a maquiana escolheu papel')

elif escolha == 'TESOURA' and maquina == 'tesoura':
    print('Empate')

#papel
if escolha == 'PAPEL' and maquina == 'tesoura':
    print('Maquina venceu ela escolheu tesoura')

elif escolha == 'PAPEL' and maquina == 'pedra':
    print('Você venceu a maquiana escolheu pedra')

elif escolha == 'PAPEL' and maquina == 'papel':
    print('Empate')


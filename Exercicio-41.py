ano = int(input('Digite o ano de nascimento: '))

atual = 2025 - ano

if atual <= 9:
    print('Você é atleta mirim')
elif atual <= 14:
    print('Você é atleta junior')
elif atual <= 19:
    print('Você é atleta sernio')
else:
    print('Você é atleta master')
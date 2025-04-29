km = float(input('Digite quanto de velocidade o carro estava: '))

if km > 80:
    print('Você foi multado, a multa é de R${}'. format((km-80)*7))
else:
    print('Tudo certo, pode seguir o caminho')
valor = float(input('Digite o valor do produto: '))

print('Qual a forma de pagamento: ')
print('1 - A vista dinhero ou cheque')
print('2 - A vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')
con = int(input('Escolha uma opção: '))

if con == 1:
    preco = valor*0.1
    print('O produto recebeu 10% de desconto, ficou no valor de {}'.format(valor - preco))
elif con == 2:
    preco = valor*0.05
    print('O produto recebeu 5% de desconto, ficou no valor de {}'.format(valor - preco))
elif con == 3:
    preco = valor/2
    print('O produto ficou no valor de {} em duas parcelas'.format(preco))
else:
    preco = valor*0.2
    valor = valor + preco
    print('O produto ficou por 3 parcelas no valor de {}'.format(valor/3))


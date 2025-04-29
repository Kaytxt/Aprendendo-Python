ano = int(input('Em que ano estamos: '))

ano1 = ano % 4
ano2 = ano % 400

if ano1 == 0 & ano2 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
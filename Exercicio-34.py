sal = float(input('Digite o valor do seu salario: '))

if sal >= 1250.00:
    aumento = sal * 0.10
    aumento = sal + aumento
    print('Seu novo salario é {}'.format(aumento))
else:
    aumento = sal * 0.15
    aumento = sal + aumento

    print('Seu novo salario é {}'.format(aumento))
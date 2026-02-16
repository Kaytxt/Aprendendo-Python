carteira = {}

carteira['nome'] = (str(input('Digite o nome: ')))
carteira['ano'] = (str(input('Digite o ano de nascimento: ')))
carteira['numeroCarteira'] = (int(input('Digite o numero da carteira (0 se não tiver): ')))

if carteira['numeroCarteira'] != 0:
    carteira['anoContratação'] = (int(input('Digite o ano da contratação: ')))
    carteira['salario'] = (float(input('Digite o salario: ')))

    for k, v in carteira.items():
        print(f' - {k} tem valor {v}')

else:
    for k, v in carteira.items():
        print(f' - {k} tem valor {v}')
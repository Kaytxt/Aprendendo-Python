pessoas = {}
cadastro = []
cadastroF = []
totPessoas = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Digite o seu nome: '))
    pessoas['sexo'] = str(input('Digite o seu sexo [F/M]: ')).lower()


    if pessoas['sexo'] != "f" and pessoas['sexo'] != "m":
        while True:
            print('ERRO - Digite apenas M ou F')
            pessoas['sexo'] = str(input('Digite o seu sexo [F/M]: ')).lower()
            if pessoas['sexo'] == "f" or pessoas['sexo'] == "m":
                break
    pessoas['idade'] = int(input('Digite a sua idade: '))

    cadastro.append(pessoas.copy())
    cond = str(input('Quer continuar [s/n]: '))

    totPessoas += 1
    media += pessoas['idade']
    if pessoas['sexo'] == 'f':
        cadastroF.append(pessoas['nome'])

    if cond == 'n':
        media /= totPessoas
        break

print(f'A quantidade de pessoas cadastradas foi {totPessoas}')
print(f'A media da idade de todos cadastrados é igual a {media}')
print(f'As mulheres cadastradas são {cadastroF}')
print(f'As pessoas que estão com a idade acima da media são: ')

for p in cadastro:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};')
        print()
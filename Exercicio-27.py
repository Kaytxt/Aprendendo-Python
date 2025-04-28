nome = str(input('Digite seu nome: ')).strip()
nomee = nome.split()
print('Seu primeiro nome é: {}'.format(nomee[0]))
print('Seu ultimo nome é: {}'.format(nomee[len(nomee)-1]))
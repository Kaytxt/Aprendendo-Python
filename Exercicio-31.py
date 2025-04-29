km = int(input("Digite a quantidade de Km da viagem: "))

if km <= 200:
    km = km * 0.50
    print('O valor da passagem ficou R${}'.format(km))
else:
    km = km * 0.45
    print('O valor da passagem ficou R${}'.format(km))
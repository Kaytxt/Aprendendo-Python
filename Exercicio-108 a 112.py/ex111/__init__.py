import moeda108

def dobro(moeda, form):
    moeda *= 2
    if form == True:
        moeda = moeda108.moeda(moeda)
    return moeda

def metade(moeda, form):
    moeda /= 2
    if form == True:
        moeda = moeda108.moeda(moeda)
    return moeda

def aumentar(moeda, form):
    moedaPor = (moeda*10)/100
    moeda += moedaPor
    if form == True:
        moeda = moeda108.moeda(moeda)
    return moeda

def diminuir(moeda, form):
    moedaPor = (moeda*10)/100
    moeda -= moedaPor
    if form == True:
        moeda = moeda108.moeda(moeda)
    return moeda

def resumo(moeda=0, form=True):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda}')
    print(f'Dobro do preço: \t{dobro(moeda, True)}')
    print(f'Metade do preço: \t{metade(moeda, True)}')
    print(f'Aumento do preço: \t{aumentar(moeda, True)}')
    print(f'Diminuição do preço: \t{diminuir(moeda, True)}')
    print('-'*30)
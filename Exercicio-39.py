nas = int(input('Digite o ano que você nasceu: '))

ano = 2025
alis = ano - nas

if alis < 18:
    print('Você ainda não precisa se alistar, ainda falta {} anos'.format(18 - alis))
elif alis == 18:
    print('Você deve se alistar')
else:
    print('Ja passou seu prazo de alistamento, você deveria ter se alistado a {} anos atrás'.format(alis - 18))

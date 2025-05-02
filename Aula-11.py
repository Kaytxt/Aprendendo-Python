n1 = float(input('Digite a nota da np1: '))
n2 = float(input('Digite a nota da np2: '))
media = (n1 + n2)/2

if media >= 7:
    print('Sua media foi {}, \033[1;32mAprovado\033[m'.format(media))
else:
    print('Sua media foi {}, \033[1;31mReprovado\033[m'.format(media))
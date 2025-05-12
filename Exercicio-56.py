m = 0
s = 0
mh = 0 
hm = ''
tm2 = 0
for p in range(1, 5):
    print('----- Pessoa -----')
    nome = str(input('Digite seu nome:  ')).strip()
    idade = int(input('Digite sua idade:  '))
    sexo = str(input('Digite seu sexo F ou M:  ')).strip()
    s += idade
    if p == 1 and sexo in 'Mm':
        mh = idade
        hm = nome
    if sexo in 'Mm' and idade > mh:
        mh = idade
        hm = nome
    if sexo in 'Ff' and idade <= 20:
        tm2 = tm2 + 1
m = s/4
print('A media da idade do grupo é {}'.format(m))
print('O homem de maior idade tem {} anos e se chama{}'.format(mh, hm))
print('A quantidade de mulheres com 20 anos ou menos é de {}'.format(tm2))
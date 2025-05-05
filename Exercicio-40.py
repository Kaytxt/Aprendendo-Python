p1 = float(input('Digite a nota da sua primeira prova: '))
p2 = float(input('Digite a nota da sua segunda prova: '))

media = (p1+p2)/2

if media >= 7:
    print('Aprovado')
elif 5.0 <= media <= 6.9:
    print('Recuperação')
else:
    print('Reprovado')
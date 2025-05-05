r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As 3 retas formam um triangulo')
    
    if r1 == r2 and r2 == r3 and r3 == r1:
        print('Esse triangulo é Equilatero')

    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esse triangulo é Isosceles')

    else:
        print('Esse triangulo é Escaleno')

else:
    print('Não é um triangulo')




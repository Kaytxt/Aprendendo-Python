num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

numm = num1
nume = num1

if nume > num2:
    nume = num2
if nume > num3:
    nume = num3

print('O numero menor é {}'.format(nume))

if numm < num2:
    numm = num2
if numm < num3:
    numm = num3

print('O numero maior é {}'.format(numm))
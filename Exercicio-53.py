p = str(input('Digite uma palavra: ')).strip().lower()

for v in reversed(p):
    print(v, end='')

if p == p[::-1]:
    print(' É um palíndromo!')
else:
    print(' Não é um palíndromo.')
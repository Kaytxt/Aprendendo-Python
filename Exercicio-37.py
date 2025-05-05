num = int(input('Digite um numero: '))

print('Você quer converter esse numero para:')
print('1 - Binario')
print('2 - Octal')
print('3 - Hexadecimal')
escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))

elif escolha == 2:
    print('{} convertido para ocatal é igual a {}'.format(num, oct(num)[2:]))

else:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))



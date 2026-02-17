def leiaint(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um numero inteiro valido')
        if ok:
            break
    return valor
    


numero = leiaint('Digite um numero: ')
print(f'Você digitou o numero {numero}')
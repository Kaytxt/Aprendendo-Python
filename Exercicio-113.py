def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
             print('ERRO: VALOR INTEIRO DIGITADO INVALIDO')
             continue
        except KeyboardInterrupt:
            print('Usuario preferiu nao informar esse numero')
            return 0
        else:
             return n


def leiafloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('ERRO: VALOR DECIMAL DIGITADO É INVALIDO TENTE NOVAMENTE')
            continue
        except KeyboardInterrupt:
            print('Usuario preferiu nao informar esse numero')
            return 0
        else:
            return n


n = leiaint('Digite um valor inteiro: ')
nf = leiafloat('Digite um valor decimal: ')

print(f'Os valores digitados foram {n} e {nf}')


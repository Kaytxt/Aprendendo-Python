def fatorial(num, show=False):  
    '''
    Calcula o fatorial de um numero
    
    :param num: O numero a ser calculado
    :param show: se for True ele mostra a resolução do calculo 
    ''' 
    f = 1
    if show==True:
        for num in range(num, 0, -1):
            f *= num
            print(f'{num} ', end='')
        return (f)
    else:
        for num in range(num, 0, -1):
            f *= num
        return (f)


print(f'{fatorial(5, show=True)}')

def votar(ano):
    if ano >= 18 and ano < 65:
        resultado = 'Voto obrigatorio'
        return resultado
    elif ano >= 65:
        resultado = 'Voto opcional'
        return resultado
    else:
        resultado = 'Você não pode votar'
        return resultado

ano = int(input('Em que ano você nasceu: '))
anoAtual = 2026
idade = anoAtual - ano

print(f'Você tem {idade} de idade: {votar(idade)}')
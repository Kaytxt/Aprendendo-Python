def notas(*num, sit=False):
    total = media = 0
    situaçãoSala = {}
    menorNota = 20
    maiorNota = 0
    for c in num:
        total += 1
        media += c
        if maiorNota <= c:
            maiorNota = c
        if menorNota >= c:
            menorNota = c
    media = media/total

    situaçãoSala['total'] = total
    situaçãoSala['maior nota'] = maiorNota
    situaçãoSala['menor nota'] = menorNota
    situaçãoSala['media'] = media

    if sit:
        if media > 7:
            situaçãoSala['situação'] = 'BOA'
        else:
            situaçãoSala['situação'] = 'Ruim'

    return situaçãoSala

print(notas(3.5, 10, 6.6, sit=False))
tabela = ['Bragantino', 'Palmeiras', 'Chapecoense', 'Mirassol', 'Fluminense', 'Bahia', 'Sao Paulo', 'Flamengo', 'Botafogo', 'Gremio', 'Athletico', 'Coritiba', 'Vitoria', 'Vasco', 'AtleticoMG', 'Internacional', 'Santos', 'Remo', 'Corinthians', 'Cruzeiro']
lugar = 1


print("Os 5 primeiros times da tabela:")
for primeiros in range(5):
    print("{}° - {}" .format(primeiros + 1, tabela[primeiros]))


print("Os 4 ultimos colocados da tabela:")
for ultimos in range(-1, -5, -1):
    print("{}° - {}".format(lugar, tabela[ultimos]))
    lugar += 1

print("Os times em ordem alfabetica:")
tabela_ordenada = sorted(tabela)
print(tabela_ordenada)

posicao = tabela.index("Chapecoense")
print('Chapecoense esta na posição {} da tabela'.format(posicao + 1))
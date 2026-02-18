import ex111

p = float(input("Digite o preço: R$"))
print(f'A metade de {ex111.moeda(p)} é igual a {ex111.metade(p, True)}')
print(f'O dobro de {ex111.moeda(p)} é igual a {ex111.dobro(p, True)}')
print(f'Aumentando 10% de {ex111.moeda(p)} temos {ex111.aumentar(p, True)}')
print(f'Diminuindo 15% de {ex111.moeda(p)} temos {ex111.diminuir(p, True)}')


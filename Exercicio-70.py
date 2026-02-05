precoBarato = 100000000000000000000000000000000000000000000000000000000000000000
totalCompra = 0 
nomeBarato = ''
produtoCaro = 0
escolha = 's'

print("--------------------------------")
print("     LOJA DO SUPER BARATÃO      ")
print("--------------------------------")

while escolha == "s":
    nomeProduto = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    
    totalCompra += preco
    
    if preco > 1000:
        produtoCaro += 1 
    
    if precoBarato > preco:
        precoBarato = preco
        nomeBarato = nomeProduto

    escolha = str(input("Quer continuar? [S/N] ")).lower()
    

print('O total da compra foi R${}'.format(totalCompra))
print('Temos {} produtos custando mais de R$1000'.format(produtoCaro))
print('O produto mais barato foi {} que custa R${}'.format(nomeBarato, precoBarato))
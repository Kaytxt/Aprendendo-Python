d = int(input('Digite a quantidade de dias que você utilizou o carro: '))
km = float(input('Digite a quantidade de km que foi rodada no carro: '))
tot = d*60 + km*0.15
print('O valor que você tera que pagar é de R${} pelos dias usados, R${} pelos kms rodados, o valor total é de R${}'.format(d*60, km*0.15, tot))
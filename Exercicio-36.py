vlcasa = float(input("Qual é o valor da casa: "))
ano = int(input("Em quantos anos você pretende pagar "))
salario = float(input("Quanto você recebe de salario: "))

parcela = ano * 12
vlparcela = vlcasa/parcela 

if vlparcela > salario*0.3:
    print("Seu emprestimo foi negado")
else:
    print("Seu emprestimo foi aceito, as parcelas ficaram no valor de {} por mês".format(vlparcela))
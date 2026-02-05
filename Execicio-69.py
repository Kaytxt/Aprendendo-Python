escolha = ''
idadeSuperior = 0
homensCadastrados = 0
mulherJovem = 0

while True:
    print("------------------------")
    print("  CADASTRE UMA PESSOA   ")
    print("------------------------")
    
    print("------------------------")
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).lower()
    print("------------------------")
    
    escolha = str(input("Quer continuar? [S/N] ")).lower()
    
    if idade >= 18:
        idadeSuperior += 1
    if sexo == "m":
        homensCadastrados += 1
    if sexo == "f" and idade < 20:
        mulherJovem += 1
    
    if escolha == "n":
        print('Total de pessoas com mais de 18 anos: {}'.format(idadeSuperior))
        print('Ao todo temos {} homens cadastrados'.format(homensCadastrados))
        print('E temos {} mulheres com menos de 20 anos'.format(mulherJovem))
        break
         
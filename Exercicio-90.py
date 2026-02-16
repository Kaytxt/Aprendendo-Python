aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input("Digite a media do aluno: "))

if aluno['media'] < 7.0:
    print(f'Aluno: {aluno["nome"] }')
    print(f'Media: {aluno["media"] }')
    print(f'Situação: Reprovado')

else:
    print(f'Aluno: {aluno["nome"] }')
    print(f'Media: {aluno["media"] }')
    print(f'Situação: Aprovado')
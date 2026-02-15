aluno = list()
Alunos = list()
f = 1
while True:

    aluno.append(f)
    aluno.append(str(input("Digite o nome do Aluno: ")))
    aluno.append(float(input("Digite a primeira nota: ")))
    aluno.append(float(input("Digite a segunda nota: ")))

    
    Alunos.append(aluno[:])
    aluno.clear()

    c = str(input('Quer continuar? s/n')).lower()

    if c == 'n':
        break
    else:
        f += 1

for p in Alunos:
    print(f'{p[0]} - {p[1]} - {(p[2]+p[3])/2}')

while True:
    busca = int(input("Deseja mostrar a nota de qual aluno? (999 para encerrar): "))
    
    if busca == 999:
        break
    
    for p in Alunos:
        if p[0] == busca:
            print(f'Notas de {p[1]} são {p[2]} e {p[3]}')
            achou = True
            break 
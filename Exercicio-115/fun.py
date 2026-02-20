def escolhas(op):
    while True:
            print('-='*20)
            print(f'{"MENU PRINCIPAL":^40}')
            print('-='*20)
            print('1 - Ver pessoas cadastradas\n' \
                '2 - Cadastrar novas pessoas\n' \
                '3 - Sair do sistema')
            try:
                escolha = int(input(op))
                if(escolha == 1):
                    verPessoas()
                elif(escolha == 2):
                    cadastrar()
                elif(escolha == 3):
                     print('Saindo do sistema. Obrigado!')
                     break
                elif(escolha > 3):
                     print('ERRO: Esse numero não é uma opção')
            except(ValueError, TypeError):
                print('ERRO: Por favor digite um valor valido!')
                continue
        
        



def verPessoas():
    print('-' * 40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-' * 40)
    try:
        with open("Exercicio-115/arquivo.txt", "r", encoding="utf-8") as f:
            for linha in f:
                print(linha.replace('\n', ''))
    except FileNotFoundError:
        print('Arquivo não encontrado ou vazio.')
    print('-' * 40)


def cadastrar():
    print('-' * 40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-' * 40)
    nome = str(input('Digite o nome que quer cadastrar: '))
    idade = int(input("Digite a idade: "))
    with open("Exercicio-115/arquivo.txt", "a", encoding="utf-8") as f:
         f.write(f'{nome:<30}{idade:>3} anos\n')
         print(f'{nome} foi registrado com sucesso!')



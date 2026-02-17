def ajuda(var):
    print(help(var))
    

while True:
    res = str(input('Digite o que você precisa de ajuda (fim para encerrar): ')).lower()
    if res == 'fim':
        break

    ajuda(res)

    

while True:
    num = int(input("Qual numero você quer ver a tabuada: "))
    if num < 0:
        print("Programa encerrado")
        break
    for tab in range(1, 11):
        print('{} x {} = {}'.format(num, tab, (num*tab)))
        tab += 1

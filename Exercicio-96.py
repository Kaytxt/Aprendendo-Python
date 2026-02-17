def areaTerreno(a, b):
    area = a * b
    print(f'A area de um terreno {a}x{b} é de {area}m²')

print('Controle de terreno')
print('-='*30)
l = float(input('Qual a largura do seu terreno? '))
c = float(input('Qual o comprimento do seu terreno? '))
areaTerreno(l, c)
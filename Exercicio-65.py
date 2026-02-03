totNum = 0
mv = 0
res = "s"
s = 0

while True:
    n = int(input("Digite um numero: "))
    
    s += n

    totNum += 1

    if mv <= n:
        mv = n

    res = str(input("Quer continuar? S ou N: ")).lower()
    if res == "n":
        break
    
media = s/totNum

print('O maior valor digitado foi {} e a media dos numeros é igual a {}'.format(mv, media))
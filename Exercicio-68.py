import random
escolhaPc = ''
c = 1
venceu = 0

print("=========================")
print("VAMOS JOGAR PAR OU IMPAR")
print("=========================")


while True:
    numeroPlayer = int(input("Digite um valor: "))
    escolhaPlayer = str(input("Par ou Impar [P/I]: ")).lower()
    pcNumero = random.randint(1, 10)
    
    if escolhaPlayer == "p":
        escolhaPc = "i"
    else:
        escolhaPc = "p"
    
    soma = pcNumero + numeroPlayer
    
    if soma % 2 == 0:
        print('Você jogou {} e o computador jogou {}. Total {}, deu PAR!'.format(numeroPlayer, pcNumero, soma))
    else:
        print('Você jogou {} e o computador jogou {}. Total {}, deu IMPAR!'.format(numeroPlayer, pcNumero, soma))
    
    if escolhaPlayer == "p" and soma % 2 == 0:
        print("Você VENCEU")
        venceu += 1
    elif escolhaPlayer == "i" and soma % 2 != 0:
        print("Você VENCEU")
        venceu += 1
    else:
        print("Você PERDEU")
    
    if c == 3:
        print('GAME OVER! Você venceu {} vezes'.format(venceu))
        break
    c += 1
    
    
    
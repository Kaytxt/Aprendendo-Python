c = 0
import random
vitoria = 0

while c < 5:
    humanoNumero = int(input("Digite um valor: "))
    humanoEscolha = str(input("Você quer par ou impar [I ou P]: ")).lower()
    maquinaNumero = random.randint(1, 10)
    if humanoEscolha == "i":
        maquinaEscolha = "p"
    else:
        maquinaEscolha = "i"

    res = humanoNumero + maquinaNumero

    if res % 2 == 0 and humanoEscolha == "p":
        print("Você jogou {} e a maquina {}. Total de {} deu PAR!" \
        " VOCÊ VENCEU".format(humanoNumero, maquinaNumero, res))
        vitoria += 1
    elif res % 2 != 0 and humanoEscolha == "i":
        print("Você jogou {} e a maquina {}. Total de {} deu IMPAR!" \
        " VOCÊ VENCEU".format(humanoNumero, maquinaNumero, res))
        vitoria += 1
    elif res % 2 == 0 and maquinaEscolha == "p":
        print("Você jogou {} e a maquina {}. Total de {} deu PAR!" \
        " MAQUINA VENCEU".format(humanoNumero, maquinaNumero, res))
    else: 
        print("Você jogou {} e a maquina {}. Total de {} deu IMPAR!" \
        " MAQUINA VENCEU".format(humanoNumero, maquinaNumero, res))
    
    c += 1

print("Você venceu {} de 5 partidas, parabens!".format(vitoria))

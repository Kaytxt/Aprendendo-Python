import random

s = 1
nm = random.randint(1, 10)

nr = int(input('Adivinhe qual numero eu pensei:'))
acertou = False

while not acertou:
    if(nr < nm):
        nr = int(input('Mais... tente mais uma vez:'))
    if(nr > nm):
        nr = int(input('Menos... tente mais uma vez:'))
    s += 1
    if nm == nr:
        acertou = True

print('Parabens você acertou!!!')
print('Teve um total de {} tentativas'.format(s))
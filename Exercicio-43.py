peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura*altura)

print(f'Seu imc é: {imc: .2f}')

if imc < 18.5:
    print('Você esta abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Você esta no peso ideal')
elif 25 <= imc <= 30:
    print('Você esta no sobrepeso')
elif 30 <= imc <= 40:
    print('Você esta com obesidade')
else:
    print('Obesidade mórbida')


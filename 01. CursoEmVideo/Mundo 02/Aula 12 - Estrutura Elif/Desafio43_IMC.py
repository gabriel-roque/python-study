"""
Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seun IMC e mostre seu status, de acordo com a tabela:
► Abaixo de 18.5: ABAIXO DO PESO
► Entre 18.5 e 25: PESO IDEAL
► 25 ate 30: SOBREPESO
► 30 ate 40: OBESIDADE
► Acima de 40: OBESIDADE MORBIDA
"""

print('{:^20}'.format('== IMC =='))
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura*2)

if imc <= 18.5: #ABAIXO DO PESO
    print('Status de IMC: {:.2f}'.format(imc))
    print('>> abaixo do peso'.upper())
elif imc >= 18.5 and imc <= 25: #PESO IDEAL
    print('Status de IMC: {:.2f}'.format(imc))
    print('>> peso ideal'.upper())
elif imc >= 25 and imc <= 30: #SOBREPESO
    print('Status de IMC: {:.2f}'.format(imc))
    print('sobrepeso'.upper())
elif imc >= 30 and imc <= 40: #OBESIDADE
    print('Status de IMC: {:.2f}'.format(imc))
    print('>> obesidade'.upper())
elif imc >= 40: #OBESIDADE MORBIDA
    print('Status de IMC: {:.2f}'.format(imc))
    print('>> obesidade morbida'.upper())
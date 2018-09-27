"""
DESAFIO 55

Faca um programa que leia um peso de 5 pessoas. No final mostra qual foi o maior e o menor
"""
maiorPeso = 0
menorPeso = 999
posicaoMaior = 0
posicaoMenor = 0

for c in range(1,6):
    peso = float(input('Insira o peso da {}° pessoa: '.format(c)))

    if peso >= maiorPeso:
        maiorPeso = peso
        posicaoMaior = c
    elif peso < menorPeso:
        menorPeso = peso
        posicaoMenor = c

print('O MAIOR peso foi da {}° pessoa com {}'.format(posicaoMaior, maiorPeso))
print('O MENOR peso foi da {}° pessoa com {}'.format(posicaoMenor, menorPeso))
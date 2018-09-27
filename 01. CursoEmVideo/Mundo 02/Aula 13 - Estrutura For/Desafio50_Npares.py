"""
DESADIO 50

Desenvolva um programa que leia seis numeros inteiros e  mostre a soma apenas
daqueles que forem pares. Se o valor digitado for impar, desconsidere-o
"""
somaP = 0
for c in range (1,7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if (n%2) == 0:
        somaP += n
print('A soma dos PARES: {}'.format(somaP))
"""
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
• O 1° valor e maior
• O 2° valor e maior
• Nao existe valor maior, os dois sao iguais
"""

n1 = int(input('Insira o 1° valor: '))
n2 = int(input('Insira o 2° valor: '))

if n1 > n2:
    print('O 1° valor e maior'.upper())
elif n2 > n1:
    print('O 2° valor e maior'.upper())
else:
    print('Nao existe valor maior, os dois sao iguais')
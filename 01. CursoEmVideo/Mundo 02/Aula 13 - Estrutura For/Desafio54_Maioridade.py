"""
DESAFIO 54

Crie um programa que leia o ano de nascimento de 7 pesssoas. No final, mostre quantas pessoas ainda
nao atingiram a maioriadade e quantas ja sao maiores
"""

idadePessoa = 0
totMaior = 0
totMenor = 0

for c in range(1,8):
    idadePessoa = int(input('Insira a idade da {}° pessoa: '.format(c)))
    if idadePessoa >= 21:
        totMaior += 1
    elif idadePessoa < 21:
        totMenor += 1

print('{} pessoas ainda NAO atigiram a maioridade.'.format(totMenor))
print('{} pessoas JA atingiram a maioridade.'.format(totMaior))
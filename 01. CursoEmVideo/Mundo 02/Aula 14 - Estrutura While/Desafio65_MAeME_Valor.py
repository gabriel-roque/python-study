'''
Desafio 65

Crie um programa que leia varios numeros inteiros. No final da execucao, mostre a media entre todos
os valores e qual foi o Maior e Menor valores lidos. O programa deve perguntar
ao usuario se ele quer ou nao continuar a digitaar.
'''

resposta = ''
media = soma = maior = 0
menor = 0
totalValores = 0

while resposta != 'N':
    valor = int(input('Insira o valor: '))
    soma = soma + valor #a soma de todos oa valores digitados
    totalValores += 1 #total de valores digitados

    if valor > maior: #maior valor
        maior = valor
    elif valor < menor: #menor valor
        menor = valor


    resposta = str(input('Quer continuar? [S/N]: ')).upper()

media = soma/totalValores #calcula media

print('Media: {:.2f}'.format(media))
print('Maior Valor: {}'.format(maior))
print('Menor Valor: {}'.format(menor))
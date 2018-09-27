"""
DESAFIO 56

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
► A media de idade do grupo
► Qual e o nome do homem mais velho
► Quantas mulheres tem menos de 20 anos
"""

somaIdade = 0
maiorIdade = 0
homemMaisVelho = str
mediaIdade = 0
mulheres20 = 0

for c in range(1,5):
    print('=== {}° PESSOA ==='.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()

    somaIdade = (somaIdade + idade) #soma total da idade do grupo
    mediaIdade =  somaIdade/4 # calculo da media

    if sexo == 'M' and idade > maiorIdade: #vereficacao do home mais velho
        homemMaisVelho = nome

    if sexo == 'F' and idade <= 20: # verificacao da mulher com menos de 20 anos
        mulheres20 = mulheres20 + 1

print('A media do grupo: {}'.format(mediaIdade))
print('O homem mais velho: {}'.format(homemMaisVelho))
print('Mulheres com menos de 20 anos {}'.format(mulheres20))
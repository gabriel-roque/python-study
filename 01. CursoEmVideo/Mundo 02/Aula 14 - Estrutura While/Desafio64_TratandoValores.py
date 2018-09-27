'''
Desafio 64

Crie um programa que leia varios numeros inteiros. O programa so vai parar quando o usuario digitar o valor 999.
Que e a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.
'''

valor = total = soma = cont = 0 # atribui o mesmo valor para todas as variaveis

while cont != 999: #enquanto for difrente de 999 o procedimento e executado
    valor = int(input('Informe o valor [999 - STOP]: '))
    soma = soma + valor
    total = total + 1

    if valor == 999: #se o valor for igual a 999 ele ira tirar o FLAG da soma e do total de valores digitados
        soma = soma - 999
        total = total -1
        cont = 999


print('O total de valores digitados {}'.format(total))
print('A soma de todos os {} digitados: {}'.format(total, soma))
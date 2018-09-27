"""
Desafio 66

Crie um programa que leia varios numeros inteiros. O programa so vai parar quando o usuario digitar o valor 999.
Que e a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.
"""

valor = soma = total = 0
cont = 1

while True:
    valor = int(input(f'Insira {cont}° o valor: '))

    if valor == 999: #ira verificar 1 se a parada e ativada
        break

    total += 1
    soma += valor
    cont += 1

print(f'A soma dos {total} valores: {soma}.')
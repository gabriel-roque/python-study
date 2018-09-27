"""
Desafio 70

Crie um programa que leia o nome e o preco de varios produtos. O programa devera
perguntar se o user vai continuar. No final, mostre:

A) Qual e o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000
C) Qual e o nome do produto mais barato.

"""

nome = op = ProdutoBarato = ''
preco = Mepreco = Mapreco = total = mais1k = 0


while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Valor do produto: '))
    total += preco
    print('='*20)


    if preco > Mapreco:
        Mapreco = preco
        Mepreco = Mapreco
    if preco < Mepreco:
        Mepreco = preco
        ProdutoBarato = nome
    if preco > 1000:
        mais1k += 1

    op = str(input('Quer continuar? [S/N]: ')).upper()
    print('=' * 20)

    if op == 'N':
        break

print('-' * 40)
print(f'Total: R$ {total}')
print(f'{mais1k} produtos custam mais que R$ 1.000,00')
print(f'Produto mais barato e {ProdutoBarato} com o preco de: R$ {Mepreco}')
print('-' * 40)
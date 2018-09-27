# Escreva um programa para aprovar o emprestimo bancario para compra de uma casa.
# O programa vai  perguntar o valor da casa. O salario do comprador e quantos anos ira durar para pagar.

# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

import emoji

#print(emoji.emojize('Python is :thumbsup:', use_aliases=True))

print('-='*10)
print('{:>14} {:<5}'.format('Bank LINUX', emoji.emojize(':bank:', use_aliases=True)))
print('-='*10)

valor = float(input('Qual o valor casa? '))
salario = float(input('Qual seu salario? '))
periodo = int(input('Anos de financiamento: '))


prestM = (valor / (periodo * 12))
Psalario = (salario - (30/100 * salario))

if prestM >= Psalario:
    print('EMPRESTIMO NEGADO')
else:
    print('EMPRESTIMO APROVADO')
    print('Prestacao Mensal: R$ {:.2f}'.format(prestM))
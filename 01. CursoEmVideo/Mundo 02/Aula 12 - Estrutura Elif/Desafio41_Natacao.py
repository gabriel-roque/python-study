"""
A confederacao Nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostra sua categoria,
de acordo com a idade:
• Ate 9 anos: Mirim
• Ate 14 anos: Infantil
• Ate 19 anos: Junior
• Ate 20 anos: Senior
• Acima: Master
"""
from datetime import date
print('confederacao Nacional de natacao'.upper())

ano = int(input('Informe seu ano de nascimento: '))
anoAtual = date.today().year
idade = (anoAtual - ano)

if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <=19:
    print('CATEGORIA JUNIOR')
elif idade <= 20:
    print('CATEGORIA SENIOR')
elif idade > 20:
    print('CATEGORIA MASTER')
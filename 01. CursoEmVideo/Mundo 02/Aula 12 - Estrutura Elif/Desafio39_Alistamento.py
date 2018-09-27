'''
Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
• Se ele ainda vai se alistar
• se e a hora de se alistar
• se ja passou do tempo do alistamento

► o programa devera mostrar o tempo que falta ou que passou do prazo
'''
from emoji import emojize #biblioteca de emoiji
from datetime import date #bibliotece de datas

print('-='*20)
print('{:>28} {:<20}'.format('| alistamento militar', emojize(':beginner: |',use_aliases=True) ).upper())
print('-='*20)

ano = date.today().year #funcao que obtem o ano atual do computador [date.today().year]
print('Ano atual: {}\n'.format(ano))
anoN = int(input('Informe seu ano de nascimento: '))
idade = (ano - anoN) #idade necesaria

if idade == 18:
    print('Realizar Alistamento no ano Decorrente {}'.upper().format(ano))
elif idade < 18:
    print('Relizar alistamento somente no ano de {}'.format(18 - idade + ano))
    print('Falta(m) {} ano(os) para o alistamento'.format(18 - idade))
elif idade > 18:
    print('esta fora do prazo de alistamento, favor se apresentar em um junta militar'.upper())
    print('Ano(s) ultrapasado(os): {}'.format(ano - (anoN + 18)))
    print('Ano de alistamento {} '.upper().format(anoN + 18))
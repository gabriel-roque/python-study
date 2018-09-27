from datetime import date
ano = int(input('0 para analisar o ano ATUAL - Qual o ano: '))

# a biblioteca date, como sa se diz trabalha com data
# se o user digitar zero o python ira pegar o ano da maquina e colocar na condicao
if ano == 0:
    ano == date.today().year
    print('Ano Atual: {}'.format(date.today().year))


#Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando ele com 366 dias, um dia
#a mais do que os anos normais de 365 dias,
#ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).

if (ano % 400 == 0 and 100 != 0 or ano % 400 == 0):
    print('Ano Bissexto'.upper())
else:
    print('Nao é ano bissexto'.upper())
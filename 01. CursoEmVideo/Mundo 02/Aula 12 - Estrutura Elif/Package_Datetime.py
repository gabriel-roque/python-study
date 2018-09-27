from datetime import date
ano = int(input('0 para analisar o ano ATUAL - Qual o ano: '))

# a biblioteca date, como sa se diz trabalha com data
# se o user digitar zero o python ira pegar o ano da maquina e colocar na condicao
if ano == 0:
    ano == date.today().year
    print('Ano Atual: {}'.format(date.today().year))
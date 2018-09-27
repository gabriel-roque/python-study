print('JADILSON`s MARKET')
print('')
produto = float(input('Qual o valor do produto: R$ '))

desconto = ((5/100)*produto)

nvalor = (produto-desconto)

print('Com 5% de desconto: R$ {:.2f} '.format(nvalor))
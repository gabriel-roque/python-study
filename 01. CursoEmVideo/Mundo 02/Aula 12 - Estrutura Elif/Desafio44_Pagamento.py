"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
• À vista dinheiro / cheque: 10% de desconto
• À vista no cartão: 5% de desconto
• Em até 2x no cartão: preço normal
• 3x ou mais no cartão: 20% de juros
"""

print('{:=^40}'.format(' central de compras '.upper()))
valor = float(input('Insira o valor da compra: '))

print('Selecione sua forma de pagamento.\n\n'
      '[1] ► À vista Dinheiro / Cheque: 10% de desconto\n'
      '[2] ► À vista Cartão: 5% de desconto\n'
      '[3] ► Em até 2x no cartão: preço normal\n'
      '[4] ► 3x ou mais no cartão: 20% de juros')
OP = int(input('OP: ')) #escolha do usuário

if OP == 1:
    Nvalor = (valor - (10 / 100 * valor))
    print('Total: R$ {:.2f}'.format(Nvalor))
elif OP == 2:
    Nvalor = (valor - (5 / 100 * valor))
    print('Total: R$ {:.2f}'.format(Nvalor))
elif OP == 3:
    Nvalor = (valor / 2)
    print('Total: R$ {:.2f} em 2x no cartão'.format(Nvalor))
elif OP == 4:
    vezes = int(input('Quantidade de vezes (3x min.): '))
    Nvalor = ((valor + (20 / 100 * valor)) / vezes)
    print('Total: R$ {:.2f} em {}x no cartão'.format(Nvalor, vezes ))
else:
    print('Opcao invalida, tente novamente'.upper())

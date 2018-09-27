#Ordem de precendência
#1 - ( ) Parênteses
#2 - ** Potência
#3 - *, /, //, %
#4 - +, -
#Ordem de precendência

print ('|||| OPERADORES ARITIMÉTICOS ||||')
print('')
#ADIÇÃO
print('=== ADICÃO ===')
n1 = float(input('Informe o 1º Valor: '))
n2 = float(input('Informe o 2º Valor: '))

#ADIÇÃO
resul = (n1 + n2)
print('{} + {} = {}'.format(n1, n2, resul))

#SUBTRAÇÃO
print('=== SUBTRAÇÃO ===')
n1 = float(input('Informe o 1º Valor: '))
n2 = float(input('Informe o 2º Valor: '))

#SUBTRAÇÃO
resul = (n1 - n2)
print('{} - {} = {}'.format(n1, n2, resul))

#MULTIPLICAÇÃO
print('=== MULTIPLICAÇÃO ===')
n1 = float(input('Informe o 1º Valor: '))
n2 = float(input('Informe o 2º Valor: '))

#MULTIPLICAÇÃO
resul = (n1 * n2)
print('{} X {} = {}'.format(n1, n2, resul))

#DIVISÃO
print('=== DIVISÃO ===')
n1 = float(input('Informe o 1º Valor: '))
n2 = float(input('Informe o 2º Valor: '))

#DIVISÃO
resul = (n1 / n2)
print('{} / {} = {}'.format(n1, n2, resul))

#POTENCIAÇÃO
print('=== POTENCIAÇÃO ===')
n1 = float(input('Informe o Base: '))
n2 = float(input('Informe a potência: '))

#POTENCIAÇÃO
resul = (n1 ** n2)
print('{} potência de {} = {}'.format(n1, n2, resul))

#DISISÃO INTEIRA
print('=== DISISÃO INTEIRA ===')
n1 = float(input('Informe o 1º Valor: '))
n2 = float(input('Informe o 2º Valor: '))

#DISISÃO INTEIRA
resul = (n1 // n2)
print('A divisão INTEIRA entre {} e {} = {}'.format(n1, n2, resul))

#RESTO DA DIVISÃO
print('=== RESTO DA DIVISÃO ===')
n1 = float(input('Informe o 1º Valor: '))
n2 = float(input('Informe o 2º Valor: '))

#RESTO DA DIVISÃO
resul = (n1 % n2)
print('O RESTO da divisão entre {} e {} = {}'.format(n1, n2, resul))

#RAIZ QUADRADA
print('=== RAIZ QUADRADA ===')
n = int(input('Informe o valor: '))

#RAIZ QUADRADA
print('A raiz quadrada de {} é {:.2f}'.format(n,n**(1/2)))
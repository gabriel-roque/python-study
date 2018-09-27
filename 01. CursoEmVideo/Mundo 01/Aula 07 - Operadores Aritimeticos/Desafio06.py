n = int(input('Informe um valor: '))

print(' Seu dobro: {} \n Seu tripo: {} \n Sua raiz quadrada: {:.2f} \n'.format(n*2, n*3, n**(1/2)))
#usando funcao ~pow~ para raiz quadrada
print(' Seu dobro: {} \n Seu tripo: {} \n Sua raiz quadrada: {:.2f} '.format(n*2, n*3, pow(n,(1/2))))
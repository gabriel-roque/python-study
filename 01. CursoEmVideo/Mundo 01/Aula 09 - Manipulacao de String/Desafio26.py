frase = str(input('Insira uma frase: '))
print('A letra `a` aparece {} vezes'.format(frase.count('a')))
print('A primeira vez que `a` e exibi na posicao {}'.format(frase.find('a')))
print('A ultima vez que `a` e exibida na posicao {}'.format(frase.rfind('a')))
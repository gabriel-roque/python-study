'''
DESAFIO 53

Verificar se um nome e um palindrome. OSB: Ignore os espacos

ex: apos a sopa
    a sacada da casa
    a torre da derrota
'''

palavra = str(input('Insira o texto: ').upper())
palavra = palavra.split() #quebra em lista
palavra = (''.join(palavra)) #tira os espacos

print('Palavra original: {}'.format(palavra))

palavraInvertida = (palavra[::-1]) #inverte a palavra
print('Palavra invertida: {}'.format(palavraInvertida))

if palavra == palavraInvertida:
    print('► E uma PALINDROME')
else:
    print('► NAO e um PALINDROME')
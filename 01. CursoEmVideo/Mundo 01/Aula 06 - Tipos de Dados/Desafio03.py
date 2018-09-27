print ('===== DESAFIO 03 =====')

n1 = int(input('1º Valor: '))
n2 = int(input('2º Valor: '))

soma = n1 + n2

#ANULAÇÃO DO CÓDIGO

#print ('A soma dos valores ', n1, '+', n2, '=', soma)
#print ('O tipo de classe:',(type(n1)))

#Mais fácil a utuilização do .format

print ('A soma entre {} e {} vale {}'.format(n1, n2, soma))
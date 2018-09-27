import math
num = int(input('Insira um nº: '))
#sempre que for necessario utilizar a função
raiz = math.sqrt(num)
#função CEIL = arredonda pra cima
print('A raiz quadrada de {} equivale a {}'.format(num, math.ceil(raiz), raiz))
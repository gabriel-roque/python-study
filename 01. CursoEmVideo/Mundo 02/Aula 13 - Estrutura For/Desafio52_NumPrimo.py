"""
DESAFIO 52

Verificar se um numero e primo
"""
tot = 0

num = int(input('Insira um valor: '))
for c in range(1, num + 1):
    if num%c == 0:
        tot += 1
print('O numero {} foi divisivel {} vezes'.format(num, tot))

if tot <= 2:
    print('O numero {} e PRIMO'.format(num))
else:
    print('O numero {} NAO E PRIMO'.format(num))
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i-1, f + 1, p):
        print(c, end=' ')

print('\n')

for c in range(i-1, f + 1):
        print(c, end=' ')
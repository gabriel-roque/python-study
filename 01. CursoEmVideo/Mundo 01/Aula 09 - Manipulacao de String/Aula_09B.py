'''
frase = '   Curso em Video Python    '
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.find('Curso'))

print(frase.replace('Python', 'Android'))
print(frase)
frase = (frase.replace('Python', 'Android'))
print(frase)
'''

frase = ('Curso em Video Python')
print(frase.split())
print(' '.join(frase))
dividido = frase.split()
print(dividido[2][3])
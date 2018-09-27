print('==== DESAFIO 04 ====')

print('')
#ESPAÇO
n = input('Digite algo: ')

print('Tipo da classe:', type(n))
print('')
#ESPAÇO

print('Só tem espaços?', n.isspace())
print('É numérico?', n.isnumeric())
print('É alfabetico?', n.isalpha())
print('É alfa numérico?', n.isalnum())
print('Esta em Maiúsculas?', n.isupper())
print('Esta em Minusculas?', n.islower())
#vale lembrar que capitalizada se diz quando possue letras Maiuscula e Minusculas
print('Esta capitalizada?', n.istitle())
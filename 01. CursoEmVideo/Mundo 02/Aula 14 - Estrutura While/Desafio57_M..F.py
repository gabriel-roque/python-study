"""
Desafio 57

Faca um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F.
Caso esteja errado, peca para a digitacao novamente ate ter um valor correto
"""
sexo = ''
while sexo != 'STOP':
    sexo = str(input('[M/F]: ')).upper().strip()[0]

    if sexo == 'M':
        print('Sexo Masculino')
        sexo = 'STOP'
    elif sexo == 'F':
        print('Sexo Feminino')
        sexo = 'STOP'
    else:
        print('Informe um respota valida.')
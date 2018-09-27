print('JEQUITI CONSULTORIA')
print('====================')
nome = str(input('Qual o nome do fucionario: '))

salario = float(input('Informe o salario: R$ '))
print('O AUMENTO SERA DE 15% \n')

aumento = ((15/100)*salario)
Nsalario = (salario+aumento)

print('O funcionario {} tera o seu reajuste salarial para: R$ {:.2f}'.format(nome, Nsalario))
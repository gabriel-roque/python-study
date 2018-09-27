nome = str(input('Informe o nome do aluno: '))
nota1 = float(input('Informe a 1 nota: '))
nota2 = float(input('Informe a 2 nota: '))

print('A media do aluno {} e {:.1f}'.format(nome,(nota1+nota2)/2))
cidade = str(input('Informe o nome da cidade: '))
dividido = cidade.split()
print(('Pousse SANTOS no inico do nome? {}').format('Santos' in dividido[0]))
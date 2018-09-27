salario = float(input('Informe o valor do salário: '))

if (salario > 1250.00):
    aumento = ((10 / 100) * salario)
    Nsalario = (salario + aumento)
    print('O aumento sera de 10% >> R$ {} \n >> Reajuste Salarial: R$ {:.2f}'.format(aumento, Nsalario))
else:
    aumento = ((15 / 100) * salario)
    Nsalario = (salario + aumento)
    print('O aumento sera de 15% >> R$ {} \n >> Reajuste Salarial: R$ {:.2f}'.format(aumento, Nsalario ))
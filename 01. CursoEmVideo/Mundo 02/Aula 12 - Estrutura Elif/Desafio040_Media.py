"""
Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com media atingida:
• Media abaixo de 5.0 (REPROVADO)
• Media entre 5.0 e 6.9 (RECUPERACAO)
• Media 7.0 ou superior (APROVADO)
"""

n1 = float(input('Insira 1° nota: '))
n2 = float(input('Insira 2° nota: '))
media = (n1+n2)/2

print('Media do aluno: {}'.format(media))

if media < 5.0:
    print('REPROVADO')
elif media >= 5.1 and media <= 6.9:
    print('RECUPERACAO')
elif media >= 7.0:
    print('APROVADO')
'''
Desafio 69

Crie um programa que leia idade e o sexo de varias pessoas. A cada pessoa cadastrada
o programa devera perguntar se o usuario quer o nao continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''

idade = total18 = totalM = m20 =0
sexo = op = ''


while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    print('='*30)

    if idade > 18:
        total18 += 1
    if sexo == 'M':
        totalM += 1
    if sexo == 'F' and idade > 20:
        m20 += 1


    op = str(input('Quer continuar? [S/N]: ')).upper() #operacao que o user escolhe
    print('-'*30)

    if op == 'N': #quebra da repeticao
        break

print('/'*50)
print(f'{total18} pesso(as) com + de 18 anos.')
print(f'Foram cadastrados {totalM} homens.')
print(f'Apenas {m20} mulher(es) com + de 20 anos.')
print('/'*50)
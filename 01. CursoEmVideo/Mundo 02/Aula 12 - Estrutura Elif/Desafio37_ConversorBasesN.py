'''
Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a bese de conversao:
1- para binario
2- octal
3- hexadecimal
'''

numero =  int(input('Insira o valor que deseja: ')) #valor a ser convertido

print('Escolha qual operacao deseja realizar')
print('='*15)
print('1- Binario \n2- Octal \n3- Hexadecimal'.upper())
print('='*15)

escolha = int(input('operação ► '.capitalize())) #escolha do usuario

if escolha == 1:
    #binario
    print(bin(numero)[2:]) # [2:] come a exibir a partir da 2 casa, sendo que a contagem é 0, 1, 2......
elif escolha == 2:
    #octal
    print (oct(numero)[2:])
elif escolha == 3:
    #hexadecinal
    print (hex(numero)[2:])
else:
    print('Opção inválida')

cores = {'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}


text = 'Hello Wolrd!'
print('......{} \033[31m'.format(text, cores['verde'], text))
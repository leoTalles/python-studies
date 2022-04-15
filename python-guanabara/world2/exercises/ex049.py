# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for

print('-=' * 16)
print('VAMOS APRENDER TABUADA DISGRAÇA')
print('-=' * 16)
num = int(input('Digite um número para saber sua tabuada: '))

print('-=' * 10)
for tab in range(1, 11):
    print('\033[1;32m{} x {} é igual a: {}\033[m'.format(num, tab, num * tab))
print('-=' * 10)

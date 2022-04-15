# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR

num = int(input('Insira um número: '))
r = (num % 2)
if r == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))
    


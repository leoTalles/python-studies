# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep

v1 = int(input('Insira um valor: '))
v2 = int(input('Insira outro valor: '))

menu = 0
while menu != 5:
    sleep(2)
    menu = int(input('''
-=-=-=-=-=-=-=-=-=-=-=-= 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa  
-=-=-=-=-=-=-=-=-=-=-=-=             
             '''))
    if menu == 1:
        print('-='*5)
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
        print('-='*5)
    elif menu == 2:
        print('-='*5)
        print('{} * {} = {}'.format(v1, v2, v1 * v2))
        print('-='*5)
    elif menu == 3:
        if v1 > v2:
            print('-='*5)
            print('O número {} é maior'.format(v1))
            print('-='*5)
        if v2 > v1:
            print('-='*5)
            print('O número {} é maior'.format(v2))
            print('-='*5)
    if menu == 4:
        v1 = int(input('Insira um valor: '))
        v2 = int(input('Insira outro valor: '))
        print('-='*5)
print('Fim?')
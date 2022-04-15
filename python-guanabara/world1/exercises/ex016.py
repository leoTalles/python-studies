# DESAFIO 016
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# EX: Digite um número: 6.127 -> O número 6.127 tem a parte inteira 6

import math
num = float(input('Insira um número real para saber sua porção inteira: '))
print('A porção inteira de {:.2f} é igual a {}'.format(num, math.trunc(num)))

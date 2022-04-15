# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num1 = int(input('\033[1;38mDigite um numero: '))
num2 = int(input('Digite outro: '))

if num1 > num2:
    print('\033[1;34mO primeiro valor {} é maior '.format(num1))
elif num1 == num2:
    print('\033[1;32mNão existe valor maior, os dois são iguais: {} e {}'.format(num1, num2))
elif num1 < num2: 
    print('\033[1;33mO segundo valor {} é maior '.format(num2))
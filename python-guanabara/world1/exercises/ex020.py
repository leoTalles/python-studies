# DESAFIO 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos, Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

n1 = input('Joga 1 nome no peito do teu pai: ')
n2 = input('Mais um: ')
n3 = input('Outro: ')
n4 = input('Cade mais? ')

sort = [n1, n2, n3, n4]
random.shuffle(sort)


print('A ordem dos grupos será')
print(sort)


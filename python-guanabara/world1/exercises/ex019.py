# DESAFIO 019
# Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.
import random

n1 = str(input('Qual nome? '))
n2 = str(input('Qual nome? '))
n3 = str(input('Qual nome? '))
n4 = str(input('Qual nome? '))

sort = random.choice([n1, n2, n3, n4])

print('Parabens, o escolhido pra apagar o quadro é vc {}'.format(sort))

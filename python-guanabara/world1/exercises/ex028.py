# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE O E 5 E PEÇA 
# PRO USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCER OU PERDEU

from random import randint
from time import sleep

cpunum = randint(0, 5)
print('Processando...')
sleep(3)
usernum = int(input(('Pensei em um número de 0 a 5... tente adivinhar: ')))

if cpunum == usernum:
    print('Ah filho da puta parabens acertou')
    print('Eu tinha pensado no {}'.format(cpunum))
else:
    print('Tu se fudeu pq eu ganhei babaca kkkkkkk')    
    print('Eu tinha pensado no {}'.format(cpunum))
    

    

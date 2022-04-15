# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer

from random import randint
from time import sleep

cpunum = randint(1, 11)
print('Silencio estou pensando...')
sleep(1.5)
usernum = int(input('Pensei em um número de 1 a 10... \nTente adivinhar: '))
p = 1

while usernum != cpunum:
    usernum = int(input('Tente novamente kk: '))
    count = +1
    p += count
print(' ------ ATÉ Q ENFIM PORRA CARALHO ------ ')
print('Eu pensei no número', cpunum)
sleep(2)
print('Vc tentou {} vezes, caralho menor'.format(p))
print(' --------------------------------------- ')
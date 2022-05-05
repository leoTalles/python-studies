# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from ast import IsNot
import random
from timeit import repeat
count = 0
while True:
    print('-=' * 19)
    escolha = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    user = int(input('Diga um número: '))
    cpu = random.randint(1, 10)
    count += 1
    resultado = cpu + user 

    if escolha == 'P' and (resultado % 2) == 0:
        print('-=' * 19)
        print('Ganhador, vitorioso!')
        print('Deu par caralho')
        print(f'O computador jogou {cpu} e você jogou {user}')
        continue
    elif escolha == 'I' and (resultado % 2) != 0:
        print('-=' * 19)
        print('Ganhou')
        print('Deu ímpar carai')
        print(f'O computador jogou {cpu} e você jogou {user}')
    else:
        print('-=' * 19)
        print('Perdeu')
        print(f'O computador jogou {cpu} e você jogou {user}')
        count -= 1
        break
print('==' * 19)
print(f'VOCÊ TEVE UM WINSTREAK DE {count} PARTIDAS')
print('==' * 19)

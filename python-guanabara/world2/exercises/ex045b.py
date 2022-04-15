from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA  
[ 1 ] PAPEL
[ 2 ] TESOURA
      ''')
user = int(input('Fala tua play pro pai: '))

if cpu == 0:
    if user == 0:
        print('Empatou cria')
    elif user == 1:
        print('Ganhou cria')
    elif user == 2:
        print('Perdeu lixoso')
    
elif cpu == 1:
    if user == 0:
        print('Perdeu lixoso')
    elif user == 1:
        print('Empatou criacionista')
    elif user == 2:
        print('Ganhou pprt')
    
elif cpu == 2:
    if user == 0:
        print('Ganhou trem')
    elif user == 1:
        print('Perdeu mt fracassado')
    elif user == 2:
        print('Empatou meno')


print('CPU JOGOU {}'.format(itens[cpu]))
print('TU JOGOU {}'.format(itens[user]))
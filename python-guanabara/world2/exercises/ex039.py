# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

ano = int(input('Qual seu ano de nascimento: '))
idade = 2022 - ano
atraso = idade - 18
restam = 17 - idade 

if idade == 17:
    print('\033[1;34mALISTE-SE JÁ SOLDADO PORRA\033[m')
elif idade == 18:
    print('\033[1;32mALISTE-SE JÁ SOLDADO PORRA TA RASPANDO\033[m')
elif idade < 17:
    print('\033[1;33mSUA HORA TA CHEGANDO, FALTAM APENAS {} ANOS\033[m'.format(restam))
elif idade >= 19:
    print('\033[1;31mVOCE ESTÁ {} ANOS ATRASADO SOLDADO\033[m'.format(atraso))
    
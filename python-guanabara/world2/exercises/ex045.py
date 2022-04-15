# Crie um programa que faça o computador jogar Jokenpô com você
import random
from time import sleep

print('VAMOS JOGAR JOKENPO NESSA PORRA CARALHO')

user = str(input('Escolha entre PEDRA, PAPEL ou TESOURA: ').upper())
cpu = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if cpu == 'PEDRA' and user == 'PEDRA':
    print('\033[1;33mEMPATE: CHOQUE DE PEDRAS PPRT KK')
elif cpu == 'PEDRA' and user == 'PAPEL':
    print('\033[1;32mVITORIA: AMASSOU A PEDRINHA DELE BOA KK\033[m')
elif cpu == 'PEDRA' and user == 'TESOURA':
    print('\033[1;31mDERROTA: O CPU AMASSOU TUA TESOURINHA KKKK\033[m')
    
    
elif cpu == 'PAPEL' and user == 'PEDRA':
    print('\033[1;31mDERROTA: FOI AMASSADIN FOI? KKKKKK\033[m')
elif cpu == 'PAPEL' and user == 'PAPEL':
    print('\033[1;33mEMPATE: TAPORRA MENO EMPATOU\033[m')
elif cpu == 'PAPEL' and user == 'TESOURA':
    print('\033[1;32mVITORIA: RASGOU O MALANDRO NO MEI KKKKKK\033[m')

    
elif cpu == 'TESOURA' and user == 'PEDRA':
    print('\033[1;32mVITORIA: AMASSA A TESOURA DELE MRM MENO\033[m')
elif cpu == 'TESOURA' and user == 'PAPEL':
    print('\033[1;31mDERROTA: CPU TE RASGOU KKKKKKK\033[m')
elif cpu == 'TESOURA' and user == 'TESOURA':
    print('\033[1;33mEMPATE: ULTIMO CHOQUE DE TESOURA ASSIM SÓ VI NO KKKKK\033[m')
else: 
    print('\033[1;35mTÁ DE MAROLA? ESCREVE CERTO PORRA\033[m')
    
sleep(1)
print('cpu jogou:', cpu)
print('voce jogou', user)
# Crie um programa que contenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

alfabeto = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número dentro de 0 até 20: '))
   
    while num < 0 or num > 20:
        num = int(input('Tente novamente, DIGITE UM NÚMERO DE 0 ATÉ 20: '))
    print(f'Você digitou o número {alfabeto[num]}.')

    resposta = str(input('Desejas continuar? [S/N] '))
    if resposta in 'Ss':
        continue
    else:
        break
print('ai calica')
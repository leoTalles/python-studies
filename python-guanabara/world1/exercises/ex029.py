# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H, MOSTRE
# UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE

speed = float(input('Digite a velocidade do carro em Km: '))

if speed > 80:
    valor = (speed-80) * 7
    print('\033[1;31m Você foi multado e o valor da multa é de R${:.2f}'.format(valor))
else:
    print('\033[1;32m Boa 06, ta andando na linha')
    
    
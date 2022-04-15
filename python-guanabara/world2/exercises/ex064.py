# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (Desconsiderando o flag(999))
n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Insira números caralho (FLAG: 999): '))
    c += 1
    soma += n
print('Você digitou {} números'.format(c - 1))
print('A soma entre os números digitados foi {}'.format(soma - 999))

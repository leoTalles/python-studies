# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere
from xmlrpc.client import ServerProxy

count = 0
s = 0
for x in range(1, 7):
    n = int(input('digite o {}º numero: '.format(x)))
    if n % 2 == 0:
        s += n  
        count += 1
print('Voce informou {} PARES e a SOMA é igual a {}'.format(count, s))
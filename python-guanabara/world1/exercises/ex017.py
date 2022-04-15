# DESAFIO 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa
import math

opos = float(input('Digite o comprimento do cateto oposto: '))
adja = float(input('Agora o cateto adjacente: '))
hipo = math.hypot(opos, adja)

print('O cateto oposto vale {}, o cateto adjacente {} e a hipotenusa {:.2f}'.format(opos, adja, hipo))



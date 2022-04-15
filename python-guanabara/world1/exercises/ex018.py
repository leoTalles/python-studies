# DESAFIO 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

ang = float(input('Digite um ângulo para saber seu seno, cosseno e tangente: '))

sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O ângulo é {}. O seno equivale a {:.2f}, cosseno equivale a {:.2f} e tangente equivale a {:.2f}'
      .format(ang, sin, cos, tan))

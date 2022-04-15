# Crie um programa que leia o ano de nascimento de 7 pessoas. 
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas
# já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for c in range(1, 8):
    nasc = int(input('{}ª pessoa, digite o seu ano de nascimento: '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else: 
        totmenor += 1

print('Existem {} pessoas maiores de idade'.format(totmaior))
print('Existem {} pessoas menores de idade'.format(totmenor))
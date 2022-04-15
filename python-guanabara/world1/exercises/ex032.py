# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

from datetime import date

'''
from calendar import isleap #USANDO MODULOS

ano = int(input('Digite um ano para saber se é bissexto: '))

if isleap(ano):
    print('Ih, é bissexto mané')
else:
    print('Não deu, não é bissexto')    

'''

ano = int(input('Fale um ano ai: Coloque 0 para analisar o ano atual ')) # FORMULA VANILLA (SEM MÓDULOS)

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é show bissexto'.format(ano))
else:
    print('o ano {} nnao é bissextoo'.format(ano))
    


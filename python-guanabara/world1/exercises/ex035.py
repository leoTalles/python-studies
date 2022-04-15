# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E DIGA AO USUÁRIO
# SE ELAS PODEM OU NAO FORMAR UM TRIANGULO

print('-=-' * 11)
print('\033[0;33m ANALISADOR DE TRIANGULOS CARALHO')
print('-=-' * 11)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32m Podem formar triangulo\033[m')
else:
    print('\033[1;31m nao pode caralho porra')



    
# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while

n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
termos = n1 + (10 - 1)* r
count = n1

while count <= termos:
    print(count,'-', end=' ')
    count += r
print('\nFIM CARALHO')


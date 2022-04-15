# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# EQUILÁTERO:   todos os lados iguais 
# ISÓSCELES:    dois lados iguais
# ESCALENO:     todos os lados diferentes

print('-=-' * 11)
print('\033[0;33m ANALISADOR DE TRIANGULOS CARALHO')
print('-=-' * 11 +'\033[m' )

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;32mPodem formar um triangulo:\033[m', end=' ')
    if r1 == r2 == r3:
        print('\033[1;32mEquilátero\033[m')       
    elif r1 != r2 != r3 != r1:
        print('\033[1;32mEscaleno\033[m')    
    else:
        print('\033[1;32mIsósceles\033[m')  
else:
    print('\033[1;31m nao pode caralho porra')


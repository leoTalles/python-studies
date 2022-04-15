# Faça um programa que leia um número qualquer e mostre seu fatorial
# EX: 5! = 5x4x3x2x1 = 120
num = int(input('digite um numero: '))
fatorial = 1
count = 1

while count <= num:
    fatorial = fatorial * count
    count += 1
print('O fatorial de {} é {}'.format(num, fatorial))
print('fim')

# Resolução do guanabara
'''
n = int(input('digite um numero'))
c = n 
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f)
'''

# Resolução com módulos
'''
from math import factorial
n = int(input('digite um numero'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
'''

# RESOLUÇÃO USANDO FOR
''' 
usernum = int(input('Digite um número: '))
fac = 1
for usernum in range(usernum, 0, -1):
    fac *= usernum
print(fac)
'''
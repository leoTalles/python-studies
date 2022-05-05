# LOOPS WHILE PARA CONSULTA
cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

n = cont = 0
while cont < 3:
    n = int(input('Digite um número'))
    cont += 1
print('Fim')

# GAMBIARRA SEM VERGONHA
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))
print('Fim')

# SEM GAMBIARRA, BONITO
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

# USANDO FSTRINGS

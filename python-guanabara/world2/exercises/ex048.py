# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
# de 3 e que se encontram no intervalo de 1 até 500
s = 0
count = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        count += 1
        s = s + x
print('A soma dos {} elementos é igual a {}'.format(count, s))

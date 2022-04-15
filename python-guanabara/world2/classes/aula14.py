'''for c in range(1, 11):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')
    
n = 1 
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

n1 = 1 
par = ímpar = 0
while n1 != 0:
    n1 = int(input('Digite um valor: ')) 
    if n1 % 2 == 0:
        par += 1
    else:
        ímpar += 1    
print('Voce digitou {} números pares e {} números ímpares'.format(par, ímpar))

# Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o {} peso: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))



#p1 = float(input('digite o peso carai: '))
#p2 = float(input('digite o peso carai: '))
#p3 = float(input('digite o peso carai: '))
#p4 = float(input('digite o peso carai: '))
#p5 = float(input('digite o peso carai: '))
#print('O maior peso é:', max(p1, p2, p3, p4, p5))
#print('O menor peso é:', min(p1, p2, p3, p4, p5))   



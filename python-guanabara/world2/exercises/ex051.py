# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10
# primeiros termos dessa progressão

n1 = int(input("Primeiro elemento: ") )
r = int(input("Razao: ") )
termos = n1 + (10 - 1)* r


for c in range(n1, termos+r, r):
    print(c)
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando a flag).
count = soma = 0
print('-=' * 10)
while True:
    num = int(input('Digite um número: [999 para parar]'))
    if num == 999:
        break
    soma += num
    count += 1
print('-=' * 26)
print(f'Foram digitados {count} números (Desconsiderando a flag)')
print(f'A soma é igual a {soma}')
print('-=' * 26)

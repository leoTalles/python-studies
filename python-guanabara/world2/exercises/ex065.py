# Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não 
# continuar a digitar valores
#TODO VOLTAR AQUI DEPOIS DA AULA 15

num = 0
resp = 'S' 
soma = media = count = maior = menor = 0

while resp in 'Ss':
    num = int(input('Insira um número: '))
    soma += num
    count += 1
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if num == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num    
        if num < menor:
            menor = num
media = soma / count
print('Você digitou {} números e a soma é igual a {}'.format(count, soma))
print('O resultado da média é igual a ', media)
print('O menor numero é ', menor)
print('O maior numero é ', maior)
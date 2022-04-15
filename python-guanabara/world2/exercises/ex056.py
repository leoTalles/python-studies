# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#   A média de idade do grupo
#   Qual é o nome do homem mais velho
#   Quantas mulheres tem menos de 20 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
nomenova = ''
mulhernova = 0

for p in range(1, 5):
    print('<---- {}ª PESSOA ---->'.format(p))
    nome = str(input('Qual seu nome? ')).strip()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Sexo? (M/F): ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        nome = nomenova
        mulhernova += 1
        
mediaidade = somaidade / 4  
print('a média de idade do grupo é {} anos'.format(mediaidade)) 
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho.title(), maioridadehomem))
print('Existem {} mulheres menores que 20 anos'.format(mulhernova)) 


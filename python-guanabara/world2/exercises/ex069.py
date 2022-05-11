# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
#TODO: Assistir resolução do ex, para aperfeiçoar o código.
idade = sexo = maioridade = homenscount = mulheresmenos20 = 0
while True:
    sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()
    idade = int(input('Quantos anos? '))
    if sexo == 'M':
        homenscount += 1
    elif sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    if idade > 18:
        maioridade += 1
    print('-=-' * 10)
    verif = str(input('Deseja continuar? [S/N] ')).upper()
    if verif == 'N':
        break
print('-=-' * 12)
print(f'Existem {maioridade} pessoas com mais de 18 anos!')
print(f'Foram cadastrados {homenscount} homens!')
print(f'Foram cadastradas {mulheresmenos20} mulheres com menos de 20 anos!')
print('-=-' * 12)
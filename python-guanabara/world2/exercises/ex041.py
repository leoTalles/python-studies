# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos:   MIRIM
# até 14 anos:  INFANTIL
# até 19 anos:  JUNIOR
# até 20 anos:  SENIOR
# acima:        MASTER

ano = int(input('Diga sua data de nascimento, para saber sua categoria: '))
idade = 2022 - ano

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14 : #14             
    print('Categoria: INFANTIL')    
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade == 20:
    print('Categoria: SENIOR')
elif idade > 20:
    print('Categoria MASTER')
    
print('Você tem {} anos de idade.'.format(idade))

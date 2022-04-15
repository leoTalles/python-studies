#   CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#   O NOME COM TODAS AS LETRAS MAIÚSCULAS; O NOME COM TODAS MINÚSCULAS; QUANTAS LETRAS AO
#   TO/DO (SEM CONSIDERAR ESPAÇOS); QUANTAS LETRAS TEM O PRIMEIRO NOME;

fullname = str(input('Digite seu nome completo: ')).strip()

print('SEU NOME EM MAIÚSCULAS É: ', fullname.upper())
print('seu nome em minúsculas é: ', fullname.lower())
print('Seu nome ao todo possui {} letras '.format(len(fullname) - fullname.count(' ')))

separa = fullname.split()

print('Seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))



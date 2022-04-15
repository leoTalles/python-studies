#   FAÇA UM PROGRAMA QUE LEIA UM NOME COMPLETO DE UMA PESSOA E MOSTRE EM SEGUIDA O PRIMEIRO E O
#   ULTIMO NOME SEPARADAMENTE 
#   EX: ANA MARIA DE SOUZA
#       PRIMEIRO: ANA
#       ULTIMO= SOUZA

n = str(input('Qual seu nome completo? ')).strip().title()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

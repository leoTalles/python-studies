#   CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

nome = str(input('Qual seu nome? ')).strip()

print('Seu nome tem Silva? {}'.format(' SILVA ' in nome.upper()))





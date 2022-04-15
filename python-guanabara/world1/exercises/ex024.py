#   CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO"

city = str(input('Qual cidade que tu nasceu? ')).strip()
print(city[:5].upper() == 'SANTO')


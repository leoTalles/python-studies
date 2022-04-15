#   FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#   QUANTAS VEZES APARECE A LETRA "A" ; EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ;
#   EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

frase = str(input('Insira uma frase aqui: ')).strip()
contador = frase.count('a') + frase.count('A')
# Resolução 2
# frase = str(input('Insira uma frase: ').upper())
# print('Esta frase possui {} letras A'.format(frase.count('A')))

print('Esta frase possui {} letras A'.format(contador))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))




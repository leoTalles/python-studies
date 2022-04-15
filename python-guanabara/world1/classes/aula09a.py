#   MANIPULANDO TEXTOS (STRINGS)
#   Fatiamento 

frase = input('sexo? ')

print(frase[:13])
print(frase.count('0'))
print(frase.upper().count('0'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.split())
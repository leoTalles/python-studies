# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo.
# desconsiderando os espaços
# Ex: APOS A SOPA

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temo um palindromo')
else:
    print('n é palindromo')
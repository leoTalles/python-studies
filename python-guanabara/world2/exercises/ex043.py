# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
# status, de acordo com a tabela abaixo:
# ABAIXO DE 18.5:   Abaixo do peso
# ENTRE 18.5 E 25:  Peso ideal 
# 25 ATÉ 30:        Sobrepeso
# 30 ATÉ 40:        Obesidade
# ACIMA DE 40:      Obesidade mórbida

print('-=-' * 5)
print('SAIBA SEU IMC')
print('-=-' * 5)
altura = float(input('Qual sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('magrin mane kkkk')
elif imc <= 24.9:
    print('ta fitness hein kkkk')
elif imc <= 29.9:
    print('sobrepeso padrao ne pai kkkk')
elif imc <= 34.9:
    print('ta obesin')
elif imc <= 39.9:
    print('obesidade bolada mano')
elif imc > 40.0:
    print('obesidade mórbida paizao')
    
print('Seu IMC É {:.1f}'.format(imc))

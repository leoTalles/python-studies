"""
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, \n o produto é {} \n e a divisão é {}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e potência {}'.format(di, e) )
"""

# DESAFIO 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

ni = int(input('Digite um número: '))
# Posso usar mais ou menos variáveis
print('Analisando o valor {}, seu sucessor é {} e seu antecessor é {}'.format(ni, (ni+1), (ni-1)))

# DESAFIO 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada

n = int(input('Digite alguma porra: '))
dob = n * 2
triple = n * 3
raiz = n ** (1/2)

print('O dobro de {} é {}, O triplo é {} \ne a raiz quadrada é {:.2f}'.format(n, dob, triple, raiz))

# DESAFIO 007
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input('Digite sua nota aqui: '))
nota2 = float(input('Digite sua outra nota aqui: '))

media = (nota1 + nota2) / 2

print('A média do aluno é ', media)

# DESAFIO 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite uma altura sla: '))

cm = metros * 100
mm = metros * 1000

print('{} metros possui {}cm e {}mm '.format(metros, cm, mm))

# DESAFIO 009
# Faça um programa que leia um número inteiro qualquer e mostra na tela a sua tabuada

num = int(input('Digite um número para saber sua tabuada hehe: '))

print('-' * 12)
print('{} x {:2} é igual a {}'.format(num, 1, num*1))
print('{} x {:2} é igual a {}'.format(num, 2, num*2))
print('{} x {:2} é igual a {}'.format(num, 3, num*3))
print('{} x {:2} é igual a {}'.format(num, 4, num*4))
print('{} x {:2} é igual a {}'.format(num, 5, num*5))
print('{} x {:2} é igual a {}'.format(num, 6, num*6))
print('{} x {:2} é igual a {}'.format(num, 7, num*7))
print('{} x {:2} é igual a {}'.format(num, 8, num*8))
print('{} x {:2} é igual a {}'.format(num, 9, num*9))
print('{} x {:2} é igual a {}'.format(num, 10, num*10))
print('-' * 12)

# DESAFIO 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

money = float(input('Qual seu saldo atualmente? R$ '))

dol = money / 5.16
eur = money / 5.66

print('Você têm {:.2f} R$ e pode comprar US$ {:.2f} \n e EUR$ {:.2f}'.format(money, dol, eur))

# DESAFIO 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

alt = float(input('Digite a altura em metros: '))
lar = float(input('Digite a largura em metros: '))
area = alt * lar
tinta = area / 2

print('É necessário {:.2f}L de tinta para pintar a área de {:.2f}m'.format(tinta, area))

# DESAFIO 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

price = float(input('Qual o preço do produto? '))
off = (price / 100) * 5
newprice = price - off

print('Com o desconto de 5% você paga somente R${:.2f}! APROVEITE!'.format(newprice))

# DESAFIO 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

payment = float(input('Insira o salário: '))
inc = (payment / 100) * 15
newpayment = payment + inc

print('Com acréscimo de 15%, você passará a receber {:.2f} R$'.format(newpayment))

# DESAFIO 014
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

celsius = float(input('Informe a temperatura em °C: '))
fahr = celsius * 1.8 + 32

print('A temperatura {}°C equivale a {:.1f}°F'.format(celsius, fahr))

# DESAFIO 015
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input('Quantos km percorridos? '))
days = int(input('Quantos dias foi alugado? '))

kmprice = km * 0.15
daysprice = days * 60
lendtotal = kmprice + daysprice

print('O carro alugado por {} dias e com {}km percorridos lhe custará {:.2f}R$'.format(days, km, lendtotal)) 
 

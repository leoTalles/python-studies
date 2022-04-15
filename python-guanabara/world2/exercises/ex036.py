# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado

from time import sleep

print('\033[;36m-=-' * 12)
print('TROPA DOS EMPRÉSTIMOS')
print('-=-' * 12)

sleep(1)

valor_casa = float(input('Qual o valor da casa? '))
salario    = float(input('Qual seu salário? '))
prazo      = int(input('Em quantos anos será feito o pagamento: '))


quant_prest = prazo * 12
prest       = valor_casa / quant_prest

sleep(1)

if prest > (salario / 100) * 30:
    print('\033[0;31m Emprestimo negado vacilão')
else:
    print('\033[0;32m Empréstimo aprovado')
    print('\033[0;32m Serão aplicadas {} parcelas de R${} durante {} anos'.format(quant_prest, prest, prazo))

    

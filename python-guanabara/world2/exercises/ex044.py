# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# à vista dinheiro/cheque:  10% de desconto
# à vista cartão:           5% de desconto
# em até 2x no cartão:      preço normal
# 3x ou mais no cartão:     20% de juros
preço_normal = float(input('Qual o preço do produto? '))
print('''Qual a forma de pagamento? 
[ 1 ]  à vista no dinheiro/cheque
[ 2 ]  à vista no cartão
[ 3 ]  parcelado no cartão
      ''')
cash_vista = (preço_normal / 100) * 10
card_vista = (preço_normal / 100) * 5
card_double = preço_normal
option = int(input('Escolha uma opção: '))

if option == 1:
    print('Parabéns você ganhou um desconto de 10% e vai pagar um total de {} R$ à vista '.format(preço_normal - cash_vista))
elif option == 2:
    print('Parabéns você ganhou um desconto de 5% e vai pagar um total de {} R$ à vista'.format(preço_normal - card_vista))
elif option == 3:
    parcela = int(input('Deseja parcelar em quantas vezes? '))
    calc_parc = preço_normal / parcela 
    if parcela <= 2:
        print('Você irá pagar {} R$ em {}x de {} R$'.format(preço_normal, parcela, calc_parc))
    elif parcela >= 3:
        parcela_juros = (preço_normal + preço_normal / 100 * 20)
        juros = parcela_juros / parcela
        print('Você terá juros e pagará R${} por mês, em {} vezes'.format(juros, parcela))
        print('Sua compra de R${} custará R${} no final'.format(preço_normal, parcela_juros))
else:
    print('Deu erro paizão')
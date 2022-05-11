# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 
#TODO
preço = IDproduto = total = overthousand = count = 0
barato = ' '
print('-=' * 10)
print('Loja Maneirinha')
print('-=' * 10)
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço R$: '))
    total += preço 
    count += 1
    
    if count == 1 or preço < menor:
        menor = preço
        barato = produto
        
    if preço > 1000:
        overthousand += 1
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
    
    
print(f'Total das compras: R${total:.2f}')
print(f'{overthousand} produtos custaram mais de R$1000,00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
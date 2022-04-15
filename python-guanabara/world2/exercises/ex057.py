# Faça um programa que leia o sexo de uma pessoa mas só aceite M ou F. Caso esteja errado peça a digitação 
# novamente até ter um valor correto.
n = str(input('Qual o seu sexo? [M / F]: ')).upper().strip()
while n != 'M' and n != 'F' :
    n = str(input('Por favor amigao, fale direito é [M / F]? ')).upper().strip()
    if n == 'M':
        print('Vlw otário')
    elif n == 'F':
        print('Vlw otária')
print('Obrigado pela participação fé!')    
        

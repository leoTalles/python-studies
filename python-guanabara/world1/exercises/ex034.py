# ESCREVA UUM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DE SEU
# AUMENTO
# PARA SALÁRIOS SUPERIORES A R$ 1250.00, CALCULE UM AUMENTO DE 10%
# PARA SALÁRIOS INFERIORES OU IGUAIS, O AUMENTO É DE 15%

user = str(input('Qual o seu nome? ')).title()
salario = float(input('{}, qual é o seu salário? em R$ '.format(user)))
supsalario = (salario / 100) * 10
infsalario = (salario / 100) * 15
newsalario1 = salario + supsalario
newsalario2 = salario + infsalario

if salario > 1250:
    print('\033[35m Houve um aumento de 10 por cento e seu novo salário é R$\033[m', newsalario1)
else:
    print('\033[35m Houve um aumento de 15 por cento seu novo salário é R$\033[m', newsalario2)
    
    
    

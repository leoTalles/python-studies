# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: ')) 
n2 = float(input('Digite a segunda nota: ')) 
m = (n1 + n2) / 2


if m <= 4.0:
    print('\033[1;31mVC FOI REPROVADO LIXO')
elif m >= 7.0:
    print('\033[1;32mAPROVADO CRIA TU É PICA')
else:
    print('\033[1;33mTÁ DE RECUPERAÇÃO, VAMO ESTUDAR!')
print('\033[1;37mTua média foi {:.1f}'.format(m))
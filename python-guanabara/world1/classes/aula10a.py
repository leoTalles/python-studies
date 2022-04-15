# CONDIÇÕES PT.1
''' 

if carro.esquerda():
    blocoTrue
else:
    blocoFalse
    
''' 

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Belo pau, seu carro é novo')
else:
    print('Péssimo pau, seu carro é velho')
print('--FIM--')

# CONDIÇÃO SIMPLIFICADA
'''
tempo=int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo <= 3 else 'Carro velho')
print('--FIM--')
'''

nome = str(input('Qual seu nome? '))
if nome == 'Leonardo':
    print('Que nome de gostoso pprt')
print('Bom dia, {}!'.format(nome.title()))
print('--FIM--')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média é {}pts'.format(m))
if m >= 6:
    print('Tu é pica neguin amassaste aprovado')
else:
    print('Burro reprovou kkkkkk')
('--FIM--')    

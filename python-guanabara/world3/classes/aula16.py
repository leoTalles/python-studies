# "TUPLAS SÃO IMUTÁVEIS"
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
  
print('Saí de casa comi pra c*$%#@!')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)
print(c.index(5, 1))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
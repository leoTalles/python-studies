# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Brasileirão, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Bragantino.

times = ('Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Internacional', 'Flamengo', 'Bragantino', 
         'Santos', 'São Paulo', 'Ceará', 'Botafogo', 'Avaí', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG', 'Atlético-GO',
         'Fortaleza', 'Juventude')

print(f'Os primeiros 5 colocados são {times[0:6]}')
print('-=-' * 20)

print(f'Os últimos 4 colocados são {times[16:]}')
print('-=-' * 20)

print('Aqui vai uma lista dos times em ordem ALFABÉTICA:')
print(sorted(times))
print('-=-' * 20)

print(f'O RB Bragantino está na posição {times.index("Bragantino") + 1}')


#pos in enumerate(times)
#print('O RB Bragantino está na {pos} posição')

# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA 
# PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$ 0,45 PARA VIAGENS
# MAIS LONGAS

distancia = float(input('Qual a distância em Km da viagem? '))
if distancia > 200:
    print('O preço da viagem está R${:.2f} '.format(distancia * 0.45))
else: 
    print('O preço da viagem está R${:.2f}'.format(distancia * 0.50))
    



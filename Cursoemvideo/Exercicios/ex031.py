# Desafio 031
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km
# e R$ 0,45 para viagens mais longas.
dist = float(input('Qual é a distância da viagem em Km? '))
if dist <= 200:
    print('O preço da passagem é R$ {:.2f}.'.format(0.5 * dist))
else:
    print('O preço da passagem é R$ {:.2f}.'.format(0.45 * dist))
print('')
dist = float(input('Qual é a distância da viagem em Km? '))
valor = dist * 0.5 if dist <= 200 else dist * 0.45
print('O preço da passagem é R$ {:.2f}.'.format(valor))

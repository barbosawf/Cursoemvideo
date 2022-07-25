# Desafio 029
# Escreve um programa que leia a velicidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
vel = float(input('Qual é a velocidade do carro? '))
if vel <= 80:
    print('Velocidade adequada.')
else:
    print('Você está {:.1f} Km/h acima da velocidade máxima permitida.'.format(vel - 80))
    print('Sua multa é de R$ {:.2f}.'.format((vel - 80) * 7))
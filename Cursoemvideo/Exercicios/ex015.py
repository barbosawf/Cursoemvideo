d = int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km o carro rodou? '))
print('O preço do aluguel do carro é de R$ {:.2f}.'.format(60*d + 0.15*km))

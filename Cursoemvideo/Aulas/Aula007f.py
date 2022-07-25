print('Desafio 008')
m = float(input('Tem quantos metros? '))
print('{} metros em centímetros é {} e em milímetros é {}'.format(m, m * 100, m * 1000), '\n')

print('Desafio 009')
n1 = int(input('Qual é o número? '))
print(' {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} '
      '\n {} x 8 = {} \n {} x 9 = {} \n '.format(n1, n1 * 1, n1, n1 * 2, n1, n1 * 3, n1, n1 * 4, n1, n1 * 5, n1, n1 * 6,
                                                 n1, n1 * 7, n1, n1 * 8, n1, n1 * 9))

print('Desafio 010')
d = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Você pode comprar $ {:.2f} dólares com esse dinheiro.'.format(d / 4.1), '\n')

print('Desafio 011')
lar = float(input('Qual a largura da parede? '))
a = float(input('Qual é a altura da parede? '))
area = lar * a
print('Sabendo que cada litro de tinta pinta 2 metros quadrados de parede,\n então, você irá precisar de {} litro de '
      'tinta.'.format(area/2), '\n')

print('Desafio 012')
p = float(input('Qual o preço do produto? '))
print('O novo valor do produto com 5% de desconto é {}.'. format(p - 0.05*p), '\n')

print('Desafio 013')
sal = float(input('Qual é o salário do funcionário? '))
print('O novo salário do funcionário com 15% de aumento é {}.'. format(sal + 0.15*sal), '\n')

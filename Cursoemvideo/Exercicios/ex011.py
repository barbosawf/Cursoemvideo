print('Desafio 011')
lar = float(input('Qual a largura da parede? '))
a = float(input('Qual é a altura da parede? '))
area = lar * a
print('Sabendo que cada litro de tinta pinta 2 metros quadrados de parede,\nentão, você irá precisar de {} litro(s) de '
      'tinta.'.format(area/2), '\n')
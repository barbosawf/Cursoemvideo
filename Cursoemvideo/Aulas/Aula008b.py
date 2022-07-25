from math import sqrt, floor, ceil

num = float(input('Digite um número: \n'))
raiz = sqrt(num)
print('A raiz de {} é {:.2f}.'.format(num, raiz))
print('A raiz de {} é {} arredondado para baixo.'.format(num, floor(raiz)))  # floor arredonda para baixo
print('A raiz de {} é {} arredondado para cima.'.format(num, ceil(raiz)))  # floor arredonda para cima

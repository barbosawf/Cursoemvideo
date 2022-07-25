n = float(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('O dobro de {} é {}.\nO triplo de {} é {}\nA raiz quadrada de {} é {:.2f}.'.format(n, d, n, t, n, r))
print('A raiz quadrada de {} é {:.2f}'.format(n, pow(n, (1 / 2))))

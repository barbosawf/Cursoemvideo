import math

print('Desafio 017')
a = float(input('Qual o tamanho do cateto adjacente? '))
b = float(input('Qual é o tamanho do cateto oposto? '))
h = math.sqrt(a**2 + b**2)
h2 = math.hypot(a, b)
print('A hipotenusa é {} de um triângulo retângulo cujo cateto adjacente é {} e o cateto oposto é {}.'
      .format(h, a, b))

print('A hipotenusa é {} de um triângulo retângulo cujo cateto adjacente é {} e o cateto oposto é {}.'
      .format(h2, a, b))

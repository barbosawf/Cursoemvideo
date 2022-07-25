import math
a = float(input('Qual é o ângulo? '))
b = math.radians(a)

print('O seno de {:.2f}º é {:.2f}.'.format(a, math.sin(b)))
print('O cosseno de {:.2f}º é {:.2f}.'.format(a, math.cos(b)))
print('A tangente de {:.2f}º é {:.2f}.'.format(a, math.tan(b)))

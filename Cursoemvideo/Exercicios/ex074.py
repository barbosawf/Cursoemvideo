"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

num = ''
from random import randint, sample
for c in range(1, 6):
    a = str(randint(1, 10))
    num += a

tupla = (tuple(num))
print(tupla)

print(max(tupla))
print(min(tupla))


a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')


a = tuple(randint(1, 10) for i in range(5))
print(a)
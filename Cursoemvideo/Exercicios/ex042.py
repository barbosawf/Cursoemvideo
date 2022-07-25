print('Desafio 042')
"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois alados iguais
- Escaleno: todos os lados diferentes
"""
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
print('')
if abs(b - c) < a < (b + c):
    print('As retas podem formar um triângulo!')
    if a == b == c:
        print('O triângulo é EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('O triângulo é ISÓSCELES.')
    else:
        print('O triângulo é ESCALENO')
else:
    print('As retas não podem formar um triângulo!')
# Tuplas: variável que guarda vários valores.

"""
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # no python novo a tupla funciona sem parênteses
print(lanche[1])
print(lanche[-2])
#lanche[1] = 'Refrigerante' #Não roda porque a túpla é imutável.

for c in range(0, 4):
    print(lanche[c])

for c in lanche:
    print(c)

for pos, comida in enumerate(lanche):
    print(f'Eu cou comer {comida} na posição {pos}.')

for c in range(0, len(lanche)):
    print(f'Eu cou comer {lanche[c]} na posição {c}.')

print(sorted(lanche))
"""

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = b + a
print(c)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.count(9))

print(c.index(1)) # qual a posição está o 1?

print(c.index(2)) # Pega a primeira ocorrência do 2.
print(c.index(2, 4)) # Pega a ocorrência do 2 a partir da posição 4.

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # apaga da memória.
print(pessoa)

lanche = ['Hamburguer', 'Refrigerante', 'Pizza', 'Pudim']
print(lanche)
lanche[3] = 'Picolé'
lanche.append('Bolo')
print(lanche)
lanche.insert(0, 'Cachorro-quente')
print(lanche)
del lanche[3]
print(lanche)
lanche.pop(3)
print(lanche)
lanche.remove('Bolo')
print(lanche)
lanche.pop()
print(lanche)
valores = list(range(9, 3, -1))
print(valores)
valores = [2, 5, 1, 7, 4]
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)

print('='*30)
valores = []
valores.append(5)
valores.append(2)
valores.append(3)

for v in valores:
    print(v, end=' ')

print('')
print('='*30)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

print('='*30)
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    print(cont)
print(valores)

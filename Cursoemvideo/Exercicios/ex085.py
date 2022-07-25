"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

lista = [[], []]
print('='*50)
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('='*50)

print(sorted(lista[0]))
print(sorted(lista[1]))



"""
lista = []
par = []
impar = []
print('='*50)
for c in range(1, 8):
    n = int(input('Digite um número? '))
    if len(lista) == 0:
        lista.append(n)
    else:
        if n % 2 == 0:
            lista.insert(0, n)
        else:
            lista.append(n)

print(lista)
"""
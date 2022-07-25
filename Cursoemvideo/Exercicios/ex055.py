"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
print('Desafio 055\n')
maior = 0
menor = 10**100
for c in range(1, 6):
    peso = float(input(f'Qual é o peso da {c}ª pessoa? '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'\nO maior peso é {maior} Kg.')
print(f'\nO menor peso é {menor} Kg.\n')

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Qual é o peso da {c}ª pessoa? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'\nO maior peso é {maior} Kg.')
print(f'O menor peso é {menor} Kg.')

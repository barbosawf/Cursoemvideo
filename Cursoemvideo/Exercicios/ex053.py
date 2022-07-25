"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
"""

# Exemplo: Anotaram a data da maratona

frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
poli = []

for c in range(len(frase) -1, -1, -1):
    poli.extend(frase[c])

if poli == list(frase):
    print('Sua sentença é um políndromo!')
else:
    print('Sua sentença NÃO é um políndromo!')

frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
inverso = ''

for c in range(len(frase) -1, -1, -1):
    inverso += frase[c]

if inverso == frase:
    print('Sua sentença é um palíndromo!')
else:
    print('Sua sentença NÃO é um palíndromo!')

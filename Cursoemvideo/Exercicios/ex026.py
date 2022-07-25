# Desafio 26
# Crie um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição a letra "A" aparece pela primeira vez
# Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase digitada.'.format(frase.count('A')))
print('A letra "A" aparece pela primera vez na posição {} na frase digitada.'.format(frase.find('A') + 1))
print('A letra "A" aparece pela última vez na posição {} na frase digitada.'.format(frase.rfind('A') + 1))

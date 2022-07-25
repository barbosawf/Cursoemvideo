"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00,
         'Transferidor', 4.20, 'Compasso', 9.90, 'Mochila', 120.50, 'Caneta', 4.65,
         'Livro', 38.10)

print('='*51)
print(f'{"LISTA DE PREÇOS":^50}')
print('='*51)

for c in range(0, 18):
    if c % 2 == 0:
        print('{:.<42}R$ '.format(itens[c]), end='')
    if c % 2 != 0:
        print(f'{itens[c]:6.2f}')
print('='*51)
print('')

print("="*51)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*51)

for c in range(0, len(itens), 2):
    print(f"{itens[c]:.<40}", f"R$ {itens[c+1]:>7.2f}")

print("="*51)
"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def area():
    print('='*50)
    print(f'{"Controle de Terrenos":^50}')
    print('='*50)
    l = float(input("LARGURA (m): "))
    c = float(input("COMPRIMENTO (m): "))
    print(f'A área de um terreno de {l} X {c} é {c*l:.2f} m².')
    print('='*50)


area()

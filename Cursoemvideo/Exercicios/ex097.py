"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def escreva(frase):
    tam = len(frase)
    print('=' * (tam + 4))
    print(f'  {frase}  ')
    print('=' * (tam + 4))


escreva('Curso em Vídeo!')
escreva('Amador')

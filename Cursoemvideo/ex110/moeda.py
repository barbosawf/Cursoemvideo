"""
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""


def moeda2(p=0, m='R$'):
    return f'{m} {p:8.2f}'.replace('.', ',')


def aumentar(n=100, porc=10, formatada=False):
    res = n + (porc / 100) * n
    return res if formatada is False else moeda2(res)


def diminuir(n=100, porc=10, formatada=False):
    res = n - (porc / 100) * n
    return res if formatada is False else moeda2(res)


def dobro(n=100, formatada=False):
    res = 2 * n
    return res if formatada is False else moeda2(res)


def metade(n=100, formatada=False):
    res = 0.5 * n
    return res if formatada is False else moeda2(res)


def moeda(n=100):
    n = f'{n:.2f}'
    k = ''
    for c in n:
        if c == '.':
            c = ','
        k += c
    resp = f'R$ {k}'
    return resp


def resumo(p=100, aumento=10, reducao=20):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    declara = ['Preço analisado:', 'Dobro do preço:', 'Metade do preço:', f'{aumento}% de aumento:',
               f'{reducao}% de redução:']
    functions = [moeda2(p), dobro(p, True), metade(p, True), aumentar(p, aumento, True), diminuir(p, reducao, True)]
    for c in range(0, len(declara)):
        print(f'{declara[c]:<25}', end='')
        print(f'{functions[c]:>15}')
    print('-'*40)


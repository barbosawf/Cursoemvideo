"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""


def leiaDinheiro(dim=''):
    while True:
        resp = str(input(dim)).replace(',', '.').strip()
        if resp.isalpha() or resp == '':
            print(f'\33[0;31mERRO! "{resp}" é um preço inválido!\33[m')
        else:
            return float(resp)
            break



def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

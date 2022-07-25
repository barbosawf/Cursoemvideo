"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(ano):
    """
    Função para saber o status da obrigatoriedade de votação do cidadão.
    :param ano: ano de nascimento do cidadão.
    :return: retorna o status da obrigatoriedade de votação para o cidadão.
    """
    from datetime import datetime  # IMPORTAR DENTRO DA FUNÇÃO ECONOMIZA MEMÓRIA
    idade = datetime.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    if 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'


nasc = int(input('Ano de nascimento: '))
print(voto(nasc))

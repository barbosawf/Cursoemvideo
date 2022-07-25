"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:
Quantidade de notas
— A maior nota
— A menor nota
— A média da turma
— A situação (opcional)
"""


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    param n: uma ou mais notas dos alunos (aceita várias notas).
    param sit: valor opcional, indicando se deve ou não adicionar a situação.
    return: dicionário com várias informações sobre a situação do aluno.
    """
    dic = {'Total': len(n), 'Maior': max(n), 'Menor': min(n), 'Média': round(sum(n)/len(n), 2)}
    if sit:
        if dic['Média'] < 6:
            dic['Situação'] = 'RUIM'
        elif 6 <= dic['Média'] < 7:
            dic['Situação'] = 'BOA'
        elif 7 <= dic['Média'] < 8:
            dic['Situação'] = 'ÓTIMA'
        elif dic['Média'] >= 8:
            dic['Situação'] = 'EXCELENTE'
    return dic


resp = notas(3.4, 2.4, 5.3, 9.5, 10, sit=True)
print(resp)

help(notas)

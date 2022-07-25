"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
import time


def escreva(msg='', cor_fundo='Nenhum', cor_fonte='Branco', caracter='-', show_caracter=False):
    cores_fundo = {'Preto': '\033[40m', 'Vermelho': '\033[41m', 'Verde': '\033[42m', 'Amarelo': '\033[43m',
                   'Azul': '\033[44m', 'Magenta': '\033[45m', 'Cyan': '\033[46m', 'Cinza_Claro': '\033[47m',
                   'Cinza_Escuro': '\033[100m', 'Vermelho_Claro': '\033[101m', 'Verde_Claro': '\033[102m',
                   'Amarelo_Claro': '\033[103m', 'Azul_Claro': '\033[104m', 'Magenta_Claro': '\033[105m',
                   'Cyan_Claro': '\033[106m', 'Branco': '\033[107m', 'Nenhum': '\33[0m'}
    cores_fonte = {'Preto': '\033[30m', 'Vermelho': '\033[31m', 'Verde': '\033[32m', 'Amarelo': '\033[33m',
                   'Azul': '\033[34m', 'Magenta': '\033[35m', 'Cyan': '\033[36m', 'Cinza_Claro': '\033[37m',
                   'Cinza_Escuro': '\033[90m', 'Vermelho_Claro': '\033[91m', 'Verde_Claro': '\033[92m',
                   'Amarelo_Claro': '\033[93m', 'Azul_Claro': '\033[94m', 'Magenta_Claro': '\033[95m',
                   'Cyan_Claro': '\033[96m', 'Branco': '\033[97m'}
    if cor_fundo in cores_fundo.keys():
        cor_fundo = cores_fundo[cor_fundo]
    else:
        cor_fundo = cores_fundo['Nenhum']
    if cor_fonte in cores_fonte.keys():
        cor_fonte = cores_fonte[cor_fonte]
    else:
        cor_fonte = cores_fonte['Branco']
    if len(msg.strip()) > 0:
        tam = len(msg.strip()) + 4
        if show_caracter:
            print(f'{cor_fundo}{cor_fonte}{caracter}' * tam)
        print(f'  {cor_fundo}{cor_fonte}{msg}  ')
        if show_caracter:
            print(f'{cor_fundo}{cor_fonte}{caracter}' * tam)
        print(f'{cores_fundo["Nenhum"]}', end='')
    else:
        print(f'{cor_fundo}{cor_fonte}', end='')


def pyHelp():
    while True:
        escreva('SISTEMA DE AJUDA PyHELP', cor_fundo='Verde_Claro', caracter='~', show_caracter=True)
        resp = str(input(f'\033[0;97mFunção ou Biblioteca [fim para sair]: ')).strip()
        if resp != 'fim':
            escreva(f'Acessando o comando {resp}.', cor_fundo='Amarelo_Claro', caracter='~', show_caracter=True)
            time.sleep(2)
            escreva(cor_fundo='Branco', cor_fonte='Preto', show_caracter=False)
            help(resp)
        if resp.lower() == 'fim':
            escreva('ATÉ LOGO!', cor_fundo='Vermelho_Claro', caracter='~', show_caracter=True)
            break


pyHelp()

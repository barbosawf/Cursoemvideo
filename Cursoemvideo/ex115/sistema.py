import time

from Cursoemvideo.ex115.lib.interface import *  # importa todas as funções

from Cursoemvideo.ex115.lib.arquivo import *  # importa todas as funções

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho('SISTEMA ARQUIVO V1.0')
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\33[1;35mSaindo do Sistema... Até logo!\33[m', 60)
        break
    else:
        print('\33[0;31mERRO! Digite uma opção válida!\33[m')
    time.sleep(3)

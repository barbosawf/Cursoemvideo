from Cursoemvideo.ex115.lib.interface import *  # importa todas as funções


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # rt significa read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # wt significa write text, + se o arquivo não existir ele cria.
        a.close()
    except:
        print('\33[0;31mHouve um erro na criação do arquivo!\33[m')
    else:
        print(f'\33[0;33mArquivo {nome} criado com sucesso!\33[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\33[0;31mErro ao ler o arquivo!\33[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(f'\33[1;35m{"Nome":<45}{"Idade":>5}\33[0m')
        print('-'*50)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<45}{dado[1]:>5}')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\33[0;31mHouve um Erro na abertura do arquivo!\33[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\33[0;31mHouve um Erro na escrita dos dados!\33[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


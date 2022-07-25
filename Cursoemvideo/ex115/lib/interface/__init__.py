def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\33[0;31mERRO! Por favor, digite um número inteiro.\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[0;33mEntrada de dados interrompida pelo usuário.\33[m')
            return 'NENHUM'
        else:
            return n


def linha(tam=50):
    return '-' * tam


def cabeçalho(txt, centralidade=50):
    print(linha())
    print(str(txt).center(centralidade))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\33[0;33m{c}\33[m - \33[0;34m{item}\33[0m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

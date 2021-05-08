from time import sleep

def mostraLinha(tam=50):
    return '-' * tam


def cabeçalho(txt):
    print(mostraLinha())
    print(txt.center(50))
    print(mostraLinha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(mostraLinha())
    resposta = leiaInt('\033[32mSua Opção:\033[m ')
    return resposta


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print()
            print(mostraLinha())
            print('\033[1;31mERRO: por favor, digite um número inteiro válido\033[m')
            print(mostraLinha(),'\n')
            sleep(1)
            continue
        else:
            return n
from lib.Interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'w+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
           dado = linha.split(';')
           dado[1] = dado[1].replace('\n', '')
           print(f'{dado[0]:<30}{dado[1]:>3} anos')

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'a')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
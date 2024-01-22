'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

Aula Anterior
'''
from time import sleep


def ajuda(comando):
    """
    Mostra o manual de um comando específico.

    Parâmetros:
    comando (str): Comando para exibir o manual.
    """
    titulo(f"Acessando o manual do comando '{comando}'", cor='azul')
    print(cod_cores['azul'])
    help(comando)
    print(cod_cores['limpar'])


def titulo(msg, cor='branco'):
    """
    Imprime um título formatado.

    Parâmetros:
    msg (str): Mensagem do título.
    cor (str): Cor do título (padrão é 'branco').
    """
    print(cod_cores[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(cod_cores['limpar'])
    sleep(1)


# Dicionário de códigos de cores ANSI
cod_cores = {
    'limpar': '\033[m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;33m',
    'preto': '\033[1;30m',
    'branco': '\033[1;97m',
}

# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor='amarelo')
    comando = input(
        'Função ou Biblioteca (ou digite "FIM" para encerrar): ').strip().lower()

    if comando == 'fim':
        titulo('ATÉ LOGO!', cor='azul')
        break

    ajuda(comando)

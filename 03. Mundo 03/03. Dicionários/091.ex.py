'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''


import random
import operator
import time

# Lista para armazenar os dados dos jogadores
jogadores = []

# Loop para coletar os dados dos jogadores
for n in range(1, 5):
    # Dicionário para armazenar o nome e o número do jogador atual
    jogador = {}

    # Coleta o nome do jogador e converte para título (capitalizando)
    jogador['Nome'] = str(input(f'Jogador {n}: ')).title()

    # Gera um número aleatório de 1 a 6 e o associa ao jogador
    jogador['Número'] = random.randint(1, 6)

    # Adiciona o dicionário do jogador à lista de jogadores
    jogadores.append(jogador)

# Ordena a lista de jogadores com base no valor associado à chave 'Número' em ordem decrescente
ranking = sorted(jogadores, key=operator.itemgetter('Número'), reverse=True)

# Exibe o ranking
for posicao, jogador in enumerate(ranking, start=1):
    time.sleep(1)
    print(f'{posicao}º lugar: {jogador["Nome"]} tirou {jogador["Número"]}')

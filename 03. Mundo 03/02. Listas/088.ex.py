'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''

import random
import time

# Imprime uma linha de separação
print('-' * 50)

# Imprime o cabeçalho centralizado
print('JOGOS PARA MEGA SENA'.center(50))

# Imprime outra linha de separação
print('-' * 50)

# Solicita ao usuário o número de jogos desejado
numero_de_jogos = int(input('Número de jogos: '))

# Imprime a mensagem indicando que os jogos estão sendo sorteados
print(f' < Sorteando os {numero_de_jogos} jogos > '.center(50, '-'))

# Lista para armazenar os jogos sorteados
lista_jogos = []

# Loop para gerar os jogos
for jogos in range(numero_de_jogos):
    # Gera um jogo com 6 números diferentes de 1 a 60
    jogo = random.sample(range(1, 61), 6)

    # Adiciona o jogo à lista, ordenando os números
    lista_jogos.append(sorted(jogo))

# Loop para imprimir os jogos com pausa de 0.5 segundos entre cada impressão
for index, jogo in enumerate(lista_jogos, 1):
    time.sleep(0.5)
    print(f'Jogo {index}: {jogo}')

# Pausa antes de imprimir a mensagem de "Boa Sorte"
time.sleep(0.5)

# Imprime a mensagem "Boa Sorte" centralizada com linhas de separação
print(' < Boa Sorte > '.center(50, '-'))

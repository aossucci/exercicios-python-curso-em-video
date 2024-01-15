'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols 
feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''


# Lista para armazenar os dados de vários jogadores
lista_jogadores = []

# Loop principal para inserção de dados de jogadores
while True:
    # Dicionário para armazenar os dados de um jogador
    dados_jogador = {}
    gols = []

    # Captura o nome e a quantidade de partidas do jogador
    dados_jogador['jogador'] = str(input('Nome do jogador: ')).title()
    dados_jogador['partidas'] = int(input('Partidas jogadas: '))

    # Loop para capturar a quantidade de gols em cada partida
    for partida in range(dados_jogador['partidas']):
        gols_na_partida = int(input(f'Gols na partida {partida + 1}: '))
        gols.append(gols_na_partida)

    # Adiciona a lista de gols e o total de gols ao dicionário do jogador
    dados_jogador['gols'] = gols
    dados_jogador['total_de_gols'] = sum(gols)

    # Adiciona o dicionário do jogador à lista de jogadores
    lista_jogadores.append(dados_jogador)

    # Pergunta se deseja continuar inserindo dados de jogadores
    continuar = str(input('Quer continuar? S|N: ')).upper()
    if continuar == 'N':
        break

# Impressão dos dados de todos os jogadores
for jogador in lista_jogadores:
    print("\nDados do jogador:")
    print(f"Nome: {dados_jogador['jogador']}")
    print(f"Partidas jogadas: {dados_jogador['partidas']}")
    print("Gols por partida:")

    # Loop para imprimir os gols em cada partida
    for i, gols_na_partida in enumerate(dados_jogador['gols'], start=1):
        print(f"   Partida {i}: {gols_na_partida} gols")

    # Imprime o total de gols do jogador
    print(f"Total de gols: {dados_jogador['total_de_gols']}")
    print("=" * 30)

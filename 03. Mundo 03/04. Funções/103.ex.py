'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''

# Define uma função chamada ficha com dois parâmetros opcionais: jogador e gols.


def ficha(jogador='desconhecido', gols=0):
    # Retorna uma string formatada com as informações do jogador.
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'


# Solicita ao usuário que insira o nome do jogador e converte para o formato de título (iniciais maiúsculas).
nome_jogador = input('Nome do jogador: ').title()

# Solicita ao usuário que insira a quantidade de gols.
quantidade_gols = int(input('Quantidade de gols: '))

# Chama a função ficha com os valores fornecidos pelo usuário (ou os padrões se não fornecidos).
# Se o nome_jogador estiver vazio, a função usa o valor padrão 'desconhecido'.
# Se a quantidade_gols estiver vazia, a função usa o valor padrão 0.
dados_jogador = ficha(jogador=nome_jogador if nome_jogador else 'desconhecido',
                      gols=quantidade_gols if quantidade_gols else 0)

# Exibe a ficha do jogador.
print(dados_jogador)

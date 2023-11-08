'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

serie_A = ('Botafogo', 'Bragantino', 'Flamengo', 'Palmeiras', 'Athletico-PR', 'Grêmio', 'Atlético-MG',
           'Fortaleza', 'Fluminense', 'São Paulo', 'Cuiabá', 'Internacional', 'Bahia', 'Cruzeiro',
           'Corinthians', 'Goiás', 'Vasco', 'Santos', 'Coritiba', 'América-MG')

# Os 5 primeiros times.
print('Lista dos 5 primeiros times do campeonato')
for pos, time in enumerate(serie_A[0:4]):
    print(f'{time} está em {serie_A.index(serie_A[pos])}º')
print('-' * 20)

# Os últimos 4 colocados.
print('Lista dos quatro últimos times do campeonato')
for pos in range(len(serie_A) - 4, len(serie_A)):
    print(f'{serie_A[pos]} está em {serie_A.index(serie_A[pos])}º')
print('-' * 20)

# times em ordem alfabética
print('Times em ordem alfabética')
serie_A_sorted = sorted(serie_A)
for time in serie_A_sorted:
    print(time)
print('-' * 20)

# pesquisar posição do time no campeonato
print('Pesquisa de time na tabela')
timePesquisa = input('Quer pesquisar qual time: ').capitalize()
encontrado = False
for time in range(len(serie_A)):
    if serie_A[time] == timePesquisa:
        print(f'O {timePesquisa} está na posição {serie_A.index(timePesquisa)}º')
        encontrado = True
if not encontrado:
    print('O time em questão não está disputando o campeonato')

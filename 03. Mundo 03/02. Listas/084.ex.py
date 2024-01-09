'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:    
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.'''

# criando um looping para inserir os nomes e os pesos das pessoas na lista pessoas
pessoas = []
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas.append((nome, peso))
    pergunta = input('Voce quer continuar? [S|N]').upper()
    if pergunta == 'N':
        break

# definindo quais pessoas da lista'pessoas' são leves e pesadas
pesadas = []
leves = []
for pessoa in pessoas:
    nome, peso = pessoa
    if peso >= 80:
        pesadas.append((nome, peso))
    else:
        leves.append((nome, peso))
print('-' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas')

if pesadas:
    print('As pessoas mais pesadas são:')
    for pessoa in pesadas:
        print(f'{pessoa[0]} com {pessoa[1]}kg')
else:
    print('Não há pessoas com 80kg ou mais cadastradas')

if leves:
    print('As pessoas mais leves são:')
    for pessoa in leves:
        print(f'{pessoa[0]} com {pessoa[1]}kg')
else:
    print('Não há pessoas com menos de 80kg cadastradas')

print('-' * 30)

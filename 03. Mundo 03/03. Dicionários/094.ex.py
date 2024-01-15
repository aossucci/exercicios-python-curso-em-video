'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

# Inicializa uma lista vazia para armazenar os dados de todas as pessoas
pessoas = []
# Inicializa uma lista vazia para armazenar os dados das mulheres
mulheres = []

# Loop que solicita informações sobre nome, sexo e idade até que o usuário decida parar
while True:
    # Inicializa um dicionário para armazenar os dados de uma pessoa
    pessoa = {}

    # Solicita e valida o nome
    pessoa['Nome'] = input('Nome: ').title()

    # Solicita e valida o sexo
    while True:
        pessoa['Sexo'] = input('Sexo: [M|F]: ').upper()
        # Verifica se a opção é válida ('M' ou 'F')
        if pessoa['Sexo'] in ['M', 'F']:
            break
        else:
            print('Opção inválida. Digite M para masculino ou F para feminino.')

    # Solicita e valida a idade
    while True:
        try:
            pessoa['Idade'] = int(input('Idade: '))
            # Verifica se a idade é um número positivo
            if pessoa['Idade'] >= 0:
                break
            else:
                print('Idade deve ser um número positivo.')
        except ValueError:
            print('Por favor, digite um número inteiro para a idade.')

    # Adiciona o dicionário da pessoa à lista de pessoas
    pessoas.append(pessoa)

    # Verifica se a pessoa é do sexo feminino e, se for, a adiciona à lista de mulheres
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa)

    # Pergunta ao usuário se deseja continuar inserindo informações
    continuar = input('Quer continuar? [S|N]: ').upper()

    # Se o usuário escolher 'N', o loop é interrompido
    if continuar == 'N':
        break

# Imprime os dados completos de todas as pessoas cadastradas
print("---- Dados das Pessoas ----")
for p in pessoas:
    print(p)

# Imprime o número total de pessoas cadastradas
print(f'\nForam cadastradas {len(pessoas)} pessoas')

# Calcula e imprime a média de idade das pessoas cadastradas
if len(pessoas) > 0:
    media_idade = sum(p['Idade'] for p in pessoas) / len(pessoas)
    print(f'A média de idade das pessoas cadastradas é de {media_idade:.2f}')

# Imprime a lista de mulheres cadastradas
print(f'\nMulheres cadastradas: \n {mulheres}')

# Cria uma lista de pessoas com idade acima da média
pessoas_acima_media = [p for p in pessoas if p['Idade'] > media_idade]

# Imprime a lista de pessoas com idade acima da média
print('\nPessoas com idade acima da média:')
for p in pessoas_acima_media:
    print(p)

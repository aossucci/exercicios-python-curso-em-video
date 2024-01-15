'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

# Criando um dicionário vazio chamado boletim
boletim = {}

# Solicitando e armazenando o nome do aluno no dicionário
boletim['nome'] = str(input('Nome do aluno: ')).title()

# Solicitando e armazenando a média do aluno no dicionário
boletim['media'] = float(input('Média: '))

# Verificando a média para determinar a situação do aluno
if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
else:
    boletim['situacao'] = 'Recuperação'

# Imprimindo o dicionário completo
print(boletim)

# Iterando sobre chaves e valores do dicionário e imprimindo
for chave, valor in boletim.items():
    print(f'{chave}: {valor}')

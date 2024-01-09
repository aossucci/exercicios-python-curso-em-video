'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma 
lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa 
mostrar as notas de cada aluno individualmente.
'''

# Inicializa a lista para armazenar os dados dos alunos
boletim = []

# Loop para coletar informações sobre os alunos
while True:
    # Solicita o nome do aluno e converte a primeira letra de cada palavra para maiúscula
    nome = str(input('Nome do aluno: ')).title()
    # Solicita as notas do 1º e 2º bimestre
    nota1 = float(input('Nota 1º bimestre: '))
    nota2 = float(input('Nota 2º bimestre: '))
    # Armazena as informações do aluno em uma lista e adiciona à lista do boletim
    aluno = [nome, nota1, nota2]
    boletim.append(aluno)
    # Pergunta ao usuário se deseja continuar inserindo dados
    continuar = input('Você quer continuar? [S|N]').upper()
    # Se o usuário escolhe 'N', encerra o loop
    if continuar == 'N':
        break

# Imprime o cabeçalho do boletim
print(f'Boletim'.center(30, '-'))

# Loop para calcular a média e imprimir as informações de cada aluno
for index, aluno in enumerate(boletim):
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    # Calcula a média das notas
    media = (nota1 + nota2) / 2
    # Imprime as informações formatadas do aluno
    print(f'{index}. Nome: {nome} - Média: {media:.2f}')

# Segundo loop para permitir que o usuário veja as notas de cada aluno individualmente
while True:
    # Solicita ao usuário o número do aluno para visualizar as notas
    notas_aluno = int(
        input('Escolha o número do aluno para abrir as notas (ou 0 para sair): '))
    # Se o usuário escolhe 0, encerra o segundo loop
    if notas_aluno == 0:
        break
    # Verifica se o número do aluno está dentro da faixa válida
    if 1 <= notas_aluno <= len(boletim):
        # Obtém as informações do aluno selecionado
        aluno_selecionado = boletim[notas_aluno - 1]
        nome = aluno_selecionado[0]
        nota1 = aluno_selecionado[1]
        nota2 = aluno_selecionado[2]
        # Calcula a média das notas do aluno selecionado
        media = (nota1 + nota2) / 2
        # Imprime as notas do aluno individualmente
        print(
            f'Notas do aluno {notas_aluno}: {nome} - Nota 1: {nota1}, Nota 2: {nota2} - Média: {media:.2f}')
    else:
        # Se o número do aluno não for válido, solicita ao usuário tentar novamente
        print('Número de aluno inválido. Tente novamente.')

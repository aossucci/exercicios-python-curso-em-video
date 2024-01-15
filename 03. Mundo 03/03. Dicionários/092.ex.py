'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá 
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a 
pessoa vai se aposentar.'''

from datetime import datetime

# Obtém a data atual
data_atual = datetime.now()
pessoas = []

while True:
    pessoa = {}

    # Obtém informações pessoais
    pessoa['nome'] = str(input('Nome completo: ')).title()
    pessoa['ano_nascimento'] = int(input("Digite o ano de nascimento: "))
    pessoa['numero_ctps'] = int(
        input("Digite o número da CTPS (0 - não tem): "))
    pessoa['idade'] = data_atual.year - pessoa['ano_nascimento']

    # Verifica se a pessoa tem CTPS
    if pessoa['numero_ctps'] != 0:
        pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
        pessoa['salario'] = float(input('Salário: R$ '))

        # Calcula anos de contribuição e anos para aposentadoria
        anos_contribuicao = data_atual.year - pessoa['ano_contratacao']
        idade_aposentadoria = 65  # Idade padrão de aposentadoria
        anos_para_aposentar = max(0, idade_aposentadoria - pessoa['idade'])
        pessoa['anos_para_aposentar'] = anos_para_aposentar

    # Adiciona informações da pessoa à lista de pessoas
    pessoas.append(pessoa)

    # Exibe as informações da pessoa
    for k, v in pessoa.items():
        print(f'{k}: {v}')

    # Pergunta se deseja continuar cadastrando pessoas
    continuar = str(input('Continuar? [S|N]: '))
    if continuar.lower() in 'n':
        break

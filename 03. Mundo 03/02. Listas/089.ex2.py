ficha = list()

# Loop para inserir informações dos alunos
while True:
    nome = input('Nome do aluno: ').title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    # Cálculo da média
    media = (nota1 + nota2) / 2

    # Adiciona os dados do aluno à lista composta
    ficha.append([nome, [nota1, nota2], media])

    # Solicita ao usuário se deseja continuar
    continuar = input('Adicionar outro aluno? [S|N]: ').upper()

    # Encerra o loop se o usuário não quiser continuar
    if continuar in 'Nn':
        break

# Imprime a tabela inicial com os dados dos alunos
print('-' * 40)
print(f'{"Nº.":<4}{"Nome":<15}{"Média":>10}')
print('-' * 40)
for index, aluno in enumerate(ficha, start=1):
    print(f'{index:<4}{aluno[0]:<15}{aluno[2]:>10.1f}')

# Loop para mostrar notas individualmente
while True:
    print('-' * 40)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    # Encerra o programa se a opção for 999
    if opcao == 999:
        print('Finalizando')
        break

    # Verifica se a opção está dentro do intervalo válido
    if 1 <= opcao <= len(ficha):
        # Imprime as notas do aluno selecionado
        print(f'Notas de {ficha[opcao - 1][0]} são {ficha[opcao - 1][1]}')
    else:
        print('Opção inválida. Tente novamente.')

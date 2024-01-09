'''Exercício Python 079: Crie um programa onde o usuário possa digitar 
vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

numeros = []

while True:
    num = int(input('Digite um número: '))
    # adicionar apenas números que não constem na lista
    if num not in numeros:
        numeros.append(num)
        print('Número adicionado com sucesso')
    else:
        print('Número repetido, número não adicionado')
    pergunta = input('Deseja continuar? [S|N]').upper()
    if pergunta == 'N':
        break

numeros_em_ordem = sorted(numeros)
print(f'Os números digitados em ordem crescente são {numeros_em_ordem}')

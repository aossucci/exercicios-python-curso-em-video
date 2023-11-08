'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos = ('TV', 3000,
            'Notebook', 4000,
            'Monitor', 1000)

print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:-<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)

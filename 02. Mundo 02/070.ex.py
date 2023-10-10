'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

preco = preco_maior_1000 = menor_valor = cont = 0
produto_mais_barato = ''
while True:
    nome_produto = str(input('Nome do produto: '))
    preco_produto = float(input('Preço: R$'))
    cont += 1
    continuar = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]   
    preco += preco_produto
    if preco_produto > 1000:
        preco_maior_1000 += 1  
    if cont == 1 or preco_produto < menor_valor:
        menor_valor = preco_produto
        produto_mais_barato = nome_produto            
    if continuar == 'N':
        break
    
print(f'Valor total da compra: R${preco:.2f}')
print(f'{preco_maior_1000} produtos custam mais que R$1000')
print(f'O produto mais barato é o {produto_mais_barato} e custa R${menor_valor}')    
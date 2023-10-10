'''Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto'''

precoProduto = float(input('Preço do produto: R$'))
desconto = 5 / 100
precoComDesconto = precoProduto * ( 1 - desconto)

print(f'O preço do produto é R${precoProduto:.2f}, com o desconto de 5%, o valor caiu para R${precoComDesconto:.2f}')

'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode
comprar'''

dinheiro = float(input('Quanto dinheiro tem na carteira? R$'))
cotacaoDolar = 4.27
dolar = dinheiro * cotacaoDolar

print(f'Com {dinheiro} reais voce pode comprar {dolar:.2f} dólares')

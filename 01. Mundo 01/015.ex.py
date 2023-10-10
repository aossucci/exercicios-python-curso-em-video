'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 por dia e 0,15 por km rodado'''

kmPercorridos = float(input('Quilometragem percorrida: '))
diasAlugados = int(input('Dias alugados: '))
valorAPagar = (kmPercorridos * 0.15) + (diasAlugados * 60)

print(f'Preço a pargar: R${valorAPagar:.2f}')
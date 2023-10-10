'''Faça um programa para calcular quantos litros de tinta preciso para pintar uma parede'''

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
areaParede = altura * largura
rendimentoTinta = areaParede * 0.5

print(f'Para pintar uma parede de {areaParede:.2f}m² são necessários {rendimentoTinta:.2f} litros de tinta')
'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

dist = int(input('Digite a distância da viagem em Km: '))


if dist <= 200:
    preco = dist * 0.50   
else:
    preco = dist * 0.45

print(f'O preço da passagem é de R${preco:.2f}')
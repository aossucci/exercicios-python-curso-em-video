'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

import random

velocidade = random.randint(0, 220)
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'Você está acima da valocidade máxima permitida de 80km/h,' 
          f'sua velocidade é de {velocidade} e deverá pagar uma multa de R${multa}')      
else:
    print('Abaixo da velocidade máxima')    

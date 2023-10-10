'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e mostre o comprimento da hipotenusa'''
import math

catetoOposto = float(input('Medida do cateto oposto: '))
catetoAdjacente = float(input('Medida do cateto adjacente: '))
hipotenusa = math.sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))

print(f'A hipotenusa do triangulo é {hipotenusa}')

math.hypot(catetoAdjacente, catetoOposto)

print(f'A hipotenusa do triangulo é {hipotenusa}')
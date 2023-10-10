'''Escreva um programa que leia um valor em metros e o converta em cm e mm'''

medida = float(input('Digite a medida em metros: '))
medidaCm = medida * 100
medidaMm = medida * 1000

print(f'{medida} metros, equivalem a {medidaCm:.0f}cm e a {medidaMm:.0f}mm')

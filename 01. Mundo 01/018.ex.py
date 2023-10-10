'''Faça um programa que leia um angulo qualqur e mostre na tela o valor do seno, cosseno e tangente do angulo'''
import math

angulo = float(input('Qual o ângulo? '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'Para o angulo {angulo}, temos:\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')
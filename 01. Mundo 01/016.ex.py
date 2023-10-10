'''Crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira'''
from math import trunc

num = float(input('Digite um número: '))
print(f'O numero digitado foi {num}, sua parte inteira é {trunc(num)}')
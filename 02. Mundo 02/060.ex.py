'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:'''

from math import factorial

num = int(input('Digite um número qualquer: '))

'''f = factorial(num)
print(f)'''


cont = num
fatorial = 1
while cont > 0:
    fatorial *=  cont
    cont -= 1
    
print(f' O fatorial de {num} é {fatorial}')

